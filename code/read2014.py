import json
import csv
import re

json_data=open('2014.json')
data = json.load(json_data)

counties = ["Alameda", "Butte" , "Contra Costa", "El Dorado", "Fresno",
"Humboldt", "Imperial", "Kern", "Kings", "Lake", "Los Angeles", "Madera",
"Marin", "Mendocino", "Merced", "Monterey", "Napa", "Nevada", "Orange",
"Placer", "Riverside", "Sacramento", "San Bernardino", "San Diego",
"San Francisco", "San Joaquin", "San Luis Obispo", "San Mateo",
"Santa Barbara", "Santa Clara", "Santa Cruz", "Shasta", "Solano", "Sonoma",
"Stanislaus", "Sutter", "Tulare", "Ventura", "Yolo", "Yuba"]

percent_data = {}
total_data = {}

for county in counties:
    percent_data[county] = {}
    total_data[county] = {}

with open('2014BallotMod.csv', 'wb') as file:
    writer = csv.writer(file)
    for prop in data:
        if data[prop]["short_name"].startswith("Prop."):
            prop_name = "2014_" + re.findall("[0-9]+", data[prop]["short_name"])[0]
            for county in data[prop]["counties"]:
                temp_data = data[prop]["counties"][county]
                for candidate in temp_data["candidates"]:
                    if temp_data["name"] in percent_data:
                        temp_prop = prop_name + "_" + candidate["name"]
                        percent_data[temp_data["name"]][temp_prop] = candidate["vote_percent"] + "%"
                        total_data[temp_data["name"]][temp_prop] = candidate["vote_total"]

    header_row = percent_data["Alameda"].keys()
    header_row.sort()
    full_row = ["Category"] + header_row
    writer.writerow(full_row)
    for county in counties:
        total_row = [total_data[county][prop] for prop in header_row]
        writer.writerow([county + "_Total"] + total_row)
        percent_row = [percent_data[county][prop] for prop in header_row]
        writer.writerow([county + "_Percent"] + percent_row)

json_data.close()
