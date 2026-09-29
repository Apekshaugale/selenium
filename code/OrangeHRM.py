from selenium import webdriver
import time
c_option=webdriver.ChromeOptions()
c_option.add_experimental_option("detach",True)
driver =webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)

#replace space with .

driver.find_element("name","username").send_keys("Admin")
time.sleep(2)

driver.find_element("name","password").send_keys("admin123")
time.sleep(2)

driver.find_element("class name","oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button").click()
time.sleep(2)

# #given title
# title="OrangeHRM"
# #original title =given title

# org_title=driver.title

# if title== org_title:
#     print("The title is correct")
# else:
#     print("The title is not correct")


# driver.quit()

#to find total number of links there in the webpage a locater which is find

links=driver.find_elements("tag name","a")
print(len(links))
driver.quit()