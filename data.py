
#                    PROJECT PART 2                            #


#These dictionaries' keys will come from the first parameter and the values will be from an entry in the second parameter. The key list and the entries in each value list parallel each other: the entry at index 0 of the first parameter will be associated with the entry at index 0 in each list in the second parameter; the entry at index 1 in the first parameter will be associated with the entry at index 1 in each list in the second parameter; and so on
def mlist(lisOfString,lisOfLisOfString):
  d1 = {}
  for index in range(len(lisOfString)):
      d1[lisOfString[index]] = lisOfLisOfString[index]

      #lis.append(d1)
  return d1

def dic_list_gen(data,data2):
  lis = []
  for subList in data2:
    y = mlist(data,subList)
    lis.append(y)
  return lis

# print(dic_list_gen(['Second'], [['Example'],['Also fake']]))
# print(dic_list_gen(['Example','Other lengths'],[['Made-Up','Possible'],['a','p']]))



#                     PART B                           #
#Define a function named read_values with one parameter. The parameter will be the name of a CSV file to read (a string). The function should return a list. This list will contain a list for each non-header row in the file. You can assume the file will have a header row and at least 1 non-header row.

import csv
def read_values(filename):
  lis = []
  with open(filename) as f:
    r= csv.reader(f)
    next(r)
    for find in r:
      # print(find)
      lis.append(find)
  return lis
# print(read_values("demo.csv"))


#                     PART C                           #

# print(make_lists(['Hint', 'Num'],[{'Hint': 'Length 2 Not Required','Num' : 8675309},
#            {'Num': 1, 'Hint' : 'Use 1st param order'}]))


#                     PART D                           #

def write_values(filename,lisoflis):
  with open(filename, 'a') as f:
      writer = csv.writer(f)
      for find in lisoflis:
        # print(find)
        writer.writerow(find)
    




#                    PROJECT PART 3                            #

#Define a function named json_loader. This function's only parameter will be a string storing the URL we wish to load. Your function must read the JSON blob stored at that URL. It should return that result of converting that blob into usable Python data.

import urllib.request
import json
import csv
def json_loader(url):
  response =  urllib.request.urlopen(url)
  content = response.read().decode()
  readableToPython = json.loads(content)
  return readableToPython

#print(json_loader("https://cse.buffalo.edu/~mhertz/courses/cse115/projects/smallFile.json"))

def make_values_numeric(LisOfKeys,dic):
  for find in LisOfKeys:
    if find in dic:
      val = float(dic[find])
      dic[find] = val
  return dic    

  

#print(make_values_numeric(['number','n2'], {'name' : 'ValJean', 'number' : '24601','n2': '430.31'}))

def make_lists(KeyString,lisOfDict):
  lis = []
  for find in lisOfDict:
    lis2 = []
    for find2 in KeyString:
      x = find[find2]
      lis2.append(x)
    lis.append(lis2)
  return lis

def save_data(keys, data, filename):
  with open(filename,'w') as f:
    writer = csv.writer(f)
    x = make_lists(keys,data)
    x.insert(0,keys)
    
    for find3 in x:
      writer.writerow(find3)   




def load_data(filename):
  lst = []
  with open(filename) as f:
    r= csv.reader(f)
    header = next(r)
    for line in r:
      dic = {}
      for i in range(len(line)):
        dic[header[i]] = line[i]
      lst.append(dic)
        #print(line)
    return lst
    

    #dic[find2] = find
  #return dic

#print(load_data('sample.csv'))
