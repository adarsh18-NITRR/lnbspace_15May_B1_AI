# day 8 
# working with csv and json files

# import csv
# f = open(r'E:\python PROJECTS\Projects\Techchinest - AI course\Branch Specific\Day 8\data\1.csv','r')
# print(f.read(),end='\n')
# f.close()

import json
f = open(r'E:\PYTHON\Projects\Techchinest - AI course\Branch Specific\Day 8\data\2.json','r')
d = json.load(f)
print(type(d))
print(d)
f.close()
