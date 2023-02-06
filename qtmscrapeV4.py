# https://winnipegconstruction.ca/membership/directory/page/2/
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

# scrapes the winnipeg constructio association website
current_url = "https://winnipegconstruction.ca/membership/directory/page/2/"
i = 1
'''
THE PROBLEM:
there is not 'go to next page button', so the current url is going to need to be changed to
https://winnipegconstruction.ca/membership/directory/page/[i] in order to get all the content
'''

while current_url != "https://winnipegconstruction.ca/membership/directory/page/76/":
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(current_url)
    business_domain = driver.find_elements_by_partial_link_text("www.") # works - hacky
    # ----------------------------------------------------------------- #
    for j in range(len(business_domain)):
        print(business_domain[j].text)    
    
    business_domain = ""
    # defining url in var terms
    opening = "https://winnipegconstruction.ca/membership/directory/page/"
    page_num = 2 + i
    page_num = str(page_num) + "/"
    current_url = opening + page_num
    driver.get(current_url)
    i = i + 1
    driver.quit()
    
    


    