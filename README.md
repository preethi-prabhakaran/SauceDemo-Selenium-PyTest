# SauceDemo-Selenium-PyTest
A maintainable test automation framework built with Python, PyTest, and Selenium WebDriver, following the Page Object Model (POM) design pattern. The framework automates functional tests for the SauceDemo  e-commerce site.

Tech Stack
---------------

Language: Python 3.x
Framework: PyTest
Automation Tool: Selenium WebDriver
Design Pattern: Page Object Model (POM)
Config Management: YAML
Reporting: Pytest-HTML

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
│
├── pytest.ini               # Pytest options and HTML report config
├── requirements.txt
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


Future Enhancements
----------------------

* Add multi-browser support (Edge, Firefox)
* Add parametrized test cases
* Marking of test cases (smoke, sanity, regression etc)
* Integrate CI/CD pipeline
