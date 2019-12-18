from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="G:\Multi\Swift & Python\Python\Drivers\chromedriver")
driver.get("https://www.othoba.com/")
print(driver.title)
print(driver.current_url)
#driver.get("https://www.daraz.com.bd/#")
#print(driver.title)
#time.sleep(3)
#print(driver.current_url)
#driver.back()
#print(driver.title)
#time.sleep(3)
#driver.forward()
#print(driver.title)
#driver.find_element_by_xpath("//*[@id='search-input]").send_keys("Mobile samsung")
#driver.find_element_by_xpath("//*[@id='small-search-box-algolio-form']/button/i").send_keys(Keys.ENTER)
driver.find_element_by_name("q").send_keys("Mobile")
driver.find_element_by_xpath("//*[@id='small-search-box-algolio-form']/button").click()
time.sleep(1)
driver.close()