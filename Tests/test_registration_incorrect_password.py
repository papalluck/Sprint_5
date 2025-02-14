import unittest
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from locators import MainPageLocators, RegisterPageLocators, LoginPageLocators

class  Testregistration:
    def test_registration_incorrect_password(self, driver):
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

        driver.find_element(*MainPageLocators.REGISTER_LINK).click()
        name = "TestUser"
        email = f"VladislavZhurov15{random.randint(100, 999)}@yandex.ru"
        password = f"{random.randint(1, 99999)}"

        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)

        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()


        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegisterPageLocators.ERROR_MESSAGE)
        )

        message_error = driver.find_element(*RegisterPageLocators.ERROR_MESSAGE)

        assert message_error.is_displayed()