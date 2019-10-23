from selenium.webdriver.common.by import By


class OrderCapsules:
    def __init__(self, driver):
        self.driver = driver

    def add_to_bag_and_select_50(self, name_capsule):
        self.add_to_bag = self.driver.find_element(By.XPATH,
                                            "//button[contains(@class,'AddToBag') "
                                            "and ancestor::article[contains(@class,'ProductListElement') "
                                            "and descendant::*[contains(text(),'" + name_capsule + "')]]]")
        self.add_to_bag.click()
        self.qty = self.driver.find_element(By.ID, 'ta-quantity-selector__predefined-5')
        self.qty.click()
