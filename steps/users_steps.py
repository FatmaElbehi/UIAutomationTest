import time
from behave import given, when, then
from pages.users_page import UsersPage
import logging
import allure

def save_screenshot(context, name):
    context.driver.save_screenshot(name)
    allure.attach(context.driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)


@given(u'I am on the view system users page')
def step_impl(context):
    context.users_page = UsersPage(context,context.driver)
    context.users_page.visitUsers()
    save_screenshot(context, "Users_page.png")


@when(u'I click on the Add button')
def step_impl(context):
        context.users_page.click_Add_button()
        logging.info("Clicked the Add button")
        save_screenshot(context, "Add_button_clicked.png") 

@when(u'I redirect to save system user page')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I redirect to save system user page')


@when(u'I click the cancel button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the cancel button')