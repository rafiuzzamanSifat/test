from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="G:\Multi\Swift & Python\Python\Drivers\chromedriver")
driver.maximize_window()

driver.get("https://www.sic-info.org/en/services/lending/national-flags/")

#driver.find_element(By.XPATH, "//*[@id='cb1']/input").send_keys("superadmin")
#driver.find_element(By.XPATH, "//*[@id='password']").send_keys("123456")
#driver.find_element(By.XPATH, "/html/body/div/div/form/div[3]/button").click()

#driver.execute_script("window.scrollBy(0,1000)", "")

#element = driver.find_element_by_xpath("//*[@id='mainInner']/section/div/ul[6]/li[7]/img")
#driver.execute_script("arguments[0].scrollIntoView();", element)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")