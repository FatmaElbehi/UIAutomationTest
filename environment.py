from selenium import webdriver
from datetime import datetime 
import allure
from allure_commons.types import AttachmentType


def before_all(context):
    context.browser_name = context.config.userdata.get('browser', 'chrome')
    try:
        if context.browser_name == "chrome":
            chrome_options = webdriver.ChromeOptions()
            #chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            context.driver = webdriver.Chrome(chrome_options)
            context.driver.maximize_window()
        elif context.browser_name == "firefox":
            firefox_options = webdriver.FirefoxOptions()
            #firefox_options.add_argument('--disable-gpu')
            firefox_options.add_argument('--no-sandbox')
            firefox_options.add_argument('--disable-dev-shm-usage')
            context.driver = webdriver.Firefox(firefox_options)
            context.driver.maximize_window()
        elif context.browser_name == "edge":
            edge_options = webdriver.EdgeOptions()  
            #edge_options.add_argument('--disable-gpu')
            edge_options.add_argument('--no-sandbox')
            edge_options.add_argument('--disable-dev-shm-usage')
            context.driver = webdriver.Edge(edge_options)  
            context.driver.maximize_window()    
        else:
            raise ValueError("Browser not supported")
    except Exception as e:
        print(f"Error during WebDriver setup: {str(e)}")
        raise e  # Rethrow the exception to stop the execution if there's an error


def after_all(context):
    attach_screenshot(context)
    try:
        if hasattr(context, 'driver'):
            context.driver.quit()
    except Exception as e:
        print(f"Error during WebDriver teardown: {str(e)}")


def after_step(context, step):
    if step.status == "failed":
        attach_screenshot(context)


def attach_screenshot(context):
    allure.attach(
        name="Screenshot",
        body=context.driver.get_screenshot_as_png(),
        attachment_type=AttachmentType.PNG
    )

