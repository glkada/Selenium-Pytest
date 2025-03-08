from pytest_bdd import scenarios, given, when, then
from pageFactory.pages.basePage import BasePage
from settings import Settings
import faker
import os

settings = Settings()
f = faker.Faker()
os.environ['PLAYWRIGHT_EXP_APP_USERNAME'] = f.email()
scenarios('../features/login.feature')


@given("I open the registration page")
def open_auth_page(driver):
    entry_page = BasePage(driver)
    entry_page.open_url(settings.HOST)

@when("I register with credentials")
def registration(driver):
    entry_page = BasePage(driver)
    entry_page.register(os.getenv('PLAYWRIGHT_EXP_APP_USERNAME'), settings.HOST_PASSWORD)    

@then("I should be able to login successfully from the login page")
def login(driver):
    entry_page = BasePage(driver)
    response_message = entry_page.login(os.getenv('PLAYWRIGHT_EXP_APP_USERNAME'), settings.HOST_PASSWORD)
    assert response_message.split('>')[1] == 'Login successful! '