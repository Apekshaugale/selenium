#Automation Testing Practice

from selenium import webdriver
import time
c_option=webdriver.ChromeOptions()
c_option.add_experimental_option("detach",True)
driver =webdriver.Chrome()
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element("id","name").send_keys("Apeksha Ugale")
time.sleep(2)

driver.find_element("id","email").send_keys("apeksha@gmail.com")
time.sleep(2)

driver.find_element("id","phone").send_keys("1234567890")
time.sleep(2)

driver.find_element("id","textarea").send_keys("Pune")
time.sleep(2)
#driver.find_element(by="id",value="textarea").send_keys("Pune")
#time.sleep(2)
driver.find_element("id","female").click()
time.sleep(2)

driver.find_element("id","friday").click()
time.sleep(2)

driver.find_element("id","country").send_keys("India")
time.sleep(2)

driver.find_element("id","colors").send_keys("Blue")
time.sleep(2)

driver.find_element("id","animals").send_keys("Cat")
time.sleep(2)

driver.find_element("id","datepicker").send_keys("03/03/2019")
time.sleep(2)

driver.find_element("id","txtdate").send_keys("02/12/2019")
time.sleep(2)