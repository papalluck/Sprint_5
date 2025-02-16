from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import ConstructorPageLocators
from conftest import loggined_driver



class TestSelectingSection():
    def test_click_bun(self, loggined_driver):
        loggined_driver.find_element(*ConstructorPageLocators.SAUCES_TAB).click()
        loggined_driver.find_element(*ConstructorPageLocators.BUNS_TAB).click()
        WebDriverWait(loggined_driver, 10).until(
            EC.visibility_of_element_located(ConstructorPageLocators.CURRENT_TAB))

        assert "Булки" in loggined_driver.find_element(*ConstructorPageLocators.CURRENT_TAB).text

    def test_click_filling(self, loggined_driver):
        loggined_driver.find_element(*ConstructorPageLocators.FILLINGS_TAB).click()
        WebDriverWait(loggined_driver, 10).until(
            EC.visibility_of_element_located(ConstructorPageLocators.CURRENT_TAB))

        assert "Начинки" in loggined_driver.find_element(*ConstructorPageLocators.CURRENT_TAB).text


    def test_click_sauce(self, loggined_driver):
            loggined_driver.find_element(*ConstructorPageLocators.SAUCES_TAB).click()
            WebDriverWait(loggined_driver, 10).until(
                EC.visibility_of_element_located(ConstructorPageLocators.CURRENT_TAB))

            assert "Соусы" in loggined_driver.find_element(*ConstructorPageLocators.CURRENT_TAB).text
