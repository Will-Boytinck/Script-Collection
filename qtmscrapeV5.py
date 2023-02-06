from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

link = "https://www.vicabc.ca/membership/member-directory/?Page=1&section_id=5428&section_copy_id=0"
current_url = link

while current_url != "https://www.vicabc.ca/membership/member-directory/?Page=58&section_id=5428&section_copy_id=0":
    xpath = '//*[@title="Go to next page"]'
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(link)
    business_domain = driver.find_elements_by_partial_link_text("www.")
    for i in range(len(business_domain)):
        print(business_domain[i].text)
    business_domain = ""
    next_link = driver.find_element_by_xpath(xpath)
    next_link.click()
    current_url = driver.current_url
    link = current_url
    driver.quit()    
    