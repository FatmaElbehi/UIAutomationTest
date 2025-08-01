@allure.label.epic:LogOut
Feature: LogOut
  @logout-OK
  Scenario Outline: Logout
    Given I am on the Dashboard interface
    When I click on the Log out Button
    Then I will be redirect to the login "<url>"
    Examples:
      | url                   |
      |http://localhost:3000/ |
