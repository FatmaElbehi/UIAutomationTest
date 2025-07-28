import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.CommonMethods import CommonMethods
from resources.ChangePasswordPageLocators import ChangePasswordPageLocators
from resources.LoginPageLocators import LoginPageLocators

import logging
from selenium.common.exceptions import NoSuchElementException
import os


log_path = os.path.join('logs', 'app.log')
logging.basicConfig(filename=log_path, level=logging.INFO, filemode='a', format='%(asctime)s - %(levelname)s : %(message)s')
# Add a separate handler for ERROR level messages
error_handler = logging.FileHandler(log_path)
error_handler.setLevel(logging.ERROR)
error_formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
error_handler.setFormatter(error_formatter)

# Attach the error handler to the root logger
logging.getLogger().addHandler(error_handler)

class ChangePasswordPage():

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def visitUpdatePass(self):

        try:
            Icon=self.driver.find_element(*ChangePasswordPageLocators.ICON_CLICK)
            time.sleep(5)  
            Icon.click()
            self.logger.info("Icon clicked..")
            ChangePass_link = self.driver.find_element(*ChangePasswordPageLocators.CHANGEPASSWORD_INPUT)
            time.sleep(5) 
            ChangePass_link.click()
            logging.info("Click on change password Link...")
            UpdatePass_title = self.driver.find_element(*ChangePasswordPageLocators.UPDATEPASS_TITLE)
            self.logger.info("Update Password Title Found: %s" % UpdatePass_title)
            return True
        except Exception:
            self.logger.error("Icon not clicked ..")
            return False


    def enter_current_password(self,current_password):
        try:
            current_password_field = self.driver.find_element(*ChangePasswordPageLocators.CURRENT_PASSWORD_INPUT)
            current_password_field.send_keys(current_password)
            self.logger.info("Current Password Entered")
            time.sleep(1)  # Add a delay after entering the password
            return True
        except Exception as e:
            self.logger.error("Failed to enter current password: %s" % str(e))
            return False  
        
    def enter_new_password(self,new_password):
        try:
            new_password_field = self.driver.find_element(*ChangePasswordPageLocators.NEW_PASSWORD_INPUT)
            new_password_field.send_keys(new_password)
            self.logger.info("New Password Entered")
            time.sleep(1) 
            return True
        except Exception as e:
            self.logger.error("Failed to enter new password: %s" % str(e))
            return False
       

    def enter_confirm_password(self,confirm_password):
        try:
            confirm_password_field = self.driver.find_element(*ChangePasswordPageLocators.CONFIRM_PASSWORD_INPUT)
            confirm_password_field.send_keys(confirm_password)
            self.logger.info("Confirm Password Entered")
            time.sleep(1) 
            return True
        except Exception as e:
            self.logger.error("Failed to enter confirm password: %s" % str(e))
            return False 
    
    def click_cancel_button(self):
        self.driver.find_element(*ChangePasswordPageLocators.CANCEL_BTN).click()
        time.sleep(5)
        self.logger.info("Button Cancel Clicked..")
        return_dashboard = self.driver.find_element(*LoginPageLocators.VISIBLE)
        return_dashboard_txt = return_dashboard.text
        self.logger.info("Dashboard Title found: %s" % return_dashboard_txt)
        time.sleep(1)  

    def click_save_button(self):
        self.driver.find_element(*ChangePasswordPageLocators.SAVE_BTN).click()
        #time.sleep(5)
        self.logger.info("Button Save Clicked..")
        success_alert=self.driver.find_element(*ChangePasswordPageLocators.SUCCESS_ALERT)
        success_alert_txt = success_alert.text
        self.logger.info("Success Alert found: %s" % success_alert_txt)
        time.sleep(1)
        

    def required_msg(self,msg_error3):
        try:
            error_message_req = self.driver.find_element(*ChangePasswordPageLocators.REQUIRED_LABEL)
            error_message = error_message_req.text
            self.logger.info("Error message found: %s" % error_message)
            time.sleep(1)  # Add a delay of 1 second after getting the error message
            assert error_message == msg_error3
        except AssertionError as e:
            self.logger.error(f"Error message assertion failed: {str(e)}")
        except NoSuchElementException:
            self.logger.error("Error message element not found")
        except Exception as e:
            self.logger.error(f"Failed to get error message: {str(e)}")    


    def matching_msg(self,matching_msg_error):        
        try:
            error_message_matching = self.driver.find_element(*ChangePasswordPageLocators.MATCHING_LABEL)
            error_matching = error_message_matching.text
            self.logger.info("Error matching message found: %s" % error_matching)
            time.sleep(1)  
            assert error_matching == matching_msg_error
        except AssertionError as e:
            self.logger.error(f"Error message matching assertion failed: {str(e)}")
        except NoSuchElementException:
            self.logger.error("Error message matching element not found")
        except Exception as e:
            self.logger.error(f"Failed to get error matching message: {str(e)}")


    def least_msg(self,least_msg_error):
        try:
            error_message_least = self.driver.find_element(*ChangePasswordPageLocators.LEAST_LABEL)
            error_least = error_message_least.text
            self.logger.info("Error least message found: %s" % error_least)
            time.sleep(1)  
            assert error_least == least_msg_error
        except AssertionError as e:
            self.logger.error(f"Error message least password <7 assertion failed: {str(e)}")
        except NoSuchElementException:
            self.logger.error("Error message least pass element not found")
        except Exception as e:
            self.logger.error(f"Failed to get error least pass message <7 : {str(e)}")