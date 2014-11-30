import csv
import numpy as np
import voting
import demographic
from sklearn import linear_model

counties = ["Alameda", "Butte" , "Contra Costa", "El Dorado", "Fresno",
"Humboldt", "Imperial", "Kern", "Kings", "Lake", "Los Angeles", "Madera",
"Marin", "Mendocino", "Merced", "Monterey", "Napa", "Nevada", "Orange",
"Placer", "Riverside", "Sacramento", "San Bernardino", "San Diego",
"San Francisco", "San Joaquin", "San Luis Obispo", "San Mateo",
"Santa Barbara", "Santa Clara", "Santa Cruz", "Shasta", "Solano", "Sonoma",
"Stanislaus", "Sutter", "Tulare", "Ventura", "Yolo", "Yuba"]

sample_issues = [{ "year": 2006, "prop": "1A", "polarity": "Yes" }, { "year": 2008, "prop": "12", "polarity": "No" }]
sample_tag = { "name": "DiscoShit", "type": "Percent", "demographics": [10, 11, 12] }



def compose_design_matrix(issue, tag):
    designMatrix = None
    targetMatrix = None

    for county in counties:
        feature_vec, target_vec = demographic.construct_submatrix(issue["year"], tag["demographics"], county, issue["prop"], tag["type"], issue["polarity"])
        if designMatrix is None:
            designMatrix = feature_vec
        else:
            designMatrix = np.vstack((designMatrix, feature_vec))
        if targetMatrix is None:
            targetMatrix = target_vec
        else:
            targetMatrix = np.vstack((targetMatrix, target_vec))

    return designMatrix, targetMatrix

def combine_design_matrices(issues, tag):
    designMatrix = None
    targetMatrix = None

    for issue in issues:
        temp_design, temp_target = compose_design_matrix(issue, tag)
        if designMatrix is None:
            designMatrix = temp_design
        else:
            designMatrix = np.vstack((designMatrix, temp_design))
        if targetMatrix is None:
            targetMatrix = temp_target
        else:
            targetMatrix = np.vstack((targetMatrix, temp_target))

    # print designMatrix
    # print targetMatrix
    return designMatrix, targetMatrix


def build_model():
    sample_issues = [{ "year": 2006, "prop": "1A", "polarity": "Yes" }, { "year": 2008, "prop": "12", "polarity": "No" }]
    sample_tag = { "name": "DiscoShit", "type": "Percent", "demographics": [10, 11, 12] }
    designMatrix, targetMatrix = combine_design_matrices(sample_issues, sample_tag)
   
    inputMatrix = np.hstack((targetMatrix, designMatrix))

    clf = linear_model.LinearRegression()

    clf.fit(designMatrix, targetMatrix)


    print clf.coef_


build_model()


# combine_design_matrices(sample_issues, sample_tag)
