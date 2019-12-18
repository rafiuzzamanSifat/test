from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="G:\Multi\Swift & Python\Python\Drivers\chromedriver")
driver.maximize_window()
driver.get("file:///C:/Users/rafi.sifat/Desktop/sel.html")

row= driver.find_elements(By.XPATH, "/html/body/table/tbody/tr")
column = driver.find_elements(By.XPATH, "/html/body/table/tbody/tr[1]/th")
print(len(row))
print(len(column))

for r in range(2,row+1):
   for c in range(1,column+1):
       print(driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text)
