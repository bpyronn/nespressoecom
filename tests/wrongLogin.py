import json
import pytest
from pages.homepage import Home
from pages.login import Login
from setup.conftest import set_up


@pytest.mark.usefixtures("set_up")
class TestWrongLogin:
    def test_valid_wrong_login(self, set_up):
        with open('./data/credentials.json', 'r') as json_data:
            for i in json.load(json_data):
                self.username = i['username']
                self.password = i['wrongPassword']
        home = Home(set_up)
        home.open_login_small_window()
        login = Login(set_up)
        login.enter_credentials(self.username, self.password)
        login.check_wrong_login()
