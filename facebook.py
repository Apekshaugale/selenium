from selenium import webdriver
import time

c_option=webdriver.ChromeOptions()
c_option.add_experimental_option("detach",True)
driver =webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()


time.sleep(2)
driver.find_element("id","name").send_keys("apeksha")
time.sleep(2)