from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome (executable_path="G:\Multi\Swift & Python\Python\Drivers\chromedriver")

driver.implicitly_wait(3)

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()

input_field  = driver.find_elements(By.CLASS_NAME,'text_field')
print(len(input_field))

driver.find_element(By.ID, 'RESULT_TextField-1').send_keys('Abdul')

driver.find_element(By.ID, 'RESULT_TextField-2').send_keys('malik')

driver.find_element(By.ID, 'RESULT_TextField-3').clear()
driver.find_element(By.ID, 'RESULT_TextField-3').send_keys('+8801700878653')

driver.find_element(By.ID, 'RESULT_TextField-4').send_keys('Canada')

driver.find_element(By.ID, 'RESULT_TextField-5').send_keys('vancubar')

driver.find_element(By.ID, 'RESULT_TextField-6').send_keys('mail@malik.com')

driver.find_element(By.ID, 'RESULT_TextField-10').clear()
driver.find_element(By.ID, 'RESULT_TextField-10').send_keys('1/2/2020')

driver.find_element(By.ID, 'RESULT_TextArea-12').send_keys('Python Selenium')
#time.sleep(2)

#wait= WebDriverWait(driver,5)
#element=wait.until(Ec.element_to_be_clickable((By.XPATH,'//*[@id="q26"]/table/tbody/tr[1]/td/label')))
#element.click()
#time.sleep(2)

radio=driver.find_element(By.XPATH,'//*[@id="q26"]/table/tbody/tr[1]/td/label').is_selected()
print(radio)

driver.find_element(By.XPATH,'//*[@id="q26"]/table/tbody/tr[1]/td/label').click()

radio1=driver.find_element(By.XPATH,'//*[@id="q26"]/table/tbody/tr[1]/td/label').is_selected()
print(radio1)

driver.find_element(By.XPATH, '//*[@id="q15"]/table/tbody/tr/td[1]/label').click()
driver.find_element(By.XPATH,'//*[@id="q15"]/table/tbody/tr/td[7]/label').click()

contact=Select(driver.find_element_by_id("RESULT_RadioButton-9"))

contact.select_by_index(2)
#contact.select_by_visible_text("Morning")
contact.select_by_value("Radio-1")
print(len (contact.options))

a= contact.options
for option in a:
    print(option.text)


