import logging
from behave import given, when, then
from pages.logout_page import LogoutPage
from pages.dashboard_page import DashboardPage
import allure
import time

def save_screenshot(context, name):
    context.driver.save_screenshot(name)
    allure.attach(context.driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)


@given(u'I am on the Dashboard interface')
def step_impl(context):
    context.dashboard_page = DashboardPage(context.driver)
    context.dashboard_page.visit()
    save_screenshot(context, "Dashboard_page.png")


@when(u'I click on the Log out Button')
def step_impl(context):
    context.logout_page = LogoutPage(context,context.driver)
    context.logout_page.logout()
    save_screenshot(context, "logout.png")
    logging.info("Navigated to the login page")


@then(u'I will be redirect to the login "{url}"')
def step_impl(context,url_login):
    expected_url = url_login
    current_url =context.driver.current_url
    logging.info("Current Url : %s" %current_url)
    assert current_url == expected_url, "Redirection to the login page failed."