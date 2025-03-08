from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageFactory.objects.authPageObject import AuthPage
from time import sleep

class BasePage:
    """Base class for all driver objects."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = 1
        self.authPageObjects = AuthPage()

    def open_url(self, url: str):
        """
        This method resolves the page
        :param url:
        """
        self.driver.get(url)
        self.driver.implicitly_wait(self.wait)

    def register(self, username: str, password: str) -> None:
        """
        This method performs registration to platform.
        :param username:
        :param password:
        """
        self.driver.find_element(By.XPATH, self.authPageObjects.register).click()
        self.driver.implicitly_wait(self.wait)
        self.driver.find_element(By.XPATH, self.authPageObjects.username).send_keys(username)
        self.driver.find_element(By.XPATH, self.authPageObjects.password).send_keys(password)
        self.driver.find_element(By.XPATH, self.authPageObjects.submit_registration_creds).click()
        self.driver.implicitly_wait(self.wait)
        sleep(self.wait * 2)    # waiting for the backend services to create an account before attempting further actions. 

    def login(self, username: str, password: str) -> None:
        """
        This method performs login to platform.
        :param username:
        :param password:
        :return:
        """
        self.driver.find_element(By.XPATH, self.authPageObjects.home_btn).click()
        self.driver.implicitly_wait(self.wait)
        self.driver.find_element(By.XPATH, self.authPageObjects.login).click()
        self.driver.implicitly_wait(self.wait)
        self.driver.find_element(By.XPATH, self.authPageObjects.username).send_keys(username)
        self.driver.find_element(By.XPATH, self.authPageObjects.password).send_keys(password)
        self.driver.find_element(By.XPATH, self.authPageObjects.submit_login_creds).click()
        login_status = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, self.authPageObjects.login_status_snackbar)))
        return login_status.get_attribute('innerHTML')