import json
from pprint import pprint
json_data=open('2014.json')

data = json.load(json_data)
pprint(data)
for prop in data:
	print data[prop]["short_name"]
json_data.close()