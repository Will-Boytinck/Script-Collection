from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

# scrapes the rural manitoban contruction associatio website
current_url = "https://www.carm.ca/?unonce=2c4ce0622b&uformid=911&s=uwpsfsearchtrg&taxo%5B0%5D%5Bname%5D=category&taxo%5B0%5D%5Bopt%5D=3&taxo%5B0%5D%5Bterm%5D=uwpqsftaxoall&taxo%5B1%5D%5Bname%5D=associates&taxo%5B1%5D%5Bopt%5D=3&taxo%5B1%5D%5Bterm%5D=uwpqsftaxoall&skeyword="

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get(current_url)
business_name = driver.find_elements_by_tag_name("h4") # working
business_domain = driver.find_elements_by_partial_link_text("www.") # works - not matched with company name but w/e
# domains make no sense how to grab
# they are each in unique div classes inside a hrefs with no definable way to capture them
for i in range(len(business_domain)):
    print(business_domain[i].text)
    



       




driver.quit()