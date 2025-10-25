# SauceDemo-Selenium-PyTest
This project implements an end-to-end automated testing framework for the Saucedemo E-commerce Website using Python, Selenium, and Pytest.
It validates core functionalities like authentication, product browsing, add-to-cart, checkout, and burger menu interactions — packaged with Docker for portability and integrated with Jenkins CI/CD for automated execution and reporting.

Tech Stack
---------------

Language: Python 3.x
Framework: PyTest
Automation Tool: Selenium WebDriver
Design Pattern: Page Object Model (POM)
Config Management: YAML
Reporting: Pytest-HTML
Containerization:	Docker
CI/CD:	Jenkins

Project Structure
--------------------

├── config/
│   ├── config.yaml          # Base URL, credentials, browser
│   └── config_reader.py     # Config loader
│
├── pages/                   # Page object classes
│   ├── login_page.py
│   ├── products_page.py
│
├── tests/                   # Test cases and fixtures
│   ├── test_login.py
│   └── conftest.py
│
├── utils/
│   └── create_driver.py     # WebDriver setup (Chrome)
├── Dockerfile                   # Builds test environment image
├── Jenkinsfile                  # Defines CI/CD pipeline
├── pytest.ini                   # Pytest reporting configuration (HTML & JUnit reporting)
├── requirements.txt             # Python dependencies
└── README.md


Framework Design
-------------------

* Page Object Model (POM): Each page encapsulates its locators and actions, which enhances maintainability
* Conftest.py: contains driver setup and page objects initialization in the form of PyTest Fixtures.
* pytest.ini: handles options for pytest-html reporting such as destination folder
* Configuration: config.yaml defines environment settings; config_reader.py provides access methods.
* Browser Options: Supports headless and non-headless modes via command-line or environment variables.


How to Run Tests
------------------
Install dependencies:
pip install -r requirements.txt

Run all tests:
pytest -v

Run a specific test:
pytest tests/test_login.py::test_valid_login

How to runn Tests with Docker
------------------------------
1️. Build Docker Image
docker build -t saucedemo-test .

2️. Run Tests in Container
docker run --rm -e BASE_URL="https://www.saucedemo.com/" -e HEADLESS="true" -v "${PWD}/reports:/app/results" saucedemo-test
Reports are generated under reports/report.html on your host machine.

Jenkins CI/CD Integration
---------------------------

The Jenkinsfile automates the following stages:
1. Checkout source code from Git.
2. Build Docker image containing the test framework.
3. Run tests inside the Docker container.
4. Publish pytest-html report in Jenkins.


Future Enhancements
----------------------

* Add multi-browser support (Edge, Firefox)
* Add parametrized test cases
* Marking of test cases (smoke, sanity, regression etc)
* Integrate Allure Reports for enhanced visualization.
