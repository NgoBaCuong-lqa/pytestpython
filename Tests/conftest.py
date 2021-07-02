import pytest
from selenium import webdriver


from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    global webdriver
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
        # print(web_driver)
        request.cls.driver = web_driver
        yield web_driver
        web_driver.close()



