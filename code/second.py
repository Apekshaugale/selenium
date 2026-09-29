from selenium import webdriver
c_option=webdriver.ChromeOptions()
c_option.add_experimental_option("detach",True)
driver =webdriver.Chrome()
driver.get("https://www.youtube.com/")
driver.close()