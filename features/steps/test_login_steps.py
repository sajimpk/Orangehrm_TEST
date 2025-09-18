from behave import given, when, then
import time
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("I am on the login page")
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    # context.login_page = LoginPage(context.driver)

@when('I enter username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page.username_input.send_keys(username)
    context.login_page.password_input.send_keys(password)

@when("I click on the login button")
def step_impl(context):
    context.login_page.login_button.click()

@then("I should see the dashboard page")
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of(context.login_page.dashboard_header)
    )
    time.sleep(5)
    assert context.login_page.dashboard_header.is_displayed()
