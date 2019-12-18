from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="G:\Multi\Swift & Python\Python\Drivers\chromedriver")
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Windows.html")
time.sleep(2)

driver.find_element(By.XPATH, "//*[@id='Tabbed']/a/button").click()

print(driver.current_window_handle) #parents handler value

a=driver.window_handles

for handle in a:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title=='Sakinalium | Home':
        driver.close()
        time.sleep(5)
driver.quit()

