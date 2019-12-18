from selenium import webdriver

driver = webdriver.Chrome(executable_path="G:\Multi\Swift & Python\Python\Drivers\chromedriver")

driver.get("http://newtours.demoaut.com/")

driver.implicitly_wait(3)

assert "Welcome: Mercury Tours" in driver.title

username= driver.find_element_by_name("userName")

username.is_selected()
username.is_enabled()

username.send_keys("mercury")

driver.find_element_by_name("password").send_keys("mercury")

driver.find_element_by_name("login").click()