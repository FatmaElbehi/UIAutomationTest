from selenium.webdriver.common.by import By

class UsersPageLocators:

    ADMIN_MENU=(By.CSS_SELECTOR, "a[href='/web/index.php/admin/viewAdminModule']")
    SEARCH=(By.CLASS_NAME,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/div/div/input")
    ADD_BUTTON=(By.CLASS_NAME,"oxd-button--medium")
    BAR=(By.CLASS_NAME,"oxd-icon")
    CLOSE=(By.CLASS_NAME,"oxd-sidepanel-header-close")

