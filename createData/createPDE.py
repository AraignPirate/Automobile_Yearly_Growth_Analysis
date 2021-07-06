import random
files = ["ThreeWheelers.csv","Multiutility.csv","CommercialVehicals.csv","PassengersVehicals.csv","TwoWheelers.csv"]
three=[]
multi=[]
comm=[]
passen=[]
two=[]
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
      start +=1 
  for i in range(0,5):
    with open(files[i],"w") as file:
      file.write("Year,Production,Sales,Exports\n")
      for data in globallist[i]:
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

print("Please Use createPDE.py present in CsvYearlyData Directory")
