from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resources.LoginPageLocators import LoginPageLocators
import yaml
import logging
import os
from selenium.common.exceptions import NoSuchElementException
import time  # Import the time module
from pages.login_page import LoginPage


log_path = os.path.join('logs', 'app.log')
logging.basicConfig(filename=log_path, level=logging.INFO, filemode='a', format='%(asctime)s - %(levelname)s : %(message)s')
# Add a separate handler for ERROR level messages
error_handler = logging.FileHandler(log_path)
error_handler.setLevel(logging.ERROR)
error_formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
error_handler.setFormatter(error_formatter)

# Attach the error handler to the root logger
logging.getLogger().addHandler(error_handler)

class ForgotPassPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    
    def click_forgot_link(self):
        self.driver.find_element(*LoginPageLocators.FORGOTPASS).click()
        self.logger.info("Forgot Pass Link Clicked..")
        time.sleep(5) 

    
    def visitResetPass(self,title_reset):
        with open('config/driver.yml') as file:
         config = yaml.safe_load(file)
         reset_pass_url = config.get("RESET_PASS_URL", "")
        self.driver.get(reset_pass_url)
        time.sleep(5) 
        forgot_title = self.driver.find_element(*LoginPageLocators.FORGOT_PAGE_TITLE).text
        assert forgot_title == title_reset
        self.logger.info("Reset Password page Visited and Receive this title: %s" % forgot_title)


    def click_cancel_button(self):
        self.driver.find_element(*LoginPageLocators.CANCELBTN).click()
        self.logger.info("Cancel Button Clicked..")
        time.sleep(5) 
        '''
        login_page.visit()
        self.driver.find_element(*LoginPageLocators.CANCELBTN).click()
        self.logger.info("Cancel Button Clicked..")'''
    
    def click_reset_password_button(self):
        self.driver.find_element(*LoginPageLocators.RESETBTN).click()
        self.logger.info("Reset Password Button Clicked..")
        time.sleep(2) 

    def enter_usernameForgotPass(self,username):
        username_field = self.driver.find_element(*LoginPageLocators.USERNAME_FORGOT_PASS)
        username_field.clear()
            
        if username is not None and username != "":
            username_field.send_keys(username)
            self.logger.info("Username in Forgot Password Section Entered: %s" % username)    

    def sendPassResetInterface(self,title_password_link):
        with open('config/driver.yml') as file:
         config = yaml.safe_load(file)
         send_reset_pass_url = config.get("SEND_RESET_PASS_URL", "")
        self.driver.get(send_reset_pass_url)
        time.sleep(5) 
        pass_link_title = self.driver.find_element(*LoginPageLocators.SEND_PASS_TITLE).text
        assert pass_link_title == title_password_link
        self.logger.info("Reset Password sent successfully Visited and Receive this title: %s" % pass_link_title)