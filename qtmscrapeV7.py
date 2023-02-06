from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

link = "https://www.edmca.com/membership/membership-directory/"
current_url = link
k = 0
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get(link)
while k != 101:
    business_domain = driver.find_elements_by_partial_link_text("www.")
    for j in range(len(business_domain)):
        print(business_domain[j].text)      
            
    xpath = '//*[@id="memberDirectory"]/div[15]/ul/li[7]/a'
    next_link = driver.find_element_by_xpath(xpath)
    next_link.click()
    k = k + 1