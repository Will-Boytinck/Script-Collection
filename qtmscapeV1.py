##########################################################################
# A simple web scraper built in python that gets company information
# of off respective websites and puts that data into an excel spread sheet
# Start Edit: May 3rd 2021 | Last Edit: N/A
# Creator: Will Boytinck | wboytinck@quotetome.com
##########################################################################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re


def page(link):
    current_url = link
    
    
   
    
    while current_url != "https://www.vicabc.ca/membership/member-directory/?Page=58&section_id=5428&section_copy_id=0":
        xpath = '//*[@title="Go to next page"]'
        
        info = []
        t = []
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        driver = webdriver.Chrome(PATH)
        driver.get(link)
        business_type = driver.find_elements_by_class_name("mb10")
        
        for i in range(len(business_type)):
            if "Business Type" in business_type[i].text:
                alist = [m.start() for m in re.finditer(r":", business_type[i].text)]
                first = alist[0]
                p = business_type[i].text
                to_append = p[first+1:]
                t.append(to_append)
                 
        business_name = driver.find_elements_by_tag_name("h3")
        del business_name[0]
        
       
        for i in range(8): # appending to two different txt documents
            names = open("names.txt", "a")
            names.write(business_name[i].text)
            names.write('\n')
            types = open("types.txt", "a")
            types.write(t[i])
            types.write('\n')
            
            
        # clicking on next button
        next_link = driver.find_element_by_xpath(xpath)
        
        next_link.click()
        current_url = driver.current_url
        link = current_url
        driver.quit()
        
        
    
    


def main():
    link = "https://www.vicabc.ca/membership/member-directory/"
    page(link)
        
        
    
    

main()