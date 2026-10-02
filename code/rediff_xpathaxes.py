from selenium import webdriver
import time

c_option = webdriver.ChromeOptions()
c_option.add_experimental_option("detach",True)

driver = webdriver.Chrome()

driver.get("https://money.rediff.com/gainers/bse/daily/groupall")
driver.maximize_window()
time.sleep(2)


#here child is a variable which is storing the element of anchor tag which is having text as "Thomas Scott (India)" 
#we use self::a to get the anchor tag of the element which is stored in child variable.
#a stands for anchor tag and self is used to get the current element which is stored in child variable.
#in place of a we can use * if we don't know the tahgname of the element which is stored in child variable.
child=driver.find_element("xpath",'//*[text()="Thomas Scott (India)"]/self::a')
print(child.text)
time.sleep(2)


parent=driver.find_element("xpath",'//*[text()="Thomas Scott (India)"]/parent::*')
print(parent.text)
time.sleep(2)



ansector=driver.find_elements("xpath",'//*[text()="Thomas Scott (India)"]/ancestor::*')
print(len(ansector))

# # for i in ansector:
# #     print(i.text)      #//*[text()="Thomas Scott (India)"]/ancestor::*/parent::*

# ancsector_parent_tag=driver.find_elements("xpath",'//*[text()="Thomas Scott (India)"]/ancestor::*/parent::*')
# print(len(ancsector_parent_tag))

ansector_child_tag=driver.find_elements("xpath",'//*[text()="Thomas Scott (India)"]/ancestor::*/child::*')
print(len(ansector_child_tag))

ansector_descendant_tag=driver.find_elements("xpath",'//*[text()="Thomas Scott (India)"]/ancestor::*/descendant::*')
print(len(ansector_descendant_tag))

ansector_parent_tag=driver.find_elements("xpath",'//*[text()="Thomas Scott (India)"]/ancestor::*/parent::*')
print(len(ansector_parent_tag))


child=driver.find_element("xpath",'//*[text()="EL Forge"]/self::a')
print(child.text)
time.sleep(2)