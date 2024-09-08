from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

import logging
import time
import datetime

from app.crawler.data.cookies import GITHUB_COOKIES
from app.crawler.data.openai_key_names import OPENAI_KEY_NAMES

from app.crawler.check import check_key
from app.crawler.storage import add_key, get_keys
from app.crawler.warning import send_warning
from app.crawler.statistics import update_stat, get_stat



"""

START SCANNING OPENAI KEYS FROM GITHUB'S .ENV FILES

"""


def start_scan():

    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (helps with some issues)
    chrome_options.add_argument("--window-size=1920x1080")  # Set window size (optional)
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model (useful in Docker)
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems in containers

    # Initialize the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    first_refresh = False

    all_keys = get_keys()

    stat = get_stat()

    total_found, total_comp = int(stat[1]), int(stat[3])
    last_found = 0
    last_comp = 0

    for api_name in OPENAI_KEY_NAMES:

        logging.info(f"Searching for {api_name} in GitHub...")

        driver.get(f"https://github.com/search?q=path%3A**%2F.env+{api_name}%3D&type=code")

        # Apply cookies to session to login
        for cookie in GITHUB_COOKIES:
            name = cookie['name']
            value = cookie['value']

            driver.add_cookie({'name': name, 'value': value})

        # Refresh the page to apply the cookies and authenticate the session
        if not first_refresh:
            driver.refresh()
            first_refresh = True

        # Loop through the existed pages
        # p.s. range of 2-100 is hypothetical, usually there are up to 5 pages
        for page in range(2, 100):

            page_source = driver.page_source

            soup = BeautifulSoup(page_source, 'html.parser')

            # Check if the page is an error page
            try:
                error_check = soup.find("div", {"class": "container"}).find("h1").text
                while error_check == "Whoa there!":
                    time.sleep(5)
                    driver.refresh()

                    page_source = driver.page_source
                    soup = BeautifulSoup(page_source, 'html.parser')
                    error_check = soup.find("div", {"class": "container"}).find("h1").text
            except:
                # No error page
                pass

            envs = soup.find_all("div", {"class": "Box-sc-g0xbh4-0 kNKjla"})

            if envs:

                env_num = 0

                # Loop through the .env files
                for env in envs:

                    env_num += 1

                    lines = env.find_all('tr')

                    for line in lines:
                        if line.find("mark"):
                            key = line.text.split('=')[1].strip().replace("'", "").replace('"', '').replace("<", "").replace(">", "")

                            # Check if the key structure is valid
                            if key and (len(key) == 51 or len(key) == 132) and key.startswith("sk-") and key not in all_keys:

                                add_key(key)
                                all_keys.add(key)
                                logging.info(f"Key found: {key}")

                                last_found += 1

                                # Check if the key is valid by sending a request to the OpenAI API
                                if check_key(key):

                                    # Send a warning to the user repo as an issue if the key is compromised
                                    send_warning(driver, env_num)

                                    last_comp += 1
                                    #
                                    pass


            else:
                # Break the loop if page is empty (no .env files found)
                break


            # Click button to go to the next page if exists
            try:
                buttons_tab = driver.find_elements(By.TAG_NAME, "nav")[-1]
                buttons_tab.find_element(By.LINK_TEXT, str(page)).click()

                time.sleep(2)
            except:
                # Break the loop if no more pages
                break

    # Update the statistics
    total_found += last_found
    total_comp += last_comp

    scan_time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    update_stat(scan_time, total_found, last_found, total_comp, last_comp)
