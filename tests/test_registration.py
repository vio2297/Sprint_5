import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from locators import Locators
from constants import Constants
from faker import Faker  # Правильный импорт библиотеки Faker

fake = Faker()  # Создаём объект Faker для генерации данных


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


class TestRegistrationAcc:

    def test_successful_registration(self, driver):
        driver.get(Constants.URL_REG)  # Используем страницу регистрации
        wait = WebDriverWait(driver, 15)

        # Генерируем новые данные
        name = fake.first_name()
        email = fake.email()
        password = "StrongPass123!"  # Пример валидного пароля

        # Ввод данных в поля формы
        name_input = wait.until(EC.presence_of_element_located(Locators.NAME_INPUT))
        name_input.send_keys(name)

        email_input = wait.until(EC.presence_of_element_located(Locators.EMAIL_INPUT))
        email_input.send_keys(email)

        password_input = wait.until(EC.presence_of_element_located(Locators.PASSWORD_INPUT))
        password_input.send_keys(password)

        # Нажимаем "Зарегистрироваться"
        registration_button = wait.until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON))
        registration_button.click()

        # Ожидаем появления кнопки "Войти"
        login_button = wait.until(EC.presence_of_element_located(Locators.LOGIN_BUTTON))
        assert login_button.is_displayed(), "Кнопка 'Войти' не появилась после регистрации"

    def test_register_with_invalid_password(self, driver):
        driver.get(Constants.URL_REG)  # Используем страницу регистрации
        wait = WebDriverWait(driver, 15)

        # Генерируем новые данные
        name = fake.first_name()
        email = fake.email()
        invalid_password = "123"  # Пример некорректного пароля (слишком короткий)

        # Ввод данных
        name_input = wait.until(EC.presence_of_element_located(Locators.NAME_INPUT))
        name_input.send_keys(name)

        email_input = wait.until(EC.presence_of_element_located(Locators.EMAIL_INPUT))
        email_input.send_keys(email)

        password_input = wait.until(EC.presence_of_element_located(Locators.PASSWORD_INPUT))
        password_input.send_keys(invalid_password)

        # Нажимаем "Зарегистрироваться"
        registration_button = wait.until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON))
        registration_button.click()

        # Ожидаем сообщение об ошибке
        password_error_message = wait.until(EC.presence_of_element_located(Locators.ERROR_MESSAGE_PASSWORD))
        assert password_error_message.is_displayed(), "Ошибка пароля не появилась при регистрации с некорректным паролем"
