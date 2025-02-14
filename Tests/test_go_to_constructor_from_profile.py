from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import unittest
import unittest
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from locators import MainPageLocators, RegisterPageLocators, LoginPageLocators, ConstructorPageLocators
from locators import ProfilePageLocators

class TestFromProfileLogoToConstructor():
    def test_go_to_constructor_from_profile(self,loggined_driver):
        loggined_driver.find_element(*MainPageLocators.PERSONAL_CABINET_LINK).click()
        WebDriverWait(loggined_driver, 20).until(EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON))
        loggined_driver.find_element(*MainPageLocators.CONSTRUCTOR_LINK).click()
        WebDriverWait(loggined_driver, 20).until(EC.visibility_of_element_located(ConstructorPageLocators.CURRENT_TAB))
        current_tab = loggined_driver.find_element(*ConstructorPageLocators.CURRENT_TAB)
        assert current_tab.is_displayed()