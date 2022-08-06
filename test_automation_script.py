from selenium.webdriver import Chrome
import time # The function time.sleep() helps mask the scripted bot behavior.

# Helper function to mimic slow typing by a human
def slow_typing(element, text):
    for character in text: 
        element.send_keys(character)
        time.sleep(0.3)

# Email registered with Amazon
EMAIL_ID = "<email_registered_with_Amazon>"

# Read password from a text file and add the file to .gitignore
# Do not hardcode the password for your Amazon account.
password = ""
with open('password.txt', 'r') as password_file:
    password = password_file.read().replace('\n', '')

# Open browser and go to sign in page
browser = Chrome()
browser.get('https://amazon.in/')
time.sleep(2)
sign_in_button = browser.find_element_by_xpath('//*[@id="nav-link-accountList"]/span')
sign_in_button.click()
time.sleep(2)

# Assumption: There are no two-factor authentication enabled
# Enter the sign in credentials
username_textbox = browser.find_element_by_id("ap_email")
slow_typing(username_textbox, EMAIL_ID)
time.sleep(2)

continue_button = browser.find_element_by_id("continue")
continue_button.submit()
time.sleep(2)

password_textbox = browser.find_element_by_id("ap_password")
slow_typing(password_textbox, password)
time.sleep(2)

sign_in_button = browser.find_element_by_id("auth-signin-button-announce")
sign_in_button.submit()
time.sleep(20)

browser.close()