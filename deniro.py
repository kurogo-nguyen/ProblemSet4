import csv
import json

data=csv.DictReader(open ("deniro.csv"), delimiter=',')
newDict={}

for x in data:
    yearAnhScore={}
    yearAnhScore['score']= x.get(' "Score"')
    yearAnhScore['year']=x.get('Year')
    title=x.get(' "Title"').strip(' "')
    newDict[title]=yearAnhScore
formatted_obj=json.dumps(newDict, indent=4)
with open('deniro_json.txt', mode='w') as outfile:
        outfile.write(formatted_obj)
