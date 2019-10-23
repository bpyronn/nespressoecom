import json
import pytest
from pages.mainMenu import NavigationMenu
from pages.orderCapsules import OrderCapsules
from setup.conftest import set_up


@pytest.mark.usefixtures("set_up")
class TestOrderCapsules:
    def test_order_capsules(self, set_up):
        menu = NavigationMenu(set_up, 'Coffee')
        menu.select_menu()
        capsule = OrderCapsules(set_up)
        capsule.add_to_bag_and_select_50('Kazaare')
