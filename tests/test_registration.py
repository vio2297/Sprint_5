import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from locators import RegistrationLocators
from constants import Constants

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


# Проверка успешной регистрации
def test_successful_registration(driver):
    driver.get(Constants.URL_REG)

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(RegistrationLocators.REGISTER_BUTTON))
    driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys(Constants.NAME)
    driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(Constants.EMAIL)
    driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(Constants.PASSWORD)
    driver.find_element(*RegistrationLocators.REGISTER_BUTTON).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(RegistrationLocators.REGISTER_BUTTON))

# Проверка не успешной регистрацией с коротким паролем
def test_registration_with_short_password(driver):
    driver.get(Constants.URL_REG)

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(RegistrationLocators.REGISTER_BUTTON))
    driver.find_element(*RegistrationLocators.NAME_INPUT).send_keys(Constants.NAME)
    driver.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(Constants.EMAIL)
    driver.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys("12345")
    driver.find_element(*RegistrationLocators.REGISTER_BUTTON).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(RegistrationLocators.REGISTER_BUTTON))


# Проверка текста ошибки для некорректного пароля
    error_message = driver.find_element(*RegistrationLocators.ERROR_MESSAGE_PASSWORD).text
    assert error_message == "Некорректный пароль", "Нет сообщения об ошибке для короткого пароля"


