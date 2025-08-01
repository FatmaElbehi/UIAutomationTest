# Projet Selenium Python avec Modèle de Conception Page Object Model (POM)
![Selenium python](https://i.morioh.com/210525/039d36c3.webp)

Ce projet est une mise en œuvre d'automatisation des tests avec Selenium en utilisant le modèle de conception Page Object Model (POM) pour une meilleure maintenabilité et lisibilité du code.

## Structure du Projet
```
TestSelenium/
├── features/
│   └── login.feature
    └── logout.feature
├── steps/
│   └── login_steps.py
    └── logout_steps.py
├── pages/
│     └── login_page.py
├── target/
│     └──report.html
├── environment.py
├── docker-compose.yml
├── Dockerfile
└── requirements.txt

```  

The project is organized as follows:

- **features/**: Contains Gherkin (.feature) files that describe test scenarios.
  - *login.feature*: Example feature file for login functionality.

- **steps/**: Contains Python step definitions corresponding to test scenarios.
  - *login_steps.py*: Implementation of test steps for the login scenario.

- **pages/**: Contains Python classes representing application pages, following the Page Object Model (POM).
  - *login_page.py*: Page Object for the login page.

- **target/**: Stores the generated HTML report after test execution.
  - *report.html*: Test execution report.

- **environment.py**: Python configuration file for setting up the test environment.

- **requirements.txt**: List of Python dependencies needed to run the project.

- **docker-compose.yml**: Configuration file for Docker Compose defining services, networks, and volumes.

- **Dockerfile**: Docker configuration file describing the environment and dependencies to run Selenium tests.

---

## ⚙️ Local Setup

### ✅ Prerequisites

- Python (3.x)
- pip (Python package manager)

### 🔧 Install Dependencies

```bash
pip install -r requirements.txt

- Install Python: Download and install the latest version of Python from the official Python website (https://www.python.org/downloads/).

- Install pip: pip is the package manager for Python. You can install pip by running the following command in the command prompt or terminal:
```
python -m ensurepip --default-pip

## 🐳 Dockerisation

To create a new external Docker network, use the following command:

```bash
  docker network create orange-network
```
The project is now Dockerized using the additional files docker-compose.yml and Dockerfile.
To run the containers, use the following command:
```bash
docker-compose up -d
```

## ▶️ Running Tests

```bash
behave
```
To execute all test scenarios on Chrome using Bash:

To run a specific scenario, provide the feature file name:
```
behave features/login.feature
```
To run only tagged scenarios, for example with the tag @login-ok:
```
behave features/login.feature --tags=@login-ok
```
# Reporting 
Generate an HTML report using the following command:
```
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
behave -D browser=chrome -f behave_html_formatter:HTMLFormatter -o "target/report_$(date +"%Y%m%d_%H%M%S").html
```