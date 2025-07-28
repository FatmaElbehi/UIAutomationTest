
from behave import given, when, then
from pages.addEmployee_page import AddEmployeePage
import logging
import allure

def save_screenshot(context, name):
    context.driver.save_screenshot(name)
    allure.attach(context.driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)


@when(u'I click on the sub-menu Add Employee')
def step_impl(context):
    try:
        context.addEmployee_page.click_Add_Employee_Menu()
        logging.info("Clicked the Add Employee Menu")
        save_screenshot(context, "Add_Employee_Menu_clicked.png") 
    except Exception as e:
        logging.error("An error occurred while clicking the Add Employee Menu: %s", str(e))


@then(u'I redirect to the AddEmployee Interface with url "https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I redirect to the AddEmployee Interface with url "https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee"')