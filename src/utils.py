import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def init_driver(headless: bool = True) -> webdriver.Chrome:
    """Initialize a Chrome WebDriver instance.

    Parameters
    ----------
    headless: bool
        Whether to run Chrome in headless mode.
    """
    print("Inicializando WebDriver...")
    options = Options()
    if headless:
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    driver.implicitly_wait(10)
    logging.getLogger("selenium").setLevel(logging.WARNING)
    print("WebDriver pronto.")
    return driver
