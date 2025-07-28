@allure.label.epic:Authentification
Feature: Login
@allure.label.story:FailedScenario
@login-KO
   Scenario Outline: Login with invalid credentials
    Given I am on the login page
    When I enter my username "<username>"
    And I enter my password "<password>"
    And I click the login button
    Then I should receive an error alert "<alert>"
      Examples:
      | username        | password  |         alert       |
      | Admin           | admin123  | Invalid credentials |
      | tn7887888899999 | test123   | Invalid credentials |
       

@allure.label.story:FailedScenario
@login-KO
   Scenario Outline: Login with empty credentials
    Given I am on the login page
    When I enter my empty username 
    And I enter my empty password 
    And I click the login button
    Then I should receive an error msg under username field "<msg_error1>"
    And I should receive an error msg under password field "<msg_error2>"
      Examples:
      | msg_error1  | msg_error2 |
      | Required    | Required   |

      
@allure.label.story:FailedScenario
@login-KO
   Scenario Outline: Login with empty credentials
    Given I am on the login page
    When I enter my username "<username>"
    And I enter my empty password 
    And I click the login button
    Then I should receive an error msg under username field "<msg_error1>"
    And I should receive an error msg under password field "<msg_error2>"
      Examples:
      | username        | msg_error1  | msg_error2 |
      | tn7887888888888 | Required    | Required   |

      
@allure.label.story:FailedScenario
@login-KO
   Scenario Outline: Login with empty credentials
    Given I am on the login page
    When I enter my empty username 
    And I enter my password "<password>"
    And I click the login button
    Then I should receive an error msg under username field "<msg_error1>"
    And I should receive an error msg under password field "<msg_error2>"
      Examples:
      | password     | msg_error1  | msg_error2 |
      | test1223656@ | Required    | Required   |

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
      | Admin    | admin123 |

