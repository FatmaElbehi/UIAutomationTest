import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.CommonMethods import CommonMethods
from resources.LogoutPageLocators import LogoutPageLocators
import logging
from selenium.common.exceptions import NoSuchElementException


class LogoutPage(CommonMethods):
    def logout(self):
        Image_avatar = self.wait_for_element(LogoutPageLocators.IMAGE_AVATAR)
        Image_avatar.click()
        Link_logout = self.wait_for_element(LogoutPageLocators.LINK_LOGOUT)
        time.sleep(5) 
        Link_logout.click()
        logging.info("click on logout Link")