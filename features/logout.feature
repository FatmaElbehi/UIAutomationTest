@allure.label.epic:LogOut
Feature: LogOut
  @allure.label.epic:LogOut
  @logout-OK
  Scenario: Logout
    Given I click the logout button
    Then I should be redirected to the login page
