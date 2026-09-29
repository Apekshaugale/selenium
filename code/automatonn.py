from selenium import webdriver
import time
c_option=webdriver.ChromeOptions()
c_option.add_experimental_option("detach",True)
driver =webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
#   by usng css tag                using id=nmae
driver.find_element("css selector","#name").send_keys("Apeksha")
time.sleep(2)

driver.find_element("css selector","#email").send_keys("apeksha@gmial.com")
time.sleep(2)

driver.find_element("css selector","#phone").send_keys("9322458679")
time.sleep(2)

driver.find_element("css selector","#textarea").send_keys("Pune")
time.sleep(2)

driver.find_element("css selector","#female").click()
time.sleep(2)

driver.find_element("css selector","#monday").click()
time.sleep(2)

driver.find_element("css selector","#country").send_keys("india")
time.sleep(2)

driver.find_element("css selector","#colors").send_keys("blue")
time.sleep(2)

driver.find_element("css selector","#datepicker").send_keys("23/09/2026")
time.sleep(2)

driver.find_element("css selector","input-.submit-btn").click()
time.sleep(2)
