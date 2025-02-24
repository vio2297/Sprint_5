import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AccountPageLocators, AuthorizationLocators
from constants import Constants

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    driver.get(Constants.URL_LOGIN)
    driver.find_element(*AuthorizationLocators.EMAIL_INPUT).send_keys(Constants.EMAIL)
    driver.find_element(*AuthorizationLocators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)
    driver.find_element(*AuthorizationLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.url_changes(Constants.URL_LOGIN))

def test_navigation_to_constructor_from_account(driver, login):
    driver.get(Constants.URL_PROFILE)
    driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
    assert driver.current_url == Constants.URL, "Не выполнен переход в конструктор через кнопку 'Конструктор'"

def test_navigation_to_constructor_from_logo(driver, login):
    driver.get(Constants.URL_PROFILE)
    driver.find_element(*MainPageLocators.LOGO_BUTTON).click()
    assert driver.current_url == Constants.URL, "Не выполнен переход в конструктор через логотип"
