import webbrowser

url = "https://www.amazon.com"
webbrowser.get('safari').open_new_tab(url)

from selenium import webdriver

# Open Safari browser and go to Amazon
driver = webdriver.Safari()
driver.get("https://www.amazon.com")

# Find the search box element and enter a search query
search_box = driver.find_element_by_id("twotabsearchtextbox")
search_box.send_keys("airpods pro")

# Find the search button element and click it
search_button = driver.find_element_by_css_selector("input.nav-input[type='submit']")
search_button.click()

# Wait for the search results to load
driver.implicitly_wait(10)

# Find the first result and click on it
first_result = driver.find_element_by_css_selector("div.s-result-list > div:nth-child(1)")
first_result.click()

# Wait for the product page to load
driver.implicitly_wait(10)

# Find the add-to-cart button and click it
add_to_cart_button = driver.find_element_by_id("add-to-cart-button")
add_to_cart_button.click()

# Wait for the cart page to load
driver.implicitly_wait(10)

# Find the checkout button and click it
checkout_button = driver.find_element_by_css_selector("#hlb-ptc-btn-native")
checkout_button.click()
# 