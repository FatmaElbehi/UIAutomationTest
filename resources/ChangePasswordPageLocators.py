from selenium.webdriver.common.by import By

class ChangePasswordPageLocators:

    ICON_CLICK=(By.CLASS_NAME,"oxd-userdropdown-img")
    CHANGEPASSWORD_INPUT = (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[3]/a")    
    UPDATEPASS_TITLE=(By.CLASS_NAME,"orangehrm-main-title")
    CURRENT_PASSWORD_INPUT=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/input")
    NEW_PASSWORD_INPUT=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input")
    CONFIRM_PASSWORD_INPUT=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input")
    CANCEL_BTN=(By.CLASS_NAME,"oxd-button--medium")
    SAVE_BTN=(By.CLASS_NAME,"oxd-button--secondary")
    REQUIRED_LABEL=(By.CLASS_NAME,"oxd-input-field-error-message") 
    SUCCESS_ALERT=(By.ID,"oxd-toaster_1")
    MATCHING_LABEL=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/span")
    LEAST_LABEL=(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/span")