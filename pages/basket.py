from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class Basket:
    def __init__(self, driver):
        self.driver = driver

    def check_capsules_ordered(self, name_capsule):
        assert self.driver.find_element(By.XPATH, "//th[contains(@id, '" + name_capsule + "')]"), \
            name_capsule + " is not in the basket"

    def check_total_price(self, total_price):
        assert self.driver.find_element(By.XPATH, "//td[contains(@class, 'MiniBasketTotalTable__totalPrice-value') "
                                                  "and contains(text(), '" + total_price + "')]"), "Total price not correct"

    def go_to_shopping_bag(self):
        self.driver.find_element(By.ID, "ta-mini-basket__checkout").click()
