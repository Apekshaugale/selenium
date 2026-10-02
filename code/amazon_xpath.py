from selenium import webdriver
import time
c_option=webdriver.ChromeOptions()

c_option.add_experimental_option("detach",True)
driver =webdriver.Chrome(options=c_option)
driver.get("https://www.amazon.in")
driver.maximize_window()
time.sleep(2)


driver.find_element("xpath",'//input[@type="text" or @id="twotabsearchtextbox"]').send_keys("laptop")
time.sleep(2)

driver.find_element("xpath",'//input[@type="submit" or @id="nav-search-submit-button"]').click()
time.sleep(2)

 