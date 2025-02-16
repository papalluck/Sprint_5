from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import ConstructorPageLocators,MainPageLocators,LoginPageLocators,RegisterPageLocators
from conftest import driver
from data import Data


class TestLogInToYourAccount:

    def test_login_from_main_page(self, driver):
     driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
     email_input = driver.find_element(*LoginPageLocators.EMAIL_INPUT)
     email_input.send_keys(Data.email)

     password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
     password_input.send_keys(Data.password)

     enter_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
     enter_button.click()

     WebDriverWait(driver, 10).until(
         EC.visibility_of_element_located(ConstructorPageLocators.CHECKOUT_BUTTON))

     assert driver.find_element(*ConstructorPageLocators.CHECKOUT_BUTTON).is_displayed()

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


      assert driver.find_element(*ConstructorPageLocators.CHECKOUT_BUTTON).is_displayed()

    def test_login_from_register_form(self, driver):
       driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
       driver.find_element(*MainPageLocators.REGISTER_LINK).click()
       driver.find_element(*RegisterPageLocators.LOGIN_BUTTON_FROM_REGISTER_FORM).click()

       email_input = driver.find_element(*LoginPageLocators.EMAIL_INPUT)
       email_input.send_keys(Data.email)

       password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
       password_input.send_keys(Data.password)

       enter_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
       enter_button.click()

       WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(ConstructorPageLocators.CHECKOUT_BUTTON))

       assert driver.find_element(*ConstructorPageLocators.CHECKOUT_BUTTON).is_displayed()

    def test_login_from_reset_password_form(self, driver):
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*LoginPageLocators.RESET_PASSWORD_LINK).click()
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON_FROM_RECOVERY_FORM).click()

        email_input = driver.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(Data.email)

        password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(Data.password)

        enter_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        enter_button.click()

        WebDriverWait(driver, 10).until(
         EC.visibility_of_element_located(ConstructorPageLocators.CHECKOUT_BUTTON))

        assert driver.find_element(*ConstructorPageLocators.CHECKOUT_BUTTON).is_displayed()