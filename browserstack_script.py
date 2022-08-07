# Import necessary packages
import os, time
from browserstack/bin/dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from threading import Thread

# Load the environment variables from the .env file
load_dotenv()

# Name of the build that will run remotely on BrowserStack
# Tests will be organized within this build
BUILD_NAME = "browserstack-build-amazon-sign-in"

# The 'capabilities' array defines various browser, device, and OS combinations for the test to run.
capabilities = [
    {
        "browserName": "chrome",
        "browserVersion": "103.0",
        "os": "Windows",
        "osVersion": "11",
        "sessionName": "Parallel Test Chrome Windows",  # test name
        "buildName": BUILD_NAME  
    },
    {
        "browserName": "firefox",
        "browserVersion": "102.0",
        "os": "Windows",
        "osVersion": "10",
        "sessionName": "Parallel Test Firefox Windows",
        "buildName": BUILD_NAME
    },
]

# Change browsers
def get_browser_option(browser):
    switcher = {
        "chrome": ChromeOptions(),
        "firefox": FirefoxOptions(),
    }
    return switcher.get(browser, ChromeOptions())

# The run_session() function handles the sign in to Amazon.
# Depending on your location, modify the default value of 
# the argument AMZ_URL.
# This function also assumes that 2-factor authentication is disabled.
def run_session(cap, AMZ_URL="https://amazon.in/"):
    cap["userName"] = os.environ.get("BROWSERSTACK_USERNAME")
    cap["accessKey"] = os.environ.get("BROWSERSTACK_ACCESS_KEY")
    options = get_browser_option(cap["browserName"].lower())
    options.set_capability("browserName", cap["browserName"].lower())
    options.set_capability("bstack:options", cap)
    driver = webdriver.Remote(
        command_executor="https://hub.browserstack.com/wd/hub", options=options
    )
    # Go to Amazon sign in page
    driver.get(AMZ_URL)
    sign_in_button = driver.find_element(By.ID, "nav-link-accountList")
    sign_in_button.click()
    time.sleep(2)
    # Access the sign in credentials
    AMAZON_EMAIL = os.environ.get("AMAZON_EMAIL")
    AMAZON_PASSWORD = os.environ.get("AMAZON_PASSWORD")
    # Enter email and continue
    username_textbox = driver.find_element(By.ID, "ap_email")
    username_textbox.send_keys(AMAZON_EMAIL)
    time.sleep(2)
    continue_button = driver.find_element(By.ID, "continue")
    continue_button.submit()
    time.sleep(2)
    # Enter password and submit
    password_textbox = driver.find_element(By.ID, "ap_password")
    password_textbox.send_keys(AMAZON_PASSWORD)
    time.sleep(2)
    sign_in_button = driver.find_element(By.ID, "auth-signin-button-announce")
    sign_in_button.submit()
    time.sleep(2)
    print("Sign in test complete.")
    driver.quit()

# The Thread() function takes run_session function and each set of capability from the caps array as an argument to run each session in parallel.
for cap in capabilities:
    Thread(target=run_session, args=(cap,)).start()