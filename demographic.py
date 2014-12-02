import csv
import numpy as np
import voting

def construct_submatrix(year, demographics, county, prop, type, polarity):
    voting_data = voting.get_voting_data()
    targetArray = []
    vote = voting_data[str(year)][county + "_" + type][str(year) + "_" + prop + "_" + polarity]
    if type == "Percent":
        vote = vote[:-1]
    targetArray.append(float(vote))
    year_str = str(year)[-2:]
    if year_str == "06":
        year_str = "07"
    fileStr = 'demographic_csvs/ACS_' + year_str + '_1YR_DP2_with_ann.csv'
    with open(fileStr, 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        designArray = []

        for row in reader:
            if(row["GEO.display-label"] == (county + " County, California")):
                nextFeatureVector = []
                for dem in demographics:
                    nextFeatureVector.append(float(row[dem]))
                designArray.append(nextFeatureVector)

        return np.matrix(designArray), np.matrix(targetArray)
