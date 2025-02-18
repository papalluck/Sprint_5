import pytest
from selenium import webdriver
from data import Data
from locators import MainPageLocators, RegisterPageLocators, LoginPageLocators, ProfilePageLocators, \
    ConstructorPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(Data.BURGER_URL)

    yield chrome_driver

    chrome_driver.quit()

@pytest.fixture(scope='function')
def loggined_driver(driver):
    login_button = driver.find_element(*MainPageLocators.LOGIN_BUTTON)
    login_button.click()

    email_input = driver.find_element(*LoginPageLocators.EMAIL_INPUT)
    email_input.send_keys(Data.email)

    password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
    password_input.send_keys(Data.password)

    enter_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
    enter_button.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(ConstructorPageLocators.CHECKOUT_BUTTON))
    checkout_button = driver.find_element(*ConstructorPageLocators.CHECKOUT_BUTTON)

    yield driver
