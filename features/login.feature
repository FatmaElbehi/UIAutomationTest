@allure.label.epic:Authentification
Feature: Login
@allure.label.story:FailedScenario
@login-KO1
   Scenario Outline: Login with invalid credentials
    Given I am on the login page
    When I enter my username "<username>"
    And I enter my password "<password>"
    And I click on the login button
    Then I should receive an error alert "<alert>"
    Then Click on the OK button

  Examples:
      | username        | password  |         alert                     |
      | Admin           | admin123  | Username or password is incorrect!|
      
@allure.label.story:FailedScenario
@login-KO2
   Scenario Outline: Login with empty password
    Given I am on the login page
    When I enter my username "<username>"
    And I click on the login button
    Then I should receive an error alert "<alert>"
    Then Click on the OK button
      Examples:
      | username        | alert                             |
      | tn7887888888888 |Username or password is incorrect! |

@allure.label.story:FailedScenario
@login-KO3
   Scenario Outline: Login with empty username
    Given I am on the login page
    When I enter my empty username
    And I enter my password "<password>"
    And I click on the login button
    Then I should receive an error alert "<alert>"
    Then Click on the OK button
      Examples:
      | username        | alert                             |
      | InvalidUsername |Add proper parameter first!        |

@allure.label.story:SuccessScenario
@login-OK
   Scenario Outline: Login with valid credentials
    Given I am on the login page
    When I enter my username "<username>"
    And I enter my password "<password>"
    And I click on the login button
    Then I will be redirect to the dashboard page
      Examples:
      | username | password |
      | Admin    | Admin |

