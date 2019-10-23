from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


class Home:
    def __init__(self, driver):
        self.driver = driver
        try:
            self.btnLoginDropDown = driver.find_element(By.ID, "ta-login-dropdown--not-logged")
        except NoSuchElementException:
            pass
            #It does not work
            #self.btnLoginDropDown = driver.find_element(By.XPATH, "//button[contains(@class,'LoginDropdownButton') "
            #                                                      "and descendant::span[contains(text(),'LOGIN')]]")

    def open_login_small_window(self):
        self.btnLoginDropDown.click()

    def open_basket(self):
        time.sleep(2)
        #self.btnBasketButton = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.ID, "ta-mini-basket__open")))
        self.btnBasketButton = self.driver.find_element(By.ID, "ta-mini-basket__open")
        self.btnBasketButton.click()
