from selenium import webdriver
import time
c_option=webdriver.ChromeOptions()
c_option.add_experimental_option("detach",True)
driver =webdriver.Chrome()
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element("id","small-searchterms").send_keys("computer")
time.sleep(2)
driver.find_element("id","login-button").click()
time.sleep(2)
title='Demo Web Shop'

demo_title=driver.title

if demo_title==driver.title:
    print('The name is correct')
else:
    print('The name is notcorrect')
driver.quit()