from selenium import webdriver
from pages.login_page import LoginPage

def before_all(context):
    # Browser open
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

def before_scenario(context, scenario):
    # প্রতি scenario শুরুতে LoginPage initialize করে দেবে
    context.login_page = LoginPage(context.driver)

def after_scenario(context, scenario):
    print(f"Complate {scenario}")
    
def after_all(context):
    # সব scenario শেষে browser close হবে
    context.driver.quit()
