import bottle
import json
import appcode
import os
import os.path
import csv
import urllib.request
import urllib.parse
import parse

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


def bargraph():
  y = []
  data = readDataFromCSVFile('permitData.csv')
  for i in range(1,13):
    count = 0
    dictionaries = filterByMonth(data,i)
    for n in dictionaries:
      count = count + 1
    y.append(count)
  return y



def linegraph():
  a = []
  data1 = readDataFromCSVFile('permitData.csv')
  for n in range(2008,2020):
    count = 0
    dictionaries1 = filterByYear(data1,n)
    for h in dictionaries1:
        count = count+1
    a.append(count)
  return a



@bottle.route('/')
def router1():
  return bottle.static_file("project.html",root = '')
@bottle.route('/frontend.js')
def router2():
  return bottle.static_file('project.js',root = '')
@bottle.route('/bargraph')
def router3():
  return json.dumps(bargraph())
@bottle.route('/linegraph')
def router4():
  return json.dumps(linegraph())
#@bottle.route('/scattergraph')
#def router5():
# return json.dumps(scattergraph())

bottle.run(host = '0.0.0.0', port = 8080, debug = True)