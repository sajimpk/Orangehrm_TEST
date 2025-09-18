# 🧪 Selenium + Behave BDD Framework with POM & Allure Reporting

A **Python Selenium BDD framework** using **Behave** with **Page Object Model (POM)** design and **Allure reporting** for automated UI testing.

---

## ⚡ Features

- Selenium WebDriver for browser automation
- BDD testing with Behave (`.feature` files)
- Page Object Model (POM) for scalable maintainable code
- Dynamic waits using `WebDriverWait` and `expected_conditions`
- Allure integration for beautiful interactive reports
- Supports multiple pages (Login, Dashboard, etc.)
- Python 3.10+ compatible

---

## 📁 Project Structure
```
├── env/ 
├── features/
│ ├── login.feature 
│ └── steps/
│ └── test_login_steps.py
├── pages/
│ ├── login_page.py
│ └── dashboard_page.py
├── reports/
├── environment.py
└── README.md
```
## SET-UP
### Create Virtual Environment
```
python -m venv env
```
### Activate Environment
```
env\Scripts\activate
```
### Install Dependencies
```
pip install -r requirements.txt
```
### 🏃 Run Behave Tests
```
behave -f allure_behave.formatter:AllureFormatter -o reports
```
### Serve Allure Report
Make sure you have Allure CLI installed and Java 8+ set in your environment.
```
allure serve reports
```
