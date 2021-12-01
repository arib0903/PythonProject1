#                    PROJECT PART 1                            #


#max_value:
def max_value(data,key):
  string = ""
  for i in data:
    print(i)
    if i[key] > string: 
      string = i[key]
  return string

  
#print(max_value([{'date': '2021-02-10T00:00:00.000', 'location': 'MI'}, {'date': '2021-02-10T00:00:00.001', 'location': 'WA'}], 'date'))


#find if second parameter matches with keys in dictionary, then display the values of those keys associating the values with zero
def init_dictionary(data,key):
  newDic = {}
  for find in data: 
    for find2 in find:
      if key == find2: 
        v = find[key]
  
        newDic[v] = find['series_complete_pop_pct']

  
  return newDic

# print(init_dictionary([{'date': '01-25-2013', 'location': 'MI'},{'poop': '05-12-1923', 'location': 'NY'}],'date'))


#itterates through lod using find. gets the values of "k" and checks if "k" equals to "v". If that's true, have acc updated to the value of tgt. 
def sum_matches(lod,k,v,tgt):
  acc = 0
  for find in lod:
    if find[k] == v:
      acc += int(find[tgt])       #acc = acc + int(find[tgt])
  return acc

# print(sum_matches([{"location":"50", "NY":"100"},{"location":"50", "NY":"500"}], 'location', '50', "NY"))


#appends and prints the dictionary into the list if the value of k:v is in the original dictionary
def copy_matching(lod,k,v):
   acc = []
   for find in lod:
      if find[k] == v:
        acc.append(find)
   return acc

# print(copy_matching([{ 'date': '2021-05-02','administered_janssen': 555456, 'administered_moderna': 6733913,"location":"NY"},
