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


class TestUserLogout:

    def test_logout_from_account(self, driver):
        driver.get(Constants.URL_LOGIN)
        wait = WebDriverWait(driver, 15)

        # Вход в аккаунт
        email_input = wait.until(EC.presence_of_element_located(Locators.EMAIL_INPUT))
        email_input.send_keys(Constants.EMAIL)

        password_input = wait.until(EC.presence_of_element_located(Locators.PASSWORD_INPUT))
        password_input.send_keys(Constants.PASSWORD)

        login_button = wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON))
        login_button.click()

        # Ожидаем редиректа в профиль
        wait.until(EC.url_to_be(Constants.URL_PROFILE))

        # Переход в личный кабинет
        account_button = wait.until(EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON))
        account_button.click()

        # Выход из аккаунта
        logout_button = wait.until(EC.element_to_be_clickable(Locators.LOGOUT_BUTTON))
        logout_button.click()

        # Проверка редиректа на страницу авторизации
        wait.until(EC.url_to_be(Constants.URL_LOGIN))
        assert driver.current_url == Constants.URL_LOGIN, "Выход из аккаунта не выполнен"
