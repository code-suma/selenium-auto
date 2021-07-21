import select
import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("C:\\External\\Suma\\SQT\\WebDrivers\\chromedriver_win32\\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")
driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")
driver.find_element_by_xpath("//input[@id='btnLogin']").click()
leave= driver.find_element_by_css_selector("#menu_leave_viewLeaveModule")
entitle= driver.find_element_by_id("menu_leave_Entitlements")
my_entitle= driver.find_element_by_css_selector("#menu_leave_viewMyLeaveEntitlements")

action= ActionChains(driver)
action.move_to_element(leave).move_to_element(entitle).move_to_element(my_entitle).click().perform()
#My leave entitlements form:
#Add:
time.sleep(5)
driver.find_element_by_xpath("//input[@id='btnAdd']").click()
#Add leave entitlement
#Add multiple employees:

driver.find_element_by_xpath("//input[@id='entitlements_filters_bulk_assign']").click()
#Location:

driver.find_element_by_css_selector("#entitlements_filters_location").click()
time.sleep(5)
driver.find_element_by_css_selector("option[value='1,2,5,-1']").click()
#Leave type
driver.find_element_by_css_selector("#entitlements_leave_type").click()
time.sleep(5)
driver.find_element_by_css_selector("select[id='entitlements_leave_type'] option[value='10']").click()
#sub unit:
driver.find_element_by_xpath("//select[@id='entitlements_filters_subunit']").click()
time.sleep(5)
driver.find_element_by_css_selector("select[id='entitlements_filters_subunit'] option[value='3']").click()
#leave period:
driver.find_element_by_id("period").click()
time.sleep(5)
driver.find_element_by_xpath("//option[@value='2021-01-01$$2021-12-31']").click()
#Entitlements:
driver.find_element_by_xpath("//input[@id='entitlements_entitlement']").send_keys("120.55")
time.sleep(5)
#save:
driver.find_element_by_xpath("//input[@id='btnSave']").click()
#Confirm:
driver.find_element_by_css_selector("#dialogConfirmBtn").click()





#leave period:
#driver.find_element_by_xpath("//select[@id='period']")






