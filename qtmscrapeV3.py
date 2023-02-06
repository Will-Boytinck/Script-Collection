from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re


# https://www.vicabc.ca/membership/member-directory/?Page=4&section_id=5428&section_copy_id=0
# scrapest the vancouver island construction association
current_url = "https://www.vicabc.ca/membership/member-directory/?Page=4&section_id=5428&section_copy_id=0"

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get(current_url)
business_domain = driver.find_elements_by_partial_link_text("www.") # works - not matched with company name but w/e

for i in range(len(business_domain)):
    print(business_domain[i])