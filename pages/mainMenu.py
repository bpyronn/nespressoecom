from selenium.webdriver.common.by import By


class NavigationMenu:
    def __init__(self, driver, menu):
        self.driver = driver
        self.menu = driver.find_element(By.XPATH,
                                            "//div[contains(@class, 'HeaderNavigationBarItem__title') and contains(text(), '"+menu+"')]")

    def select_menu(self):
        self.menu.click()
