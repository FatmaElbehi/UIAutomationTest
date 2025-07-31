from selenium.webdriver.common.by import By

class LoginPageLocators:

    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//span[contains(@class, 'MuiButton-label')]")
    ALERTFAILURE=(By.CLASS_NAME,'oxd-alert-content-text')
    VISIBLE = (By.CLASS_NAME, 'oxd-text--h6')
    REQUIRED=(By.CLASS_NAME, 'oxd-input-field-error-message')
    FORGOTPASS=(By.CLASS_NAME, 'orangehrm-login-forgot-header')
    CANCELBTN= (By.XPATH, "//button[@type='button']")
    FORGOT_PAGE_TITLE=(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/h6')
    RESETBTN=(By.XPATH, "//button[@type='submit']")
    USERNAME_FORGOT_PASS=(By.CLASS_NAME,"oxd-input--active")
    SEND_PASS_TITLE=(By.CLASS_NAME,"orangehrm-forgot-password-title")

