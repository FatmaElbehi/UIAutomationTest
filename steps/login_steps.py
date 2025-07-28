from behave import given, when, then
from pages.login_page import LoginPage
import logging
import allure

def save_screenshot(context, name):
    context.driver.save_screenshot(name)
    allure.attach(context.driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)

@given("I am on the login page")
def step_impl(context):
        context.login_page = LoginPage(context.driver)
        context.login_page.visit()
        save_screenshot(context, "login_page.png") 
         
@when('I enter my username "{username}"')
def step_impl(context, username):
        context.login_page.enter_username(username)
        save_screenshot(context, "Username_entered.png") 
        
@when(u'I enter my password "{password}"')
def step_impl(context, password):
        context.login_page.enter_password(password)
        save_screenshot(context, "Password_entered.png") 

@when('I click on the login button')
def step_impl(context):
    try:
        context.login_page.click_login_button()
        logging.info("Clicked the login button")
        save_screenshot(context, "Login_button_clicked.png") 
    except Exception as e:
        logging.error("An error occurred while clicking the login button: %s", str(e))
        
@then('I will be redirect to the dashboard page')
def verify_redirection(context):
       context.login_page.assert_dashboard_displayed()
       save_screenshot(context, "Redirect_Dashboard.png") 

@then('I should receive an error alert "{msgalert}"')
def step_impl(context, msgalert):
    msgalert = context.login_page.get_error_message()
    save_screenshot(context, "Alert_received.png") 

@when(u'I enter my empty username')
def step_impl(context):
        context.login_page.enter_empty_username()
        save_screenshot(context, "EmptyUsername_entered.png") 

@when(u'I enter my empty password')
def step_impl(context):
        context.login_page.enter_empty_password()
        save_screenshot(context, "EmptyPass_entered.png") 

@then('I should receive an error msg under username field "{msg_error1}"')
def step_impl(context,msg_error1):
    context.login_page.required_msg(msg_error1)
    save_screenshot(context, "RequiredMsg_received.png") 


@then('I should receive an error msg under password field "{msg_error2}"')
def step_impl(context,msg_error2):
    context.login_page.required_msg(msg_error2)
    save_screenshot(context, "RequiredMsg_received.png") 


