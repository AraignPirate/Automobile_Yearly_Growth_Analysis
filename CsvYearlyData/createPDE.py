import random
import os
import sqlite3
import csv
files = ["ThreeWheelers.csv","Multiutility.csv","CommercialVehicals.csv","PassengersVehicals.csv","TwoWheelers.csv"]
price='PriceOverallAvg.csv'
three=[]
multi=[]
comm=[]
passen=[]
two=[]
pricelist=[]
globallist=[three,multi,comm,passen,two]
def createPDE():
  global files
  global globallist
  start = int(input("Start Year : "))
  stop = int(input("stop year : "))
  with open("ProDomSalesExport.csv","w") as file:
    file.write("Year,Production,Sales,Exports\n")
    for i in range(start,stop+1):
      pro = random.randint(700000,1500000)
      dom = pro - random.randint(300000,500000)
      exp = pro - dom - random.randint(100,1000)
      file.write(f"{start},{pro},{dom},{exp}\n")
      top5 = givesplitted(pro)
      for i in range(0,5):
        updatelist(start,top5[i],globallist[i])
      pricelist.append([start,pro*300000,dom*400000,exp*500000])
      start += 1
  for i in range(0,5):
    with open(files[i],"w") as file:
      file.write("Year,Production,Sales,Exports\n")
      for data in globallist[i]:
        file.write(f"{data[0]},{data[1]},{data[2]},{data[3]}\n")
  with open(price,'w') as file:
    file.write("Year,Production,Sales,Exports\n")
    for data in pricelist:
      file.write(f"{data[0]},{data[1]},{data[2]},{data[3]}\n") 
def decompose(i):
  while i > 0:
    n = random.randint(1,i)
    yield n
    i -= n

def givesplitted(n):
  while True:
    hey = list(decompose(n))
    if len(hey) == 15:
      #print(hey)
      top5 = hey[:5]
      rest = hey[5:]
      #print(top5)
      #print(sum(rest))
      intt = random.randint(0,4)
      top5[intt] += sum(rest)
      #print(top5)
      #print(sum(top5))
      return top5
      break
def updatelist(year,pro,listt):
  dom = pro - (pro//random.randint(3,4))
  exp = pro - dom
  listt.append([year,pro,dom,exp])



TABLENAMES = []
FILENAMES = []

DBNAME = "YearlyData.db"

class Dbhelper():
  global TABLENAMES, FILENAMES
  def __init__(self):
    file , tables = self.getTableNames()
    self.deleteTables(tables)
    self.createTables(tables,file)
  def getTableNames(self):
    txt = os.listdir()
    for name in txt:
      if name[-3:] == "csv":
        TABLENAMES.append(name[:-4])
        FILENAMES.append(name)
    return FILENAMES , TABLENAMES
  def deleteTables(self,tables):
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    for table in tables:
      cursor.execute(f"DROP TABLE IF EXISTS {table};")
    #print("TABLE DROPED")
    conn.commit()
    cursor.close()
    conn.close()
  def createTables(self,tables,files):
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    if len(tables) == len(files):
      for index in range(0,len(tables)):
        with open(files[index],newline='') as f:
          #print(files[index])
          data = csv.reader(f)
          listt = next(data)
          listdata = list(data)
          #print(listt)
          cursor.execute(f"CREATE TABLE {tables[index]} ( {listt[0]} INT,{listt[1]} INT,{listt[2]} INT, {listt[3]} INT)")
          for csvd in listdata:
            cursor.execute(f"insert into {tables[index]} ({listt[0]},{listt[1]},{listt[2]},{listt[3]}) values ({csvd[0]},{csvd[1]},{csvd[2]},{csvd[3]})")
    print("Created Table")
    conn.commit()
    cursor.close()
    conn.close()







createPDE()
Dbhelper()
print(f"MOVE {DBNAME} to DATABASE DIRECTORY")
