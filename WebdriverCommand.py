from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="G:\Multi\Swift & Python\Python\Drivers\chromedriver")

driver.get("http://newtours.demoaut.com/")

print(driver.title)
user_name=driver.find_element_by_name("userName")
print("User Name", user_name.is_displayed())
print("User Name", user_name.is_enabled())

password_name=driver.find_element_by_name("password")
print("Password", password_name.is_displayed())
print("Password", password_name.is_enabled())

user_name.send_keys("mercury")
password_name.send_keys("mercury")

Login_button=driver.find_element_by_name("login").click()

round_trip=driver.find_element_by_css_selector("input[value=roundtrip]")
print("Round Trip=", round_trip.is_selected())

oneway_trip=driver.find_element_by_css_selector("input[value=oneway]")
print("One Way trip=", oneway_trip.is_selected())

