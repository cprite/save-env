<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="200" height="200">
  </a>

  <p align="center">
    <br />
    <br />
    <br />
    <a href="https://github.com/cprite/save-env/issues">Report Bug</a>
    ·
    <a href="https://github.com/cprite/save-env/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#disclaimer">[!] Disclaimer</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#contributing">Contributing</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

**No Phishing** is an advanced browser extension using artificial intelligence to detect phishing threats with 91% accuracy in real time and provides instant notifications about potential phishing threats. It's very easy to install and operate, providing a seamless browsing experience. It's designed for Google Chrome to enhance online security for both individuals and businesses.

### Disclaimer
This extension is intended as a supplementary tool for online safety. While it demonstrates high accuracy, it is not infallible. As the developer, I am not a certified cybersecurity professional, and the extension could make errors. Users are advised to exercise caution and judgment. By using "No Phishing," you acknowledge and accept responsibility for your online safety.

### Built With

* [![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org)
* [![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white)](https://www.selenium.dev/)
* [![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white)](https://jupyterlab.readthedocs.io/en/stable)
* [![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
* [![Google Chrome](https://img.shields.io/badge/Google_chrome-4285F4?style=for-the-badge&logo=Google-chrome&logoColor=white)](https://www.google.com/chrome/)
* [![VScode](https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)](https://code.visualstudio.com/)
* [![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-A22846?style=for-the-badge&logo=Raspberry%20Pi&logoColor=white)](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

1. Clone the repo
   ```sh
   git clone https://github.com/cprite/phishing-detection-ext.git
   ```
2. Install the required dependencies
   ```sh
   pip install -r requirements.txt
   ```
3. Load the extension in Google Chrome
   - Open Google Chrome and navigate to `chrome://extensions/`.
   - Enable `Developer mode` by toggling the switch in the top-right corner.
   - Click on `Load unpacked` button.
   - Navigate to the directory where you cloned the `phishing-detection-ext` repository and select it.
   - The extension should now appear in your list of installed extensions.
4. Activate the extension
   - Once installed, you'll see the extension's icon in the Chrome toolbar.
   - Click on the icon to turn ON the extension.
   - Before using the extension, start the local server by navigating to the project's root directory in the command line:
     ```sh
     cd path/to/repo/phishing-detection-ext
     python main.py
5. Ready to Go!
   - You are now all set to surf the internet safely with the "No Phishing" extension.
   - The extension will run in the background, monitoring websites you visit for potential phishing threats.
   - Stay safe and feel free to report any suspicious sites or activities you encounter.
   - Remember, your web safety is enhanced, but always stay vigilant while browsing.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

I'm open to collaboration and contributions from fellow developers! You can easily adapt the code to work with other APIs beyond OpenAI. Feel free to fork the project and modify it to suit your needs. Together, we can enhance this tool and help more developers safeguard their projects.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/cprite/save-env.svg?style=for-the-badge
[contributors-url]: https://github.com/cprite/save-env/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/cprite/save-env.svg?style=for-the-badge
[forks-url]: https://github.com/cprite/save-env/network/members
[stars-shield]: https://img.shields.io/github/stars/cprite/save-env.svg?style=for-the-badge
[stars-url]: https://github.com/cprite/save-env/stargazers
[issues-shield]: https://img.shields.io/github/issues/cprite/save-env.svg?style=for-the-badge
[issues-url]: https://github.com/cprite/save-env/issues
[license-shield]: https://img.shields.io/github/license/cprite/save-env.svg?style=for-the-badge
[license-url]: https://github.com/cprite/save-env/blob/master/LICENSE.md
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/niknmirosh
