'''
//*[@id="tabbernav2"]/li[2]/a
//*[@id="tabbernav2"]/li[3]/a
//*[@id="tabbernav2"]/li[4]/a
'''
'''
this scrapes the calgary csa
and I got to say, this code is janky but by god am I so hyped I got it too work
'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
xpath = '//*[@id="tabbernav2"]/li[2]/a'
link = "https://weblink.cgyca.com/directory/results.aspx?SearchCategories=True&SearchNames=True&SearchOnlyMembers=False&State=AB"
current_url = link
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get(link)
k = 0
temp = 2
while k != 33:
   business_domain = driver.find_elements_by_partial_link_text("Visit Site")
   for h in range(len(business_domain)):
      variable = business_domain[h]
      var2 = variable.get_attribute('href')
      print(var2)
                  
   
   xpath = xpath = '//*[@id="tabbernav2"]/li['+str(temp)+']/a'
   temp = temp + 1
   k = k + 1
   next_link = driver.find_element_by_xpath(xpath)
   next_link.click()   