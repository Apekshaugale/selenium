from selenium import webdriver
import time

#to select methods from selenium we need to import webdriver module from selenium package.

#to sleect methods from chrome we need chromeoptiokns module from webdriver module.
c_option = webdriver.ChromeOptions()

#detch is uded to keep the browser open after the execution of the script.
#add_experimental_option is used to add the experimental option to the chrome browser.
c_option.add_experimental_option("detach",True)

driver = webdriver.Chrome()

driver.get("https://money.rediff.com/sectors")
driver.maximize_window()
time.sleep(2)


child=driver.find_element("xpath",'//*[text()="BSE Oil & Gas"]/self::a')
print(child.text)
time.sleep(2)

parent=driver.find_element("xpath",'//*[text()="BSE Oil & Gas"]/parent::*')
print(parent.text)
time.sleep(2)

ancestor=driver.find_elements("xpath",'//*[text()="BSE Oil & Gas"]/ancestor::*')
print(len(ancestor))

ansector_child_tag=driver.find_elements("xpath",'//*[text()="BSE Oil & Gas"]/ancestor::*/child::*')
print(len(ansector_child_tag))

ansector_parent_tag=driver.find_elements("xpath",'//*[text()="BSE Oil & Gas"]/ancestor::*/parent::*')
print(len(ansector_parent_tag))

ansector_descendant_tag=driver.find_elements("xpath",'//*[text()="BSE Oil & Gas"]/ancestor::*/descendant::*')
print(len(ansector_descendant_tag))