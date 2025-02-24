import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthorizationLocators, MainPageLocators, RegistrationLocators
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

def test_login_via_main_page_button(driver, login):
    driver.get(Constants.URL)
    driver.find_element(*MainPageLocators.ACCOUNT_BUTTON).click()
    assert driver.current_url == Constants.URL_PROFILE, "Не выполнен переход в личный кабинет"

def test_login_via_registration_form(driver, login):
    driver.get(Constants.URL_REG)
    driver.find_element(*RegistrationLocators.LOGIN_LINK).click()
    assert driver.current_url == Constants.URL_PROFILE, "Не выполнен вход через форму регистрации"

def test_login_via_password_recovery(driver, login):
    driver.get(Constants.URL_LOGIN)
    driver.find_element(*AuthorizationLocators.RECOVER_PASSWORD_LINK).click()
    driver.find_element(*AuthorizationLocators.EMAIL_INPUT).send_keys(Constants.EMAIL)
    driver.find_element(*AuthorizationLocators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)
    driver.find_element(*AuthorizationLocators.LOGIN_BUTTON).click()
    assert driver.current_url == Constants.URL_PROFILE, "Не выполнен вход через восстановление пароля"
