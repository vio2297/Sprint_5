import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import ConstructorLocators
from constants import Constants

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_constructor_buns_section(driver):
    driver.get(Constants.URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(ConstructorLocators.BUNS_SECTION))
    buns_section = driver.find_element(*ConstructorLocators.BUNS_SECTION)
    buns_section.click()
    buns_section = driver.find_element(*ConstructorLocators.BUNS_SECTION)
    assert buns_section.is_displayed(), "Раздел 'Булки' не найден"

def test_constructor_sauces_section(driver):
    driver.get(Constants.URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(ConstructorLocators.SAUCES_SECTION))
    sauces_section = driver.find_element(*ConstructorLocators.SAUCES_SECTION)
    sauces_section.click()
    sauces_section = driver.find_element(*ConstructorLocators.SAUCES_SECTION)
    assert sauces_section.is_displayed(), "Раздел 'Соусы' не найден"

def test_constructor_fillings_section(driver):
    driver.get(Constants.URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(ConstructorLocators.FILLINGS_SECTION))
    fillings_section = driver.find_element(*ConstructorLocators.FILLINGS_SECTION)
    fillings_section.click()
    fillings_section = driver.find_element(*ConstructorLocators.FILLINGS_SECTION)
    assert fillings_section.is_displayed(), "Раздел 'Начинки' не найден"
