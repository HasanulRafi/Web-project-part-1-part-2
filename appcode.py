import csv

def filterIn(Rafi, Sani, Ador):
  num = []
  for i in Rafi:
    if i[Sani] == Ador:
      num.append(i)
  return num

#print(filterIn(data, 'aptype', 'REPAIR'))




def filterOut(Rafi, Sani, Ador):
  num = []
  for i in Rafi:
    if i[Sani] != Ador:
      num.append(i)
  return num

#print(filterOut(data, 'aptype', 'REPAIR'))




def filterInRange(data, keynumber, low, high):
  num = []
  for i in data:
    if low <= float(i[keynumber]) and float(i[keynumber]) < high:
      num.append(i)
  return num

#print(filterInRange(data,'value', 0, 8000))




def filterByMonth(data, month):
  num = []
  for i in data:
    date = i['issued']
    if int(date.split('-')[1]) == month:
      num.append (i)
  return num

#print(filterByMonth(data,9))


def filterByYear(data, year):
  num = []
  for i in data :
    x = i['issued']
    if int(x.split('-')[0])==year:
      num.append(i)
  return num  

#print(filterByYear(data,2019))

#1
def makeDictionary(x,y):
  new = {}
  n = 0
  for i in x:
    new[i] = y[n]
    n = n + 1
  return new
#print(makeDictionary(['apno','value'],['REP-12','450']))




#2
import csv
def readDataFromCSVFile(x):
  lst=[]
  new=[]
  hr=[]
  with open(x, newline='', encoding= "utf-8") as g:
    reader=csv.reader(g)
    headerRow = True
    for line in reader:
      y={}
      if headerRow:
        hr = line
        headerRow = False
      else:
        for i in range(len(hr)):
          y[hr[i]]=line[i]
        lst.append(y)
  return lst




#3
y = {'apno': 'ELEC-72', 'value': '2000'}
def dictionaryToListOfValues(x,y):
  new = []
  for k in x:
    new.append(y[k])
  return new






#4
import csv
def writeDataToCSVFile(a,b,c,d):
  with open(a,"w") as g:
    writer = csv.writer(g)
    if d == True:
      writer.writerow(c)
    for line in b:
      writer.writerow(dictionaryToListOfValues(c,line))


import os.path
import urllib.request
import urllib.parse
def loadData(filenameRoot, howMany):
   csvFile = filenameRoot
   if not os.path.isfile(csvFile):
       params = urllib.parse.urlencode({"$limit":howMany})
       uri = "https://data.buffalony.gov/resource/9p2d-f3yt.json?%s" % params
       response = urllib.request.urlopen(uri)
       content_string = response.read().decode()
       content = json.loads(content_string)
       writeDataToCSVFile(csvFile,content,['apno','aptype','issued','value'],True)
 
loadData("permitData.csv", 5000)




'''def scattergraph():
  b=[]
  data2=readDataFromCSVFile('permitData.csv')
  for n in range(2008,2020):
    dictionaries1=filterByYear(data2,n)
    c=[]
    for n in dictionaries1:
      low = filterInRange(dictionaries1, "value", 0)

      total = 0 
      for i in low:
        for n in i.values():
          total=total + float(n)
          c.append(total)
          med = filterInRange(dictionaries1, 'value', 500, 50000)
          count=0'''
