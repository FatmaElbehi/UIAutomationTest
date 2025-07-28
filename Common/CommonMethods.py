import logging
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



log_path = os.path.join('logs', 'app.log')
logging.basicConfig(filename=log_path, level=logging.INFO, filemode='a', format='%(asctime)s - %(levelname)s : %(message)s')
# Add a separate handler for ERROR level messages
error_handler = logging.FileHandler(log_path)
error_handler.setLevel(logging.ERROR)
error_formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
error_handler.setFormatter(error_formatter)

# Attach the error handler to the root logger
logging.getLogger().addHandler(error_handler)
from selenium.common.exceptions import TimeoutException

class CommonMethods:
    def __init__(self, context,driver):
        self.context = context
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def wait_for_element(self, locator, timeout=50):
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    
    def find_element(self, *locator):
            return self.driver.find_element(*locator)