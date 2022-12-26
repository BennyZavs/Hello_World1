from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://github.com/login")

# signin_link = browser.find_element
# signin_link.click()
username_box = browser.find_element_by_id("login_field")
username_box.send_keys("_Input Login_")
password_box = browser.find_element_by_id("password")
password_box.send_keys("_Input Password_")
password_box.submit
