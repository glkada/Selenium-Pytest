from pytest_bdd import scenarios, given, when, then, parsers
from pageFactory.pages.basePage import BasePage
from pageFactory.pages.ticketPage import TicketPage
from settings import Settings
import os

settings = Settings()
scenarios('../features/ticketCreation.feature')


@given("I log in to the platform with valid credentials")
def open_auth_page(driver):
    entry_page = BasePage(driver)
    entry_page.open_url(settings.HOST)
    response_message = entry_page.login(os.environ['PLAYWRIGHT_EXP_APP_USERNAME'], settings.HOST_PASSWORD)
    assert response_message.split('>')[1] == 'Login successful! '

@when("I navigate to the ticket creation tab")
def registration(driver):
    ticket_page = TicketPage(driver)
    ticket_page.open_ticket_creation_tab()
    
@when(parsers.parse('I enter {title} in the title field and {description} in the description field, then submit the form'))
def createTicket(driver, title, description):
    ticket_page = TicketPage(driver)
    ticket_page.create_ticket(title, description)

@then(parsers.parse('I should be able to see a ticket with the title: {title}'))
def verifyTicket(driver, title):
    '''
    We're doing API validation here since the UI does not support rendering of 10+ tickets
    '''
    ticket_page = TicketPage(driver)
    response_message = ticket_page.verify_ticket(title)
    assert response_message == title
    
