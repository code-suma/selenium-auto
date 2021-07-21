from selenium import webdriver

driver = webdriver.Chrome("C:\External\Suma\SQT\WebDrivers\chromedriver_win32\chromedriver")
driver.get("https://www.amazon.co.uk/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element_by_id("nav-search-submit-button").click()
driver.find_element_by_id("twotabsearchtextbox").send_keys("Samsung phones")
driver.find_element_by_id("nav-search-submit-button").click()
driver.find_element_by_xpath("//span[text()='Samsung']").click()

phNames = driver.find_elements_by_xpath("//span[contains(@class,'a-size-base-plus a-color-base a-text-normal')]")

phPrices = driver.find_elements_by_xpath("//span[contains(@class, 'a-price-whole')]")

myphone=[]
myprice=[]


for phone in phNames:
    print(phone.text)
    myphone.append(phone.text)


for prices in phPrices:
    print(prices.text)
    myprice.append(prices.text)

list = zip(myphone,myprice)

for mydata in list:
    print(mydata)

driver.close()





