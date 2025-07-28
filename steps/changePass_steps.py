from allure_commons import fixture
from behave import given, when, then
from pages.changepassword_page import ChangePasswordPage
import allure
import time

def save_screenshot(context, name):
    context.driver.save_screenshot(name)
    allure.attach(context.driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)

@fixture
def login_before_change_password(context):
    context.execute_steps("""
        Given I am on the login page
        When I enter my username "Admin"
        And I enter my password "password"
        And I click the login button
        Then I should be redirected to the dashboard page
    """)


@given(u'I am on the update password interface')
def step_impl(context):
    context.changepassword_page = ChangePasswordPage(context.driver)
    context.changepassword_page.visitUpdatePass()
    time.sleep(5) 
    save_screenshot(context, "UpdatePassword_page.png")


@when(u'I enter my current password "{current_password}"')
def step_impl(context,current_password):
    context.changepassword_page.enter_current_password(current_password)
    save_screenshot(context, "EnterCurrentPassword_entered.png")


@when('I enter my new password "{new_password}"')
def step_impl(context,new_password):
    context.changepassword_page.enter_new_password(new_password)
    save_screenshot(context, "EnterNewPassword_entered.png")

@when('I enter my confirm password "{confirm_password}"')
def step_impl(context,confirm_password):
    context.changepassword_page.enter_confirm_password(confirm_password)
    save_screenshot(context, "EnterConfirmPassword_entered.png")


@then(u'I click on the cancel button')
def step_impl(context):
    context.changepassword_page.click_cancel_button()
    #save_screenshot(context, "Cancel_button_clicked.png") 

@then('I should receive an error msg under current_password field "{msg_error1}"')
def step_impl(context,msg_error1):
    context.changepassword_page.required_msg(msg_error1)
    save_screenshot(context, "RequiredMsgCurrentPass_received.png")


@then(u'I should receive an error msg under new_password field "{msg_error2}"')
def step_impl(context,msg_error2):
    context.changepassword_page.required_msg(msg_error2)
    save_screenshot(context, "RequiredMsgNewPass_received.png")

@then(u'I should receive an error msg under confirm_password field "{msg_error3}"')
def step_impl(context,msg_error3):
    context.changepassword_page.required_msg(msg_error3)
    save_screenshot(context, "RequiredMsgConfirmPass_received.png")

@then(u'I click on the save button')
def step_impl(context):
    context.changepassword_page.click_save_button()
    save_screenshot(context, "Save_button_clicked.png")    


@then(u'I received an error password matching msg "{matching_msg_error}"')
def step_impl(context,matching_msg_error):
    context.changepassword_page.matching_msg(matching_msg_error)
    save_screenshot(context, "MatchingPassMsg_received.png")


@then(u'I received an error password msg "{least_msg_error}"')
def step_impl(context,least_msg_error):
    context.changepassword_page.least_msg(least_msg_error)
    save_screenshot(context, "LeastPassMsg_received.png")