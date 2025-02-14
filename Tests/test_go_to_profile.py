import unittest
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from locators import MainPageLocators, RegisterPageLocators, LoginPageLocators
from locators import ProfilePageLocators


class Tests():
    def test_go_to_profile(self, loggined_driver):
        loggined_driver.find_element(*MainPageLocators.PERSONAL_CABINET_LINK).click()
        WebDriverWait(loggined_driver, 10).until(EC.visibility_of_element_located(ProfilePageLocators.LOGOUT_BUTTON))
        logout_button = loggined_driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON)
        assert logout_button.is_displayed()