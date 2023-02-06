from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
t = True
k = 0
i = 0
link = "http://www.rdca.ca/membership/directory/"
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get(link)
xpath = '//*[@id="w2dc-controller-e5d47824e4fcfb7ab0345a0c7faaa5d2"]/div/div[3]/ul/li[11]/a'
while k != 22:
    business_domain = driver.find_elements_by_partial_link_text("view our site")
    for h in range(len(business_domain)):
        variable = business_domain[h]
        var2 = variable.get_attribute('href')
        print(var2)
    k = k + 1
    next_link = "http://www.rdca.ca/membership/directory/page/" + str(2 + i) + "/"
    driver.get(next_link)
    i = i + 1
    business_domain = ""
    variable = ""
    var2 = ""

