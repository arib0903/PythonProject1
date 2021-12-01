import bottle 
import json
import processing
import os.path
import data 
import csv
def load_data( ):
   csv_file = 'saved_data.csv'
   if not os.path.isfile(csv_file):
      url = 'https://data.cdc.gov/resource/unsk-b7fc.json?$limit=50000&$where=location!=%27US%27'
      info = data.json_loader(url)
      heads = ['date','location','administered_janssen','administered_moderna','administered_pfizer','administered_unk_manuf','series_complete_pop_pct']

      data.save_data(heads, info, 'saved_data.csv')


#------------------------------------------------------------------------------#


@bottle.route('/')
def load_index():
  #runs index.html
  return bottle.static_file("index.html",root = ".")


@bottle.route('/ajax.js')
def load():
  #runs ajax.js
  return bottle.static_file("ajax.js",root = ".")


@bottle.route('/graph.js')
def load2():
  #runs graph.js
  return bottle.static_file("graph.js",root = ".")

#------------------------------------------------------------------------------#


@bottle.route('/graphBar')
def load_graph():
  #takes the data from csv file and stores it as dict
  lisOfDic = data.load_data('saved_data.csv')
  #maxVal is the max date value from the dict -lisofDic-
  maxVal= processing.max_value(lisOfDic,'date') 
  #ex returns a list of dictionaries with the max date(line 2-64)
  ex = processing.copy_matching(lisOfDic,'date',maxVal)
  #returns list of dictionaries with location as key and series_complete_pop_pct as value in a JsonBlob
  updated = processing.init_dictionary(ex,'location')
  JsonBlob = json.dumps(updated)
  return JsonBlob


#------------------------------------------------------------------------------#


def convert_to_Json(x,y):
  dic = {}
  for find in range(len(x)):
    dic[x[find]] = y[find]
  JsonBlob = json.dumps(dic)
  return JsonBlob


@bottle.route('/graphPie')
def load_pie():
  lisOfDic = data.load_data('saved_data.csv')
  # print(lisOfDic)

  maxVal= processing.max_value(lisOfDic,"date") 
  ex = processing.copy_matching(lisOfDic,'date',maxVal)

  sumAJ = json.dumps(processing.sum_matches(ex,'date',maxVal,'administered_janssen'))

  sumAM = json.dumps(processing.sum_matches(ex,'date',maxVal,'administered_moderna'))

  sumAP = json.dumps(processing.sum_matches(ex,'date',maxVal,'administered_pfizer'))

  sumAU = json.dumps(processing.sum_matches(ex,'date',maxVal,'administered_unk_manuf'))

  lis = ['Janssen','Moderna','Pfizer','Unknown']

  #this is the sum of the shit in strings
  lis2 = [sumAJ,sumAM,sumAP,sumAU]

  # returns a JsonBlob dictionary with the lis as key and lis2 as value
  return convert_to_Json(lis,lis2)




#------------------------------------------------------------------------------#

def sort(dic):
  return dic['date']

def actualSort(fullDic):
  fullDic.sort(key = sort)
  return fullDic


@bottle.post('/graphLine')
def load_line():
  lisOfDic = data.load_data('saved_data.csv')

  jsonBlob = bottle.request.body.read().decode()
  content = json.loads(jsonBlob)
  ex = processing.copy_matching(lisOfDic,'location',content['location'])

  sortedDic = actualSort(ex)
  lis = []
  lis2 = []
  for find in sortedDic:
    lis.append(find['date'])
    lis2.append(find['series_complete_pop_pct'])

  return convert_to_Json(lis,lis2) 

  
load_data()
load_graph()
load_pie()


bottle.run(host = '0.0.0.0', port = 8080,debug = True)
