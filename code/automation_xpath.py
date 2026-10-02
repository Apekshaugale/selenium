from selenium import webdriver
import time
c_option=webdriver.ChromeOptions()

c_option.add_experimental_option("detach",True)
driver =webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)

#or= //tagname[@attribute1name='attributevalue' or @attribute=2name='attributevalue']
driver.find_element("xpath",'//input[@class="form-control" or @id="name"]').send_keys("Apeksha")
time.sleep(2)

#or= //tagname[@attribute1name='attributevalue' and @attribute=2name='attributevalue']
driver.find_element("xpath",'//input[@id="email" and @type="text"]').send_keys("apeksha@gamil.com")
time.sleep(2)

#contains=  //tagname[contains(@attribute,value-attribute)]
driver.find_element("xpath",'//input[contains(@id,"phone")]').send_keys("9325461213")
time.sleep(2)

# when we don't know the tagname we use * inplace of tagname
# driver.find_element("xpath",'//*[contains(@id,"phone")]').send_keys("9325461213")
# time.sleep(2)

#startswith = //tagname[starts-with(@attribute,partial_value)]
driver.find_element("xpath",'//textarea[starts-with(@id,"textarea")]').send_keys("Pune")
time.sleep(2)


#text()  = //tagname[text()='value'] 
#text is used when there is anchor tag .
# 
# 






# driver.find_element("xpath",'//input[text()="female"]').click()
# time.sleep(2)


driver.find_element("xpath",'//input[starts-with(@id,"female")]').click()
time.sleep(2)