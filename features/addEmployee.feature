@allure.label.epic:Employees
Feature: Add Employee

Background:
    Given I am on the login page
    When I enter my username "Admin"
    And I enter my password "admin123"
    And I click the login button
    Then I should be redirect to the dashboard page

@allure.label.story:FailedScenario
@cancelAddEmployee_KO
   Scenario Outline: Cancel Add Employee Functionality
    Given I am on the update password interface
    When I click on the sub-menu Add Employee
    Then I redirect to the AddEmployee Interface with url "<add_employee_url>"
    And I click on the cancel button    

     Examples:
      | add_employee_url                                                        | 
      | https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee | 
