from selenium import webdriver
import chromedriver_autoinstaller
class TestData:

    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    BASE_URL = "https://www.facebook.com/"
    USER_NAME = "0326839977"
    PASSWOD = "adidaslovenike"

