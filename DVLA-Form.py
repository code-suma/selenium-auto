from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome("C:\External\Suma\SQT\WebDrivers\chromedriver_win32\chromedriver.exe")


driver.get("https://forms.dft.gov.uk/order-dvla-forms/")
driver.maximize_window()
driver.find_element_by_name("input_1").send_keys("R****")
#Address line 1
driver.find_element_by_name("input_10").send_keys(" *******entre")
#ADDRESS LINE 2
driver.find_element_by_name("input_43").send_keys("Regency Road")
# Town
driver.find_element_by_name("input_4").send_keys("How")
#cOUNTRY


driver.find_element_by_name("input_9").send_keys("UK")
#POSTCODE
driver.find_element_by_name("input_5").send_keys("****D")
#tickbox
time.sleep(5)
driver.find_element_by_xpath("//input[@id='choice_23_42_1']").click()
#submit button
driver.find_element_by_xpath("//input[@id='gform_submit_button_23']").click()

#driver.find_elements_by_class_name("choice_23_42_1").click()





