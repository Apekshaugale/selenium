from selenium import webdriver
import time
c_option=webdriver.ChromeOptions()
c_option.add_experimental_option("detach",True)
driver =webdriver.Chrome()
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()

time.sleep(2)

driver.find_element("id","small-searchtearms").send_keys("cricket")

# driver.back()
time.sleep(2)
# driver.forward()
# time.sleep(2)
# driver.refresh()
# time.sleep(2)
driver.close()


