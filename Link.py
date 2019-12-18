from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome (executable_path="G:\Multi\Swift & Python\Python\Drivers\chromedriver")

driver.maximize_window()

driver.get("http://newtours.demoaut.com/")

links= driver.find_elements(By.TAG_NAME,"a") # link count
print(len(links))

for link in links:
    print(link.text) #link extract

register = driver.find_element(By.LINK_TEXT,"REGISTER").click()
time.sleep(2)
driver.back()
register = driver.find_element(By.PARTIAL_LINK_TEXT,"CON").click()
time.sleep(2)
driver.back()
driver.close()