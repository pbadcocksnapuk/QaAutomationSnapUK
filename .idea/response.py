import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from seleniumwire import webdriver  # Import from seleniumwire

# Create a new instance of the Chrome driver
opts = webdriver.ChromeOptions()
url = 'https://qa6-web.snapfinance.co.uk/'
webdriver.Chrome(options = opts)

# Go to the Google home page
driver.get(url)

# Access requests via the `requests` attribute
for request in driver.requests:
    if request.response:
        print(
            request.url,
            request.response.status_code,
            request.response.headers['Content-Type']
        )