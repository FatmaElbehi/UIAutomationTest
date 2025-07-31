from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resources.LoginPageLocators import LoginPageLocators
import yaml
import logging
import os
from selenium.common.exceptions import NoSuchElementException
import time


log_path = os.path.join('logs', 'app.log')
logging.basicConfig(filename=log_path, level=logging.INFO, filemode='a', format='%(asctime)s - %(levelname)s : %(message)s')
# Add a separate handler for ERROR level messages
error_handler = logging.FileHandler(log_path)
error_handler.setLevel(logging.ERROR)
error_formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
error_handler.setFormatter(error_formatter)

# Attach the error handler to the root logger
logging.getLogger().addHandler(error_handler)

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def visit(self):
        with open('config/driver.yml') as file:
         config = yaml.safe_load(file)
         test_system_url = config.get("TEST_SYSTEM_URL", "")
        self.driver.get(test_system_url)
        self.logger.info("Login page Visited")
        #time.sleep(5)  # Add a delay of 1 second after visiting the page

    def enter_username(self, username):
        try:
            username_field = self.driver.find_element(*LoginPageLocators.USERNAME_INPUT)
            username_field.clear()
            
            if username is not None and username != "":
                username_field.send_keys(username)
                self.logger.info("Username Entered: %s" % username)
            '''else:
                self.logger.info("Empty Username Entered")'''
            
            time.sleep(5)  # Add a delay after entering the username
            return True
        except Exception as e:
            self.logger.error("Failed to enter username: %s" % str(e))
            return False


    def enter_password(self, password):
        try:
            password_field = self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
            password_field.clear()
            
            if password is not None and password != "":
                password_field.send_keys(password)
                self.logger.info("Password Entered")
            '''else:
                self.logger.info("Empty Password Entered")'''
            
            time.sleep(1)  # Add a delay after entering the password
            return True
        except Exception as e:
            self.logger.error("Failed to enter password: %s" % str(e))
            return False

    def enter_empty_username(self):
        try:
            username_field = self.driver.find_element(*LoginPageLocators.USERNAME_INPUT)
            username_field.clear()
            
            username_field.send_keys("")
            self.logger.info("Empty Username Entered")
            
            time.sleep(5)  # Add a delay after entering the username
            return True
        except Exception as e:
            self.logger.error("Failed to enter empty username: %s" % str(e))
            return False
        
    def enter_empty_password(self):
        try:
            password_field = self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
            password_field.clear()
            
            password_field.send_keys(" ")
            self.logger.info("Empty Password Entered")
            
            time.sleep(1)  # Add a delay after entering the password
            return True
        except Exception as e:
            self.logger.error("Failed to enter password: %s" % str(e))
            return False  
        
    def click_login_button(self):
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        self.logger.info("Button Clicked..")
        time.sleep(1)  # Add a delay of 1 second after clicking the login button

    def is_dashboard_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.VISIBLE))
            self.logger.info("Dashboard Displayed succes..")
            #time.sleep(1)  # Add a delay of 1 second after the dashboard is displayed
            return True
        except Exception:
            self.logger.error("Dashboard Displayed error..")
            return False

    def assert_dashboard_displayed(self):
        if self.is_dashboard_displayed():
            return True
        else:
            return False

    def get_error_message(self):
        try:
            error_message_element = self.driver.find_element(*LoginPageLocators.ALERTFAILURE)
            error_message = error_message_element.text
            self.logger.info("Error message found: %s" % error_message)
            time.sleep(1)  # Add a delay of 1 second after getting the error message
            return error_message
        except NoSuchElementException:
                self.logger.error("Failed to get error message")
                return None
        except Exception as e:
            self.logger.error("Failed to get error message: %s" % str(e))
            return None
    
    def required_msg(self, required_msg):
        try:
            error_message_req = self.driver.find_element(*LoginPageLocators.REQUIRED)
            error_message = error_message_req.text
            self.logger.info("Error message found: %s" % error_message)
            time.sleep(1)  # Add a delay of 1 second after getting the error message
            assert error_message == required_msg
        except AssertionError as e:
            self.logger.error(f"Error message assertion failed: {str(e)}")
        except NoSuchElementException:
            self.logger.error("Error message element not found")
        except Exception as e:
            self.logger.error(f"Failed to get error message: {str(e)}")
