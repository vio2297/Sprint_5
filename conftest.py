import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # Для нажатия Enter
from locators import LoginPageLocators, MainPageLocators, AccountPageLocators
from constants import Constants  # Импортируем константы

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)  # Ожидание перед каждым поиском элемента
    yield driver
    driver.quit()

@pytest.fixture
def login_user(browser):
    browser.get(Constants.URL_LOGIN)  # Открываем страницу авторизации
    browser.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(Constants.EMAIL)  # Вводим email
    browser.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(Constants.PASSWORD, Keys.RETURN)  # Вводим пароль и жмём Enter

@pytest.fixture
def open_main_page(browser):
    browser.get(Constants.URL)  # Открываем главную страницу