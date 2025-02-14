import unittest
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from locators import MainPageLocators, RegisterPageLocators, LoginPageLocators, ConstructorPageLocators
from locators import ProfilePageLocators


class TestBunClick():
    def test_click_bun(self, loggined_driver):
        loggined_driver.find_element(*ConstructorPageLocators.SAUCES_TAB).click()
        loggined_driver.find_element(*ConstructorPageLocators.BUNS_TAB).click()
        WebDriverWait(loggined_driver, 10).until(
            EC.visibility_of_element_located(ConstructorPageLocators.CURRENT_TAB))
        text = loggined_driver.find_element(*ConstructorPageLocators.CURRENT_TAB).text
        assert "Булки" in text
