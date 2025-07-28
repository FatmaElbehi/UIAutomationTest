# Projet Selenium Python avec Modèle de Conception Page Object Model (POM)
![Selenium python](https://i.morioh.com/210525/039d36c3.webp)

Ce projet est une mise en œuvre d'automatisation des tests avec Selenium en utilisant le modèle de conception Page Object Model (POM) pour une meilleure maintenabilité et lisibilité du code.

## Structure du Projet
```
TestSelenium/
├── features/
│   └── login.feature
├── steps/
│   └── login_steps.py
├── pages/
│     └── login_page.py
├── target/
│     └──report.html
├── environment.py
├── docker-compose.yml
├── Dockerfile
└── requirements.txt

```  
Le projet est organisé de la manière suivante :

- **features/** : Contient les fichiers Gherkin (.feature) décrivant les scénarios de test.
  - *login.feature* : Exemple d'un fichier de fonctionnalité pour la fonction de connexion.

- **steps/** : Contient les fichiers Python avec les étapes de test correspondant aux scénarios de test.
  - *login_steps.py* : Implémentation des étapes de test pour le scénario de connexion.

- **pages/** : Contient les classes Python représentant les pages de l'application, suivant le modèle POM.
  - *login_page.py* : Page Object pour la page de connexion.

- **target/** : Contient le rapport HTML généré après l'exécution des tests.
  - *report.html* : Rapport d'exécution des tests.

- **environment.py** : Fichier Python pour la configuration de l'environnement de test.

- **requirements.txt** : Liste des dépendances Python nécessaires pour exécuter le projet.
- **docker-compose.yml** : Fichier de configuration pour Docker Compose, spécifiant les services, les réseaux et les volumes pour le projet.

- **Dockerfile** : Fichier de configuration Docker décrivant l'environnement et les dépendances nécessaires pour exécuter les tests Selenium.

# Installation (pré-requis) Localement
- Install Python: Download and install the latest version of Python from the official Python website (https://www.python.org/downloads/).

- Install pip: pip is the package manager for Python. You can install pip by running the following command in the command prompt or terminal:
```
python -m ensurepip --default-pip
```
- Installez les dépendances en exécutant `pip install -r requirements.txt`.

# Dockerisation 
Pour créer un nouveau network externe on utilise la commande suivante:
```bash
docker network create orange-network
```
Le projet est maintenant Dockerisé avec les fichiers additionnels suivants **docker-compose.yml** et **Dockerfile**
Pour les exécuter, utilisez la cmd suivante :
```bash
docker-compose up -d
```

# Exécution des tests 
Pour exécuter tous les scénarios de test, utilisez la commande suivante :
```
behave
```
Pour exécuter tous les scénarios de test sur chrome avec Powershell  :
```
behave -D browser=chrome -f behave_html_formatter:HTMLFormatter -o "target/report_chrome$(Get-Date -Format 'yyyyMMdd_HHmmss').html"
```
Pour exécuter tous les scénarios de test sur chrome avec bash  :
```
behave -D browser=chrome -f behave_html_formatter:HTMLFormatter -o "target/report_chrome$(date +"%Y%m%d_%H%M%S").html
```
Pour exécuter tous les scénarios de test sur firefox  :
```
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
behave -D browser=chrome -f behave_html_formatter:HTMLFormatter -o "target/report_edge$timestamp.html"

```
Pour exécuter tous les scénarios de test sur Edge  :
```
behave -D browser=edge -f behave_html_formatter:HTMLFormatter -o target/report_edge$(date +"%Y%m%d_%H%M%S").html

```
Pour exécuter un scénario spécifique, ajoutez le nom du fichier feature après la commande behave :
```
behave features/login.feature
```
To execute only the login feature with the OK tag:
```
behave features/login.feature --tags=@login-ok
```
# Reporting 
Générez un rapport HTML en utilisant la commande suivante :
```
behave --format behave_html_formatter:HTMLFormatter -o target/report_$(date +"%Y%m%d_%H%M%S").html
```
# Synthèse Framework de test auto en BDD

- Approche agile
  - Approche BDD 

  - Report 
    - [Behave-report](https://behave.readthedocs.io/en/latest/formatters.html)
  - Langage de Scripting
      - Python
- Architecture / Structure
  - POM (Page Object Model)
  - features
  - pages
  - steps
  - target