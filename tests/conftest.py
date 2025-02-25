import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthorizationLocators, MainPageLocators
from constants import Constants

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)  # Ожидание перед каждым поиском элемента
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):

    driver.get(Constants.URL_LOGIN)
    driver.find_element(*AuthorizationLocators.EMAIL_INPUT).send_keys(Constants.EMAIL)
    driver.find_element(*AuthorizationLocators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)
    driver.find_element(*AuthorizationLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 5).until(EC.url_changes(Constants.URL_PROFILE))


@pytest.fixture
def open_main_page(browser):
    browser.get(Constants.URL)  # Открываем главную страницу