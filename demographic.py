import csv
import numpy as np
import voting


def modify_demographics(demographics, year):
    new_dem_array = []
    if year >= 2012:
        for dem in demographics:
            if dem.startswith('HC01_EST'):
                new_dem_array.append(dem.replace('HC01_EST', 'HC01'))
            elif dem.startswith('HC01_MOE'):
                new_dem_array.append(dem.replace('HC01_MOE', 'HC02'))
            elif dem.startswith('HC02_EST'):
                new_dem_array.append(dem.replace('HC02_EST', 'HC03'))
            elif dem.startswith('HC02_MOE'):
                new_dem_array.append(dem.replace('HC02_MOE', 'HC04'))
            else:
                new_dem_array.append(dem)
    else:
        new_dem_array = demographics
    return new_dem_array

def construct_submatrix(year, demographics, county, prop, type, polarity):

    demographics = modify_demographics(demographics, year)

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
