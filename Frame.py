from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="G:\Multi\Swift & Python\Python\Drivers\chromedriver")
driver.maximize_window()
driver.get("https://selenium.dev/selenium/docs/api/java/index.html")

driver.switch_to.frame("packageListFrame")
driver.find_element(By.XPATH, "/html/body/div[2]/ul/li[5]/a").click()
time.sleep(3)

driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")
driver.find_element(By.XPATH, "/html/body/div/ul[1]/li[10]/a/span").click()
time.sleep(3)

driver.switch_to.default_content()

driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH,"/html/body/div[1]/ul/li[5]/a").click()
time.sleep(3)

