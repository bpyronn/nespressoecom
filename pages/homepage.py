from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


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
