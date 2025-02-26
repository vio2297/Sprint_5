import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from constants import Constants

class TestConstructor:
    @pytest.fixture
    def driver():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        yield driver
        driver.quit()

    def test_constructor_buns_section(driver):
        driver.get(Constants.URL)
        wait = WebDriverWait(driver, 15)


        buns_section = wait.until(EC.element_to_be_clickable(Locators.BUNS_SECTION))
        buns_section.click()
        buns_section = driver.find_element(Locators.BUNS_SECTION)
        assert buns_section.is_displayed(), "Раздел 'Булки' не найден"

    def test_constructor_sauces_section(driver):
        driver.get(Constants.URL)
        wait = WebDriverWait(driver, 15)

        sauces_section = wait.until(EC.element_to_be_clickable(Locators.SAUCES_SECTION))
        sauces_section = driver.find_element(*Locators.SAUCES_SECTION)
        sauces_section.click()
        sauces_section = driver.find_element(*Locators.SAUCES_SECTION)
        assert sauces_section.is_displayed(), "Раздел 'Соусы' не найден"

    def test_constructor_fillings_section(driver):
        driver.get(Constants.URL)
        wait = WebDriverWait(driver, 15)


        fillings_section = wait.until(EC.element_to_be_clickable(Locators.FILLINGS_SECTION))
        fillings_section = driver.find_element(*Locators.FILLINGS_SECTION)
        fillings_section.click()
        fillings_section = driver.find_element(*Locators.FILLINGS_SECTION)
        assert fillings_section.is_displayed(), "Раздел 'Начинки' не найден"
