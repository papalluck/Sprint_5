import unittest
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from locators import MainPageLocators, RegisterPageLocators, LoginPageLocators
import pytest

class Test_registration:
    def test_successful_registration(self, driver):

        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()


        driver.find_element(*MainPageLocators.REGISTER_LINK).click()


        name = "Владислав"
        email = f"VladislavZhurov15{random.randint(100, 999)}@yandex.ru"

        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(
            Data.password)


        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()


        WebDriverWait(driver, Data.Wait_time).until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))

        login_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)


        assert login_button.is_displayed()
