from selenium import webdriver
import time

c_option = webdriver.ChromeOptions()
c_option.add_experimental_option("detach",True)

driver = webdriver.Chrome()

driver.get("https://money.rediff.com/losers/bse/daily/groupall")
driver.maximize_window()
time.sleep(2)


child=driver.find_element("xpath",'//*[text()="EL Forge"]/self::a')
print(child.text)
time.sleep(2)

parent=driver.find_element("xpath",'//*[text()="EL Forge"]/parent::*')
print(parent.text)
time.sleep(2)

ancestor=driver.find_elements("xpath",'//*[text()="EL Forge"]/ancestor::*')
print(len(ancestor))

ansector_child_tag=driver.find_elements("xpath",'//*[text()="EL Forge"]/ancestor::*/child::*')
print(len(ansector_child_tag))

ansector_parent_tag=driver.find_elements("xpath",'//*[text()="EL Forge"]/ancestor::*/parent::*')
print(len(ansector_parent_tag))

ansector_descendant_tag=driver.find_elements("xpath",'//*[text()="EL Forge"]/ancestor::*/descendant::*')
print(len(ansector_descendant_tag))