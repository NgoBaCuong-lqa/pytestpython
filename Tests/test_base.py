import pytest
from selenium import webdriver

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass