from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resources.AddEmployeeLocators import AddEmployeeLocators
import logging
import os
from selenium.common.exceptions import NoSuchElementException
import time  # Import the time module


log_path = os.path.join('logs', 'app.log')
logging.basicConfig(filename=log_path, level=logging.INFO, filemode='a', format='%(asctime)s - %(levelname)s : %(message)s')
# Add a separate handler for ERROR level messages
error_handler = logging.FileHandler(log_path)
error_handler.setLevel(logging.ERROR)
error_formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
error_handler.setFormatter(error_formatter)

# Attach the error handler to the root logger
logging.getLogger().addHandler(error_handler)

class AddEmployeePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)


    def click_Add_Employee_Menu(self):
        self.driver.find_element(*AddEmployeeLocators.ADD_MENU).click()
        self.logger.info("Add Menu Clicked..")
        time.sleep(5)  
    
