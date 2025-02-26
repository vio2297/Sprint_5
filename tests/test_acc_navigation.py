import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from constants import Constants

class TestAccNavigation:

    @pytest.fixture
    def driver():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        yield driver
        driver.quit()

    def test_acc_navigation_to_constructor_from_account(self, driver):
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

        # Переход в личный кабинет
        account_button = wait.until(EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON))
        account_button.click()
        wait.until(EC.url_to_be(Constants.URL_PROFILE))

        # Кликаем на "Конструктор"
        constructor_button = wait.until(EC.element_to_be_clickable(Locators.CONSTRUCTOR_BUTTON))
        constructor_button.click()

        # Проверяем, что находимся на главной странице
        wait.until(EC.url_to_be(Constants.URL))
        constructor_header = wait.until(EC.presence_of_element_located(Locators.CONSTRUCTOR_HEADER))
        assert constructor_header.is_displayed()

    def test_acc_navigation_to_constructor_from_logo(self, driver):
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

        # Переход в личный кабинет
        account_button = wait.until(EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON))
        account_button.click()
        wait.until(EC.url_to_be(Constants.URL_PROFILE))

        # Кликаем на логотип
        logo_button = wait.until(EC.element_to_be_clickable(Locators.SERVICE_LOGO_BUTTON))
        logo_button.click()

        # Проверяем, что находимся на главной странице
        wait.until(EC.url_to_be(Constants.URL))
        constructor_header = wait.until(EC.presence_of_element_located(Locators.CONSTRUCTOR_HEADER))
        assert constructor_header.is_displayed()
