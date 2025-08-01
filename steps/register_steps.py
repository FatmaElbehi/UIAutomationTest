from behave import given, when, then
from pages.register_page import RegisterPage
import logging
import allure

def save_screenshot(context, name):
    context.driver.save_screenshot(name)
    allure.attach(context.driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)


@given(u'I am on the register page')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.visit()
    save_screenshot(context, "register_page.png")

@when(u'I click on the Register button')
def step_impl(context):
    try:
        context.register_page.click_register_button()
        logging.info("Clicked the Register button")
        save_screenshot(context, "Register_button_clicked.png")
    except Exception as e:
        logging.error("An error occurred while clicking the Register button: %s", str(e))


@then(u'I should receive a success alert "{msgalert}"')
def step_impl(context, msgalert):
    msgalert = context.register_page.get_success_message()
    save_screenshot(context, "SuccessAlert_received.png") \

@then(u'I will be redirect to the login page')
def step_impl(context):
    context.login_page.assert_login_displayed()
    save_screenshot(context, "Redirect_Login.png")
