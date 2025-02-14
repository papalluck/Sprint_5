import unittest
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from locators import MainPageLocators, RegisterPageLocators, LoginPageLocators, ConstructorPageLocators
from locators import ProfilePageLocators

class TestLoginFromProfile():
    def test_login_from_profile(self, driver):
        driver.find_element(*MainPageLocators.PERSONAL_CABINET_LINK).click()

        email_input = driver.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(Data.email)

        password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(Data.password)

        enter_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        enter_button.click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorPageLocators.CHECKOUT_BUTTON))
        checkout_button = driver.find_element(*ConstructorPageLocators.CHECKOUT_BUTTON)

        assert checkout_button.is_displayed()