from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time



def send_warning(driver, num):

    # Click username/repo_name button
    driver.find_element(By.XPATH, f"""/html/body/div[1]/div[5]/main/react-app
                                    /div/div/div[1]/div/div/div[2]/div[2]/div
                                    /div/div[4]/div/div/div[{str(num)}]/div[1]
                                    /div[1]/div[2]/div/a[1]""").click()

    time.sleep(3)


    # Click Issues tab
    issues_xpath = '//*[@id="issues-tab"]'
    try:
        elem = WebDriverWait(driver, 0.5).until(
        EC.presence_of_element_located((By.XPATH, issues_xpath))
        )
    finally:
        driver.find_element(By.XPATH, issues_xpath).click()

    time.sleep(3)


    # Click "New" to initiate an issue creation
    init_xpath = '/html/body/div[1]/div[5]/div/main/turbo-frame/div/div[2]/div[2]/a'
    try:
        elem = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, init_xpath))
        )
    finally:
        driver.find_element(By.XPATH, init_xpath).click()

    time.sleep(3)


    # Type title and body of the issue
    title_input_xpath = '//*[@id="issue_title"]'

    try:
        elem = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, title_input_xpath))
        )
    finally:
        driver.find_element(By.XPATH, title_input_xpath).send_keys("test title")
        time.sleep(3)
        driver.find_element(By.ID, "issue_body").send_keys("test body")

    time.sleep(3)


    # Click submit to create the issue
    submit_xpath = '//*[@id="new_issue"]/div/div/div[1]/div/div[1]/div/div[3]/button'
    try:
        elem = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, submit_xpath))
        )
    finally:
        driver.find_element(By.XPATH, submit_xpath).click()


    # Go back to the env files page
    driver.back()
    driver.back()
    driver.back()
    driver.back()

    time.sleep(3)
