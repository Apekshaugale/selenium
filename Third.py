from selenium import webdriver
import time
c_option=webdriver.ChromeOptions()
c_option.add_experimental_option("detach",True)
driver =webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.get("https://www.youtube.com/")
# time.sleep(2)
# driver.maximize_window()
# time.sleep(2)
# driver.back()
# time.sleep(2)
# driver.forward()
# time.sleep(2)
# driver.refresh()
# time.sleep(2)
driver.close()

https://demowebshop.tricentis.com/