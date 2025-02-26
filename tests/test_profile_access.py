import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from constants import Constants

class TestProfileAccess:
    @pytest.fixture
    def driver():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        yield driver
        driver.quit()


    def test_navigate_to_profile_page(self, driver):
        driver.get(Constants.URL_LOGIN)
        wait = WebDriverWait(driver, 15)

        # Вводим email
        email_input = wait.until(EC.presence_of_element_located(Locators.EMAIL_INPUT))
        email_input.send_keys(Constants.EMAIL)

        # Вводим пароль
        password_input = wait.until(EC.presence_of_element_located(Locators.PASSWORD_INPUT))
        password_input.send_keys(Constants.PASSWORD)

        # Нажимаем кнопку "Войти"
        login_button = wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON))
        login_button.click()

        # Ждём перехода на главную страницу
        wait.until(EC.url_to_be(Constants.URL))

        # Переходим в личный кабинет
        account_button = wait.until(EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON))
        account_button.click()

        # Проверяем, что мы попали в профиль
        wait.until(EC.url_to_be(Constants.URL_PROFILE))
        assert "account/profile" in driver.current_url, "Не удалось перейти в профиль"

        # Проверяем, что есть кнопка "Выход"
        logout_button = wait.until(EC.presence_of_element_located(Locators.LOGOUT_BUTTON))
        assert logout_button.is_displayed(), "Кнопка выхода не найдена"
