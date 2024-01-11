from selenium import webdriver
from webdriver_manager import chrome
import pytest


@pytest.fixture()
def setup(request):
    global browser
    browser = "chrome"
    app_url = 'https://www.flightradar24.com/data/airports/pnq.'
    web_driver = webdriver.Chrome(options=webdriver.ChromeOptions())

    request.cls.driver = web_driver
    web_driver.get(app_url)
    web_driver.maximize_window()
    return web_driver
