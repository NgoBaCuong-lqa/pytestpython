from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class LoginPage(BasePage):
    # locator
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "pass")
    LOGIN_BUTTON = (By.ID, "u_0_d_dX")
    #constructor of the page class
    def __init__(self,driver):
        super().__init__(driver)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)