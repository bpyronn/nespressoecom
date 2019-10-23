import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def set_up():
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--no-sandbox")
    pathToChrome = '/Users/bpyronn/Downloads/chromedriver'
    driver = webdriver.Chrome(executable_path=pathToChrome, chrome_options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.nespresso.com/ch/en/home")
    yield driver
    driver.close()
    driver.quit()
