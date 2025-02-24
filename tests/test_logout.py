import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthorizationLocators, AccountPageLocators
from constants import Constants


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    driver.get(Constants.URL_LOGIN)

    # Ожидание загрузки страницы
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((AuthorizationLocators.EMAIL_INPUT)))

    if len(driver.find_elements(*AuthorizationLocators.EMAIL_INPUT)) == 0:
        raise Exception("Элемент EMAIL_INPUT не найден! Проверь XPATH в AuthorizationLocators")

    driver.find_element(*AuthorizationLocators.EMAIL_INPUT).send_keys(Constants.EMAIL)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((AuthorizationLocators.PASSWORD_INPUT)))
    driver.find_element(*AuthorizationLocators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AuthorizationLocators.LOGI_BUTTON)))
    driver.find_element(*AuthorizationLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.url_changes(Constants.URL_LOGIN))


def test_logout(driver, login):
    driver.get(Constants.URL_PROFILE)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AccountPageLocators.LOGOUT_BUTTON)))
    driver.find_element(*AccountPageLocators.LOGOUT_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.url_to_be(Constants.URL_LOGIN))

    assert driver.current_url == Constants.URL_LOGIN, "Не выполнен выход из аккаунта"
