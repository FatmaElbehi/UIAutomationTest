from lib2to3.pgen2 import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.CommonMethods import CommonMethods
from resources.UsersPageLocators import UsersPageLocators
import yaml
import logging
from selenium.common.exceptions import NoSuchElementException
import time  # Import the time module
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

class UsersPage(CommonMethods):

    def visitUsers(self):
            time.sleep(5) 
          
            '''search_field=self.driver.find_element(*UsersPageLocators.SEARCH)
            search_field.clear()
            search_field.send_keys("Admin")'''
            admin_menu = self.wait_for_element(UsersPageLocators.ADMIN_MENU)
            admin_menu.click()


    def click_Add_button(self):
        self.wait_for_element(*UsersPageLocators.ADD_BUTTON).click()
        self.logger.info("Add Button Clicked..")
        time.sleep(5)  