import unittest
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from locators import MainPageLocators, RegisterPageLocators, LoginPageLocators
from locators import ProfilePageLocators


class Test_profile_log_out:
    def test_logout(self, loggined_driver):
        loggined_driver.find_element(*MainPageLocators.PERSONAL_CABINET_LINK).click()
        WebDriverWait(loggined_driver, 10).until(
            EC.visibility_of_element_located((ProfilePageLocators.LOGOUT_BUTTON))
        )
        loggined_driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()
        WebDriverWait(loggined_driver, 10).until(
            EC.visibility_of_element_located((LoginPageLocators.LOGIN_BUTTON))
        )
        login_button = loggined_driver.find_element(*LoginPageLocators.LOGIN_BUTTON)

        assert login_button.is_displayed()