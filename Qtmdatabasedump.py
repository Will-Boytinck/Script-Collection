import re
lines = []
company_list = []
contact_list = []
rfm_list = []
viable_list = ["gmail.com", "hotmail.com", "shaw.ca", "outlook.com", "yahoo.ca", "yahoo.com", "telus.net", "user.com", "13.ca", "live.com", "hotmail.ca", "quotetome.com", "quotetome.ca"]
dump = open("Qtmdatabasedump.txt", "r")
for line in dump:
    lines.append(line)

for each_line in lines:
    #print(each_line) # data is transfered over properly
    alist = [m.start() for m in re.finditer(r";", each_line)]
    fourth = alist[3]
    fifth = alist[4]    
    iso = each_line[fourth+1:fifth] # works
    contact_list.append(iso)
    # isolating company domain
    blist = [m.start() for m in re.finditer(r"@", iso)]
    only = blist[0]
    company_domain = iso[only+1:]
    #print(company_domain) # works
    if company_domain not in viable_list:
        if company_domain not in company_list:
            company_list.append(company_domain)


for aline in company_list:
    print(aline)
   
for bline in contact_list:
    alist = [m.start() for m in re.finditer(r"@", bline)]
    only = alist[0]
    temp = bline[only+1:]
    if temp not in viable_list:
        rfm_list.append(bline)
#for cline in rfm_list:
    #rint(cline)
        
        