from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

facebook = "https://www.facebook.com/"
emails = ["<your_email>"]
passwords = ["<your_password>"]

options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")  # disable notifications

driver = webdriver.Chrome('/Users/rajdeep/chromedriver',
                          options=options)  # path to chromedriver
driver.maximize_window()
driver.get(facebook)  # go to facebook.com
time.sleep(3)

email = driver.find_element_by_id('email')
email.send_keys(emails[0])
password = driver.find_element_by_id('pass')
password.send_keys(passwords[0])
driver.find_element_by_id('loginbutton').click()  # login
time.sleep(3)

print("Login Successful")

driver.get(facebook + 'events/birthdays/')
time.sleep(3)

feed = 'Happy Birthday!'  # birthday wish message
elements = driver.find_elements_by_tag_name("textArea")

if elements != []:
    cnt = 0
    for el in element:
        print("inside loop")
        cnt += 1
        element_id = str(el.get_attribute('id'))
        print("got element id")
        XPATH = '//*[@id ="' + element_id + '"]'
        post_field = driver.find_element_by_xpath(XPATH)
        print("got post_field")
        post_field.send_keys(feed)
        post_field.send_keys(Keys.RETURN)
        print("Birthday Wish posted for friend " + str(cnt))
else:
    print("None of your friends have a birthday today.")

driver.get(facebook)
time.sleep(5)
driver.find_element_by_id('pageLoginAnchor').click()
time.sleep(5)
driver.find_element_by_link_text('Log Out').click()
time.sleep(5)

driver.close()
