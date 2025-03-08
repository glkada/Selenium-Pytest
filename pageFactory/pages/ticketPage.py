from selenium.webdriver.common.by import By
from pageFactory.objects.ticketObject import TicketPageObject
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.apiHelpers import ApiHelper
import json

class TicketPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = 1
        self.ticketPageObjects = TicketPageObject()

    def open_ticket_creation_tab(self) -> None:
        element = WebDriverWait(self.driver, self.wait).until(
        EC.presence_of_element_located((By.XPATH, self.ticketPageObjects.create_ticket_btn)))
        element.click()
        self.driver.implicitly_wait(self.wait)

    def create_ticket(self, title: str, description: str) -> None:
        """
        This method creates ticket on the platform.
        :param title:
        :param description:
        """
        self.driver.find_element(By.XPATH, self.ticketPageObjects.ticket_title).send_keys(title)
        self.driver.find_element(By.XPATH, self.ticketPageObjects.ticket_description).send_keys(description)
        self.driver.find_element(By.XPATH, self.ticketPageObjects.ticket_submit_btn).click()
        self.driver.implicitly_wait(self.wait)

    def verify_ticket(self, title: str) -> None:
        """
        This method checks if the created ticket is present in the api resopnse.
        :param title:
        :return:
        """
        apiHelper = ApiHelper()
        res = apiHelper.reqeust("GET", "/api/tickets/user/1")
        res = json.loads(res)
        for value in res:
            if value['title'] == title:
                return value['title']
        return None
        