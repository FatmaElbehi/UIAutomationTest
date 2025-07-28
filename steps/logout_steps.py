import logging
from behave import given, when, then
from pages.logout_page import LogoutPage
import allure
import time

def save_screenshot(context, name):
    context.driver.save_screenshot(name)
    allure.attach(context.driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)

@given(u'I click the logout button')
def step_impl(context):
    save_screenshot(context, "DashboardInterface.png")
    context.logout_page = LogoutPage(context,context.driver)
    context.logout_page.logout() 
    time.sleep(5) 
    save_screenshot(context, "logout.png")
    logging.info("Navigated to the login page")

@then(u'I should be redirected to the login page')
def step_impl(context):
    # Vérifiez que la redirection a été effectuée en vérifiant l'URL actuelle
    expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    current_url =context.driver.current_url
    logging.info("Current Url : %s" %current_url)
    assert current_url == expected_url, "La redirection vers la page de connexion a échoué."