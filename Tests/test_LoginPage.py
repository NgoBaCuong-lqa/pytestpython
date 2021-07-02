import pytest

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Pages.BasePage import BasePage

@pytest.mark.usefixtures('init_driver')

class Test_Login(BasePage):
    LOGIN_BUTTON = (By.ID, "u_0_d_dX")
    # def test_login_page_title(self):
    #     self.driver.get('https://www.google.com/')
    #     loginPage = LoginPage(self.driver)
    #     title = loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
    #     assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.driver.get('https://vi-vn.facebook.com/')
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.do_click(self.LOGIN_BUTTON)
