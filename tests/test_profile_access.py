import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators
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
    driver.find_element(*MainPageLocators.EMAIL_INPUT).send_keys(Constants.EMAIL)
    driver.find_element(*MainPageLocators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)
    driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.url_changes(Constants.URL_LOGIN))

def test_go_to_profile(driver, login):
    driver.get(Constants.URL)
    driver.find_element(*MainPageLocators.ACCOUNT_BUTTON).click()
    assert driver.current_url == Constants.URL_PROFILE, "Не выполнен переход в личный кабинет"
