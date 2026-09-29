from selenium import webdriver
import time
c_option=webdriver.ChromeOptions()
c_option.add_experimental_option("detach",True)
driver =webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element("id","user-name").send_keys("standard_user")
time.sleep(2)

driver.find_element("id","password").send_keys("secret_sauce")
time.sleep(2)


#driver.find_element(by="id",value="textarea").send_keys("Pune")
#time.sleep(2)
driver.find_element("id","login-button").click()
time.sleep(2)

title="Swag Labs"

swag_title=driver.title
if swag_title==driver.title:
    print("The title is correct.")
else:
    print("The title is not correct")