from behave import given, when, then
from pages.forgotPass_page import ForgotPassPage
import logging
import allure
import os 

def save_screenshot(context, name):
    context.driver.save_screenshot(name)
    allure.attach(context.driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)


@when(u'I click on ForgotPasswordlink')
def step_impl(context):
        context.forgotPass_page = ForgotPassPage(context.driver)
        context.forgotPass_page.click_forgot_link()
        logging.info("Clicked the forgot password link")
        save_screenshot(context, "forgot_passLink_clicked.png") 

@then(u'I should redirect to Reset Password Interface and get this title "{title_reset}"')
def step_impl(context,title_reset):
        context.forgotPass_page.visitResetPass(title_reset)
        save_screenshot(context, "Reset_Pass.png")

@then(u'I click on Cancel to be redirect to the login page')
def step_impl(context):
    context.forgotPass_page.click_cancel_button()
    logging.info("Clicked the cancel button")
    save_screenshot(context, "cancel_button_clicked.png") 

@then(u'I click on Reset Password Button')
def step_impl(context):
    context.forgotPass_page.click_reset_password_button()
    logging.info("Clicked the reset password button")
    save_screenshot(context, "reset_passwordbutton_clicked.png")


@then('I enter my username "{username}"')
def step_impl(context,username):
    context.forgotPass_page.enter_usernameForgotPass(username)
    save_screenshot(context, "UsernameForgotPassword_entered.png") 

@then('I should redirect to the confirmation Interface by getting this title "{title_password_link}"')
def step_impl(context,title_password_link):
    context.forgotPass_page.sendPassResetInterface(title_password_link)
    save_screenshot(context, "Send_Reset_Pass_Interface.png")