import mysql.connector as sql
import statistics
import matplotlib.pyplot as plt
import numpy as np
"""

db = sql.connect(
    host = "localhost",
    user = "root",
    passwd = "MarinersSweet116"
    )

print (db)

mycursor = db.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
    
"""
db = sql.connect(
    host = "localhost",
    user = "root",
    passwd = "MarinersSweet116",
    database = "lahmansbaseballdb"
    )
    
mycursor = db.cursor()

mycursor.execute("select teamID, yearID, sum(salary) from salaries group by teamID, yearID order by yearID, teamID;")

sal = mycursor.fetchall()

avsal = {}
for entry in sal:
    if entry[1] not in avsal:
        avsal[entry[1]] = []
    avsal[entry[1]].append(entry[2])
    
for year in avsal:
    avsal[year] = sum(avsal[year])

#mycursor.execute("SHOW TABLES")

#for x in mycursor:
 #   print(x)
    
mycursor.execute("select yearID, teamID, playerID, salary from salaries order by yearID, teamID, salary desc;")

sal = mycursor.fetchall()

dic = {}
for item in sal:
    if item[0] not in dic:
        dic[item[0]] = {}
    if item[1] not in dic[item[0]]:
        dic[item[0]][item[1]] = []
    dic[item[0]][item[1]].append(item[3])

years = {}
      
for year in dic:
    years[year] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for team in dic[year]: 
        if len(dic[year][team]) >= 20:  
             for player in range(0,20):
                 years[year][player] += dic[year][team][player]
    r = sum(years[year])
    for entry in range(0,20):
        years[year][entry] = years[year][entry]/r

#print(dic)   
#print(years)        
#print(dic)

"""
Goddamn pivoting(sp?)
"""

ranks = {}
for rank in range(0, 20):
    ranks[rank] = []
    for year in years:
        ranks[rank].append(years[year][rank])

#print(ranks)
s = 0
for rank in ranks:
    print(len(ranks[rank]))
        
  
N = range(1985, 2017)
# This is the part where I spent 25 minutes trying to subtract 1985 from 2016
r = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for rank in ranks:
    plt.bar(N, ranks[rank], bottom = r)
    r = np.add(r, ranks[rank]).tolist()
plt.xlabel("Year")
plt.ylabel("Salary Distribution")
plt.title("Total Salary Distribution 1985 - 2016")
#plt.show()









