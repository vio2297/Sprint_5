import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators
from constants import Constants

@pytest.mark.usefixtures("driver", "login")  # Указываем, что тесты используют фикстуры driver и login
class TestAccNavigation:
    def test_acc_navigation_to_constructor_from_account(self, driver):
        """Проверяет переход в конструктор через кнопку 'Конструктор'"""
        driver.get(Constants.URL_PROFILE)

        constructor_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)
        )
        constructor_button.click()

        WebDriverWait(driver, 10).until(EC.url_to_be(Constants.URL))
        assert driver.current_url == Constants.URL, "Не выполнен переход в конструктор через кнопку 'Конструктор'"

    def test_acc_navigation_to_constructor_from_logo(self, driver):
        """Проверяет переход в конструктор через логотип"""
        driver.get(Constants.URL_PROFILE)

        logo_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGO_BUTTON)
        )
        logo_button.click()

        WebDriverWait(driver, 10).until(EC.url_to_be(Constants.URL))
        assert driver.current_url == Constants.URL, "Не выполнен переход в конструктор через логотип"
