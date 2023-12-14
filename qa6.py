import time
# commit
from seleniumwire import webdriver  # Import from seleniumwire
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re
import pandas as pd
from snapstar.database.sync_pool.postgres_pool import postgres


url = "https://qa6-web.snapfinance.co.uk/"
driver = webdriver.Chrome() #options = opts)

# Agreeing to cookies
driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/nav/div/div/div/div[2]/button").click()
time.sleep(1)
# Clicking on check eligibility
driver.find_element(By.XPATH,"/html/body/div[3]/header/div[2]/div/div[3]/div[1]/div[2]/ul/li[5]/a").click()
time.sleep(1)
# Step1
# Agreeing to Cookies
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/nav/div/div/div/div[1]/button").click()
time.sleep(1)
# Choosing title
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div[1]/div[1]/div"
                             "/div/label[3]/button").click()
# Entering first name
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div[1]/div[5]/div"
                             "/input").send_keys('John')
# Entering last name
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div[1]/div[6]/div"
                             "/input").send_keys('Smith')
# Selecting marital status
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div[2]/div[2]/div"
                             "/div/label[2]/button").click()
# Entering Date of Birth
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div[3]/div[1]/div"
                             "/input").send_keys('01/01/1999')
# Entering Email
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div[3]/div[2]/div"
                             "/input").send_keys('test@snapfinance.co.uk')
# Entering phone number
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div[3]/div[4]/div"
                             "/input").send_keys('07888888888')
# Entering postcode
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div[4]/div[1]/div"
                             "[1]/div/div/div/div[1]/div/input").send_keys('MK8 0AB')
# Scrolling to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# Clicking on find address
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div[4]/div[1]/div"
                             "[1]/div/div/div/div[1]/div/div/button").click()
time.sleep(3)
# telling selenium where the list is    ISSUE IS HERE
dropdown = driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div[4]/"
                                        "div[1]/div[1]/div/div/div/div[2]")
# listing the elements in the dropdown
time.sleep(3)
dropdownDiv = dropdown.find_elements(By.TAG_NAME,"div")
time.sleep(3)
# Printing the elements and checking if they are equivalent to what we are looking for
# If they are equivalent to "Click here if your address isn't on this list" then clicking on the list
for div in dropdownDiv:
    print(div.text)
    if div.text == "Click here if your address isn't on this list":
        div.click()

# flat or apartment
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div[4]/div[1]/div["
                             "3]/div/input").send_keys('')
# House Name
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div[4]/div[1]/div["
                             "4]/div/input").send_keys('')
# House Number
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div[4]/div[2]/div[1"
                             "]/div/input").send_keys('1')
# Street
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div[4]/div[2]/div[2"
                             "]/div/input").send_keys('Vincent Avenue')
# Town or City
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div[4]/div[2]/div[4"
                             "]/div/input").send_keys('MILTON KEYNES')
# Time at address
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div[4]/div[4]/div/"
                             "div[1]/div/label[2]/button").click()
# Where are you looking to shop
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
# Selecting where to shop
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div[6]/div/div/"
                             "select").click()
time.sleep(1)
# defining the select variable as selecting an area on the webpage (can only do this when the options are in an option
# element on inspection)
select = Select(driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form"
                                             "/div[6]/div/div/select"))
# Selecting the box that says 'I want to check my eligibility'
select.select_by_visible_text('I want to check my eligibility')
time.sleep(3)
# Clicking continue to Step2
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div[7]/div[2]/div"
                             "[2]/button").click()
# Step 2
time.sleep(8)
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div[1]/div[1]/div/"
                             "div[1]/div/div[1]/label[1]/button").click()
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div[1]/div[2]/div/"
                             "div/input").send_keys('2000')
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div[1]/div[1]/"
                             "div/div[3]/div/div/input").send_keys('Snap')
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div[2]/div/div/"
                             "div/label[2]/button").click()
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div[3]/div[2]/"
                             "div[1]/div/input").send_keys('500')
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div[4]/div/div["
                             "2]/div[1]/div/div/div/input").send_keys('500')
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div[5]/div/div["
                             "1]/div/label[1]/button").click()
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div[6]/div/div["
                             "1]/div/label[1]/button").click()
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div[7]/div[2]/"
                             "button").click()
# Page 3
time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div/div[3]/div["
                             "4]/div/div[1]/button[1]").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div/div[2]/div["
                             "3]/div/div/div/div/button").click()
time.sleep(3)
# Need to enter the verification code here

for request in driver.requests:
    if "verificationCode" in request.url:
        input_string = request.response.body.decode('utf-8')
        print(input_string)
        pattern = r'{"code":"(\d{3})",'
        match = re.search(pattern, input_string)
        if match:
            driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div/"
                                          "div[2]/div[3]/div/div/div/div/input").send_keys(match.group(1))
            print(match.group(1))

# Step 3 Last Step Page
time.sleep(3)
select = Select(driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/"
                                             "div/div[2]/div[4]/div/div/div/div[1]/div/select"))
select.select_by_visible_text('What is the name of your first school?')

driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div/div[2]/div[4]/"
                             "div/div/div/div[2]/div/input").send_keys('SnapSchool')
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div/div[3]/div[2]/"
                             "div/div[2]/label").click()
driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div/div[3]/div[3]/"
                             "div/label[1]/input").click()
# Test Decision criteria

select = Select(driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/"
                                             "test-decision/div/div[1]/select"))
select.select_by_visible_text('Real Analytics Call')

driver.find_element(By.XPATH,"/html/body/div[5]/div/div/div[2]/div/div/div/div[2]/div/div/form/div/div[3]/div[4]"
                             "/div/div[2]/button").click()

for request in driver.requests:
    if "submitApplication" in request.url:
        input_string = request.response.body.decode('utf-8')
#        print(input_string)
        pattern = r'{"id":(\d{8}),'
        caid = re.search(pattern, input_string)
        pattern = r'"applicationIdString":"([^"]+)"'
        appid = re.search(pattern, input_string)
        if caid:
            print(caid.group(1))
            print(appid.group(1))
            break

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
