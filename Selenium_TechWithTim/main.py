from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

#Waiting for element to exists/load completely
WebDriverWait(driver, 5).until( 
    EC.presence_of_element_located((By.CLASS_NAME,"gLFyf"))
)

input_element = driver.find_element(By.CLASS_NAME,"gLFyf")
input_element.send_keys("Tech with Tim" + Keys.ENTER) # Typing text in search box and searching.

#Waiting for element to exists/load completely
WebDriverWait(driver, 20).until( 
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"Tech with Tim"))
)
#Click on a link based on a text
link = driver.find_element(By.PARTIAL_LINK_TEXT,"Tech with Tim")
'''
    PARTIAL_LINK_TEXT  -> text present inside the link
    LINK_TEXT -> Exact match
'''
link.click()

time.sleep(10)

driver.quit()