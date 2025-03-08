import pytest
from selenium import webdriver
from pageFactory.pages.basePage import BasePage
from settings import Settings

settings = Settings()

@pytest.fixture()
def driver():
    # Instantiate the WebDriver, for example using Chrome:
    driver = webdriver.Chrome()
    yield driver
    # Teardown: quit the driver
    driver.quit()