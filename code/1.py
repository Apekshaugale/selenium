# 

#locaters
from selenium import webdriver
import time

c_option=webdriver.ChromeOptions()

c_option.add_experimental_option("detach",True)#to pass value 

driver =webdriver.Chrome(options=c_option)#object creation


driver.get("https://demowebshop.tricentis.com/")#linked to url
time.sleep(2)

driver.maximize_window()#to maxmiized the screen
time.sleep(2)


driver.find_element("class name","ico-register").click()
time.sleep(2)

# driver.find_element("Partial Link text","Reg").click()
# time.sleep(2)





driver.find_element("id","gender-female").click()
time.sleep(2)

driver.find_element("id","FirstName").send_keys("Apeksha")
time.sleep(2)