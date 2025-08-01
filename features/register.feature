@allure.label.epic:Authentification
Feature: Register
@allure.label.story:FailedScenario
@register-KO1
Scenario Outline: Register with invalid credentials
    Given I am on the register page
    When I enter my username "<username>"
    And I enter my password "<password>"
    And I click on the Register button
    Then I should receive an error alert "<alert>"
    Then Click on the OK button

    Examples:
      | username        | password  |         alert                  |
      | Admin           | Admin  | UserName Admin Already Exist!     |

  @allure.label.story:FailedScenario
    @register-KO2
  Scenario Outline: Register with empty password & confirm password
    Given I am on the register page
    When I enter my username "<username>"
    And I click on the Register button
    Then I should receive an error alert "<alert>"
    Then Click on the OK button
    Examples:
      | username        | alert                             |
      | ppp |Username or password is incorrect! |

  @allure.label.story:FailedScenario
    @register-KO3
  Scenario Outline: Register with empty username
    Given I am on the register page
    When I enter my empty username
    And I enter my password "<password>"
    And I enter my confirm password "<confirm_password>"
    And I click on the Register button
    Then I should receive an error alert "<alert>"
    Then Click on the OK button
    Examples:
      | password | confirm_password |  alert                       |
      | Io.13456 |      Io.13456    |  Add proper parameter first! |

  @allure.label.story:SuccessScenario
    @register-OK
  Scenario Outline: Register with valid credentials
    Given I am on the register page
    When I enter my username "<username>"
    And I enter my password "<password>"
    And I enter my confirm password "<confirm_password>"
    And I click on the Register button
    Then I should receive a success alert "<alert>"
    Then I will be redirect to the login page
    Examples:
      | username    | password    | confirm_password | alert                    |
      | FatmaElbehi | FatmaElbehi | FatmaElbehi      | Registered Successfully. |

