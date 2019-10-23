import json
import time
import pytest
from pages.mainMenu import NavigationMenu
from pages.orderCapsules import OrderCapsules
from pages.homepage import Home
from pages.basket import Basket
from setup.conftest import set_up


@pytest.mark.usefixtures("set_up")
class TestOrderCapsules:
    def test_order_capsules(self, set_up):
        menu = NavigationMenu(set_up, 'Coffee')
        menu.select_menu()
        capsule = OrderCapsules(set_up)
        capsule.add_to_bag_and_select_50('Kazaar')
        home = Home(set_up)
        home.open_basket()
        basket = Basket(set_up)
        basket.check_capsules_ordered('kazaar')
        basket.check_total_price('28.50')
        basket.go_to_shopping_bag()
        time.sleep(5)
