import re
import matplotlib.pyplot as plt
import numpy as np

lines = []
c = []
d = []
dump = open("action-report-qtm.txt", "r")
for line in dump:
    lines.append(line)
    
for line in lines:
    line = line.split()
    action_count = line[1]
    action_count = int(action_count)
    name = line[2]

    if name == "Courtenay":
        date=line[0]
        print(date)
        d.append(date)
        c.append(action_count)
        
        
j = 0
n = []
for i in range(100):
    if i % 5 == 0:
        j = j + i
        n.append(j)
        
for k in range(len(d)):
    print(d)
        
d = d[0:101]
c.reverse()
x = c
plt.xticks(x,labels=d)
plt.plot(x, label = "Courtenay")
plt.yticks(n)
plt.ylabel("action-count")
plt.legend()
plt.show()
            

    
    
 