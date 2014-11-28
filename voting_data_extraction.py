import csv
import numpy as np

# Usage:
# voting_data = get_voting_data()
# result = voting_data["2006"]["Los Angeles_Percent"]["2006_1A_Yes"]
# -> result = '76.500%'

def get_voting_data():
    years = ["2006", "2008", "2010", "2012"]
    vote_map = {}
    for year in years:
        with open('elections/' + year + 'BallotMod.csv', 'rb') as csvfile:
            sub_map = {}
            reader = csv.DictReader(csvfile)
            for row in reader:
                sub_map[row["Category"]] = row
            vote_map[year] = sub_map
    return vote_map

print get_voting_data()["2006"]["Santa Clara_Percent"]["2006_1B_Yes"]
