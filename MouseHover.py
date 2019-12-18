from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome (executable_path="G:\Multi\Swift & Python\Python\Drivers\chromedriver")
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.XPATH, "//*[@id='txtUsername']").send_keys("admin")
driver.find_element(By.XPATH, "//*[@id='txtPassword']").send_keys("admin123")
driver.find_element(By.XPATH, "//*[@id='btnLogin']").click()

admin=driver.find_element(By.XPATH, "//*[@id='menu_admin_viewAdminModule']/b")
user_management=driver.find_element(By.XPATH, "//*[@id='menu_admin_UserManagement']")
user=driver.find_element(By.XPATH, "//*[@id='menu_admin_viewSystemUsers']")

actions=ActionChains(driver)
actions.move_to_element(admin).move_to_element(user_management).move_to_element(user).click().perform() #Mouse Hover
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

actions.double_click(user).perform() #double click
actions.context_click(user).perform() #right click
