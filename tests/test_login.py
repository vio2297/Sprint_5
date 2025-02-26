import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from constants import Constants


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


class TestUserLogin:

    def login(self, driver):

        wait = WebDriverWait(driver, 15)

        email_input = wait.until(EC.presence_of_element_located(Locators.EMAIL_INPUT))
        email_input.send_keys(Constants.EMAIL)

        password_input = wait.until(EC.presence_of_element_located(Locators.PASSWORD_INPUT))
        password_input.send_keys(Constants.PASSWORD)

        login_button = wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON))
        login_button.click()

        wait.until(EC.element_to_be_clickable(Locators.MAKE_ORDER_BUTTON))

    def test_login_account_button(self, driver):
        driver.get(Constants.URL_LOGIN)
        wait = WebDriverWait(driver, 15)

        account_button = wait.until(EC.element_to_be_clickable(Locators.LOGIN_INTO_ACCOUNT_BUTTON))
        account_button.click()

        wait.until(EC.url_to_be(Constants.URL_LOGIN))

        self.login(driver)

    def test_login_account_button_in_header(self, driver):
        driver.get(Constants.URL_LOGIN)
        wait = WebDriverWait(driver, 15)

        account_button = wait.until(EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON))
        account_button.click()

        wait.until(EC.url_to_be(Constants.URL_LOGIN))

        self.login(driver)

    def test_login_registration_form(self, driver):
        driver.get(Constants.URL_LOGIN)
        wait = WebDriverWait(driver, 15)

        login_text_link = wait.until(EC.element_to_be_clickable(Locators.LOGIN_TEXT_LINK))
        login_text_link.click()

        wait.until(EC.url_to_be(Constants.URL_LOGIN))

        self.login(driver)

    def test_login_register_forgot_password(self, driver):
        driver.get(Constants.URL_LOGIN)
        wait = WebDriverWait(driver, 15)

        login_text_link = wait.until(EC.element_to_be_clickable(Locators.LOGIN_TEXT_LINK))
        login_text_link.click()

        wait.until(EC.url_to_be(Constants.URL_LOGIN))

        self.login(driver)
