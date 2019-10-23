from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.username = driver.find_element(By.ID, "ta-header-username")
        self.password = driver.find_element(By.ID, "ta-header-password")
        self.rememberMe = driver.find_element(By.ID, "ta-header-remember-me")
        self.btnSubmit = driver.find_element(By.ID, "ta-login-form__submit")

    def enter_credentials(self, username, password):
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.rememberMe.click()
        self.btnSubmit.click()

    def check_wrong_login(self):
        self.loginErrMsg = self.driver.find_element(By.ID, "email-error-message")
        assert self.loginErrMsg, "Error message was not displayed"

    def check_right_login(self):
        self.logged = self.driver.find_element(By.ID, "ta-login-dropdown--logged")
        assert self.logged, "Not properly logged"
