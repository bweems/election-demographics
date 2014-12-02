import csv
import random
import numpy as np
import voting
import demographic
from sklearn import svm
from sklearn.cluster import KMeans
from sklearn.svm import SVR
from sklearn import linear_model

counties = ["Alameda", "Butte" , "Contra Costa", "El Dorado", "Fresno",
"Humboldt", "Imperial", "Kern", "Kings", "Lake", "Los Angeles", "Madera",
"Marin", "Mendocino", "Merced", "Monterey", "Napa", "Nevada", "Orange",
"Placer", "Riverside", "Sacramento", "San Bernardino", "San Diego",
"San Francisco", "San Joaquin", "San Luis Obispo", "San Mateo",
"Santa Barbara", "Santa Clara", "Santa Cruz", "Shasta", "Solano", "Sonoma",
"Stanislaus", "Sutter", "Tulare", "Ventura", "Yolo", "Yuba"]

# sample_issues = [{ "year": 2006, "prop": "1A", "polarity": "Yes" }, { "year": 2008, "prop": "12", "polarity": "No" }]
# sample_tag = { "name": "DiscoShit", "type": "Percent", "demographics": [10, 11, 12] }

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

    return designMatrix, targetMatrix

def zero_or_one(number):
    if number > 50:
        return 1
    else:
        return 0

def convert_to_binary_target(targetMatrix):
    vecfunc = np.vectorize(zero_or_one)
    return vecfunc(targetMatrix)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def test():
    sample_issues = [{ "year": 2008, "prop": "11", "polarity": "No" }]
    sample_tag = { "name": "DiscoShit", "type": "Percent", "demographics": [26] }
    model, design_matrix, target_matrix = build_classifier_model(sample_issues, sample_tag)
    test_classifier_model(model, design_matrix, target_matrix.ravel())

def get_all_training_issues():
    issues_hash = {}
    issues_hash['infra'] = []
    issues_hash['education'] = []
    issues_hash['crime'] = []
    issues_hash['environment'] = []
    issues_hash['gambling'] = []
    issues_hash['society'] = []
    issues_hash['politics'] = []
    issues_hash['corporate'] = []
    f = open('Proposition Labels.csv', 'rU')
    for line in f:
        arr = line.split(',')
        if arr[0] != '2014' and is_number(arr[0]):
            next_dict = {'year': int(arr[0]), 'prop': arr[4], 'polarity': arr[6]}
            category = arr[5]
            if category != '0' and category != 'veterans':
                issues_hash[category].append(next_dict)

    return issues_hash

def build_classifier_model(issues, tag):
    design_matrix, target_matrix = combine_design_matrices(issues, tag)
    binary_target_matrix = convert_to_binary_target(target_matrix)
    clf = svm.SVC()
    clf.fit(design_matrix, np.asarray(binary_target_matrix).ravel().transpose())
    return clf, design_matrix, binary_target_matrix

def build_regression_model(issues, tag):
    design_matrix, target_matrix = combine_design_matrices(issues, tag)
    clf = SVR()
    clf.fit(design_matrix, np.asarray(target_matrix).ravel().transpose())
    return clf

def test_classifier_model(model, design_matrix, target_matrix, test_design_matrix, test_target_matrix):

    num_errors = 0.0
    target_array = np.asarray(target_matrix).ravel()
    for i in range(len(target_array) - 1):
        if model.predict(design_matrix[i])[0] != np.array(target_array[i]):
            num_errors += 1
            # print design_matrix[i]
            # print np.array(target_array[i])
            # print
    print
    print "Number of errors (Training):"
    print num_errors
    print "Error percentage (Training):"
    print num_errors / len(target_array)
    print

    num_test_errors = 0.0
    test_target_array = np.asarray(test_target_matrix).ravel()
    for i in range(len(test_target_array) - 1):
        if model.predict(test_design_matrix[i])[0] != np.array(test_target_array[i]):
            num_test_errors += 1
            # print test_design_matrix[i]
            # print np.array(test_target_array[i])
            # print

    print "Number of errors (Testing):"
    print num_test_errors
    print "Error percentage (Testing):"
    print num_test_errors / len(test_target_array)
    print


def train_model():
    training_issues_hash = get_all_training_issues()
    model_hash = {}
    tag = { "name": "DiscoShit", "type": "Percent", "demographics": [26] }



def test_features():
    training_issues_hash = get_all_training_issues()
    train_issues = training_issues_hash['infra']
    random.shuffle(train_issues)
    test_issues = []
    test_issues.append(train_issues.pop())
    test_issues.append(train_issues.pop())
    features = ["HC02_EST_VC04", "HC02_EST_VC06", "HC02_EST_VC07"]

    tag = { "name": "Infra", "type": "Percent", "demographics": features }

    model, design_matrix, target_matrix = build_classifier_model(train_issues, tag)
    test_design_matrix,test_target_matrix = combine_design_matrices(test_issues, tag)

    test_target_matrix = convert_to_binary_target(test_target_matrix)

    test_classifier_model(model, design_matrix, target_matrix, test_design_matrix, test_target_matrix)

test_features()
