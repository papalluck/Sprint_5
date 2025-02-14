import unittest
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from locators import MainPageLocators, RegisterPageLocators, LoginPageLocators, ConstructorPageLocators
from locators import ProfilePageLocators


class TestFillingClick():
    def test_click_filling(self, loggined_driver):
            loggined_driver.find_element(*ConstructorPageLocators.FILLINGS_TAB).click()
            WebDriverWait(loggined_driver, 10).until(
                EC.visibility_of_element_located(ConstructorPageLocators.CURRENT_TAB))
            text = loggined_driver.find_element(*ConstructorPageLocators.CURRENT_TAB).text
            assert "Начинки" in text