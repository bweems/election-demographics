import csv
import random
import numpy as np
import voting
import demographic
import threading
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

features = []

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
    # print
    # print "Number of errors (Training):"
    # print num_errors
    # print "Error percentage (Training):"
    # print num_errors / len(target_array)
    # print

    num_test_errors = 0.0
    test_target_array = np.asarray(test_target_matrix).ravel()
    for i in range(len(test_target_array) - 1):
        if model.predict(test_design_matrix[i])[0] != np.array(test_target_array[i]):
            num_test_errors += 1
            # print test_design_matrix[i]
            # print np.array(test_target_array[i])
            # print

    # print "Number of errors (Testing):"
    # print num_test_errors
    # print "Error percentage (Testing):"
    # print num_test_errors / len(test_target_array)
    # print

    return (num_errors / len(target_array)), (num_test_errors / len(test_target_array))


def train_model():
    training_issues_hash = get_all_training_issues()
    model_hash = {}
    tag = { "name": "DiscoShit", "type": "Percent", "demographics": [26] }


def loop_test_features():

    features = ["HC02_EST_VC129","HC02_EST_VC120", "HC02_EST_VC73", "HC02_EST_VC108", "HC02_EST_VC68"]

    total_training = 0.0
    total_test = 0.0
    num_iters = 1
    for i in range(num_iters):
        train_error, test_error = test_features('politics', features)
        total_training += train_error
        total_test += test_error

    # print 
    # print "Training Error:"
    # print total_training / num_iters
    # print "Testing Error:"
    # print total_test / num_iters
    # print


# Gambling features: 


def test_features(issue_tag, features):
    training_issues_hash = get_all_training_issues()
    train_issues = training_issues_hash[issue_tag]
    test_size = len(train_issues) / 4
    random.shuffle(train_issues)

    test_issues = []    

    for i in range(test_size):
        test_issues.append(train_issues.pop())

    tag = { "name": "DiscoShit", "type": "Percent", "demographics": features }
    model,design_matrix, target_matrix = build_classifier_model(train_issues, tag)
    test_design_matrix,test_target_matrix = combine_design_matrices(test_issues, tag)
    test_target_matrix = convert_to_binary_target(test_target_matrix)
    train_error, test_error = test_classifier_model(model, design_matrix, target_matrix, test_design_matrix, test_target_matrix)

    return train_error, test_error

def load_features():
    with open("features.txt", "rb") as file:
        contents = file.readline().strip()
        features = contents.split(",")
        return features

def brute_force_features():
    all_features = load_features()
    best = []
    test_error = float("inf")
    for i in range(20, 21):
        for j in range(20):
            features = random.sample(all_features, i)
            avg = 0.0
            k = 10
            while k > 0:
                try:
                    train, test = test_features('infra', features)
                    avg += test
                    k -= 1
                except:
                    features = random.sample(all_features, i)
                    k = 10
            avg /= 10.0
            if avg < test_error:
                best = features
                test_error = avg
    print "Best features:"
    print best
    print "Best test error:"
    print test_error

def aggregate_test_features(tag, features):
    N = 20
    total_train = 0.0
    total_test = 0.0
    for i in range(N):
        train, test = test_features(tag, features)
        total_train += train
        total_test += test
    print "Training error:"
    print total_train / N
    print "Test error:"
    print total_test / N

    return test_classifier_model(model, design_matrix, target_matrix, test_design_matrix, test_target_matrix)

issues = ['infra','education','crime','environment','gambling','society','politics','corporate']
all_features = ["HC01_EST_VC02","HC01_MOE_VC02","HC02_EST_VC02","HC02_MOE_VC02","HC01_EST_VC03","HC01_MOE_VC03","HC02_EST_VC03","HC02_MOE_VC03","HC01_EST_VC04","HC01_MOE_VC04","HC02_EST_VC04","HC02_MOE_VC04","HC01_EST_VC05","HC01_MOE_VC05","HC02_EST_VC05","HC02_MOE_VC05","HC01_EST_VC06","HC01_MOE_VC06","HC02_EST_VC06","HC02_MOE_VC06","HC01_EST_VC07","HC01_MOE_VC07","HC02_EST_VC07","HC02_MOE_VC07","HC01_EST_VC08","HC01_MOE_VC08","HC02_EST_VC08","HC02_MOE_VC08","HC01_EST_VC09","HC01_MOE_VC09","HC02_EST_VC09","HC02_MOE_VC09","HC01_EST_VC10","HC01_MOE_VC10","HC02_EST_VC10","HC02_MOE_VC10","HC01_EST_VC11","HC01_MOE_VC11","HC02_EST_VC11","HC02_MOE_VC11","HC01_EST_VC12","HC01_MOE_VC12","HC02_EST_VC12","HC02_MOE_VC12","HC01_EST_VC13","HC01_MOE_VC13","HC02_EST_VC13","HC02_MOE_VC13","HC01_EST_VC14","HC01_MOE_VC14","HC02_EST_VC14","HC02_MOE_VC14","HC01_EST_VC15","HC01_MOE_VC15","HC02_EST_VC15","HC02_MOE_VC15","HC01_EST_VC16","HC01_MOE_VC16","HC02_EST_VC16","HC02_MOE_VC16","HC01_EST_VC17","HC01_MOE_VC17","HC02_EST_VC17","HC02_MOE_VC17","HC01_EST_VC19","HC01_MOE_VC19","HC02_EST_VC19","HC02_MOE_VC19","HC01_EST_VC20","HC01_MOE_VC20","HC02_EST_VC20","HC02_MOE_VC20","HC01_EST_VC21","HC01_MOE_VC21","HC02_EST_VC21","HC02_MOE_VC21","HC01_EST_VC22","HC01_MOE_VC22","HC02_EST_VC22","HC02_MOE_VC22","HC01_EST_VC23","HC01_MOE_VC23","HC02_EST_VC23","HC02_MOE_VC23","HC01_EST_VC24","HC01_MOE_VC24","HC02_EST_VC24","HC02_MOE_VC24","HC01_EST_VC25","HC01_MOE_VC25","HC02_EST_VC25","HC02_MOE_VC25","HC01_EST_VC27","HC01_MOE_VC27","HC02_EST_VC27","HC02_MOE_VC27","HC01_EST_VC28","HC01_MOE_VC28","HC02_EST_VC28","HC02_MOE_VC28","HC01_EST_VC29","HC01_MOE_VC29","HC02_EST_VC29","HC02_MOE_VC29","HC01_EST_VC30","HC01_MOE_VC30"]#,"HC02_EST_VC30","HC02_MOE_VC30","HC01_EST_VC31","HC01_MOE_VC31","HC02_EST_VC31","HC02_MOE_VC31","HC01_EST_VC32","HC01_MOE_VC32","HC02_EST_VC32","HC02_MOE_VC32","HC01_EST_VC33","HC01_MOE_VC33","HC02_EST_VC33","HC02_MOE_VC33","HC01_EST_VC34","HC01_MOE_VC34","HC02_EST_VC34","HC02_MOE_VC34","HC01_EST_VC35","HC01_MOE_VC35","HC02_EST_VC35","HC02_MOE_VC35","HC01_EST_VC36","HC01_MOE_VC36","HC02_EST_VC36","HC02_MOE_VC36","HC01_EST_VC37","HC01_MOE_VC37","HC02_EST_VC37","HC02_MOE_VC37","HC01_EST_VC38","HC01_MOE_VC38","HC02_EST_VC38","HC02_MOE_VC38","HC01_EST_VC40","HC01_MOE_VC40","HC02_EST_VC40","HC02_MOE_VC40","HC01_EST_VC41","HC01_MOE_VC41","HC02_EST_VC41","HC02_MOE_VC41","HC01_EST_VC42","HC01_MOE_VC42","HC02_EST_VC42","HC02_MOE_VC42","HC01_EST_VC43","HC01_MOE_VC43","HC02_EST_VC43","HC02_MOE_VC43","HC01_EST_VC44","HC01_MOE_VC44","HC02_EST_VC44","HC02_MOE_VC44","HC01_EST_VC45","HC01_MOE_VC45","HC02_EST_VC45","HC02_MOE_VC45","HC01_EST_VC46","HC01_MOE_VC46","HC02_EST_VC46","HC02_MOE_VC46","HC01_EST_VC48","HC01_MOE_VC48","HC02_EST_VC48","HC02_MOE_VC48","HC01_EST_VC49","HC01_MOE_VC49","HC02_EST_VC49","HC02_MOE_VC49","HC01_EST_VC51","HC01_MOE_VC51","HC02_EST_VC51","HC02_MOE_VC51","HC01_EST_VC52","HC01_MOE_VC52","HC02_EST_VC52","HC02_MOE_VC52","HC01_EST_VC53","HC01_MOE_VC53","HC02_EST_VC53","HC02_MOE_VC53","HC01_EST_VC54","HC01_MOE_VC54","HC02_EST_VC54","HC02_MOE_VC54","HC01_EST_VC56","HC01_MOE_VC56","HC02_EST_VC56","HC02_MOE_VC56","HC01_EST_VC57","HC01_MOE_VC57","HC02_EST_VC57","HC02_MOE_VC57","HC01_EST_VC59","HC01_MOE_VC59","HC02_EST_VC59","HC02_MOE_VC59","HC01_EST_VC60","HC01_MOE_VC60","HC02_EST_VC60","HC02_MOE_VC60","HC01_EST_VC61","HC01_MOE_VC61","HC02_EST_VC61","HC02_MOE_VC61","HC01_EST_VC62","HC01_MOE_VC62","HC02_EST_VC62","HC02_MOE_VC62","HC01_EST_VC63","HC01_MOE_VC63","HC02_EST_VC63","HC02_MOE_VC63","HC01_EST_VC64","HC01_MOE_VC64","HC02_EST_VC64","HC02_MOE_VC64","HC01_EST_VC66","HC01_MOE_VC66","HC02_EST_VC66","HC02_MOE_VC66","HC01_EST_VC67","HC01_MOE_VC67","HC02_EST_VC67","HC02_MOE_VC67","HC01_EST_VC68","HC01_MOE_VC68","HC02_EST_VC68","HC02_MOE_VC68","HC01_EST_VC69","HC01_MOE_VC69","HC02_EST_VC69","HC02_MOE_VC69","HC01_EST_VC70","HC01_MOE_VC70","HC02_EST_VC70","HC02_MOE_VC70","HC01_EST_VC71","HC01_MOE_VC71","HC02_EST_VC71","HC02_MOE_VC71","HC01_EST_VC72","HC01_MOE_VC72","HC02_EST_VC72","HC02_MOE_VC72","HC01_EST_VC73","HC01_MOE_VC73","HC02_EST_VC73","HC02_MOE_VC73","HC01_EST_VC74","HC01_MOE_VC74","HC02_EST_VC74","HC02_MOE_VC74","HC01_EST_VC75","HC01_MOE_VC75","HC02_EST_VC75","HC02_MOE_VC75","HC01_EST_VC77","HC01_MOE_VC77","HC02_EST_VC77","HC02_MOE_VC77","HC01_EST_VC78","HC01_MOE_VC78","HC02_EST_VC78","HC02_MOE_VC78","HC01_EST_VC80","HC01_MOE_VC80","HC02_EST_VC80","HC02_MOE_VC80","HC01_EST_VC81","HC01_MOE_VC81","HC02_EST_VC81","HC02_MOE_VC81","HC01_EST_VC82","HC01_MOE_VC82","HC02_EST_VC82","HC02_MOE_VC82","HC01_EST_VC83","HC01_MOE_VC83","HC02_EST_VC83","HC02_MOE_VC83","HC01_EST_VC84","HC01_MOE_VC84","HC02_EST_VC84","HC02_MOE_VC84","HC01_EST_VC85","HC01_MOE_VC85","HC02_EST_VC85","HC02_MOE_VC85","HC01_EST_VC86","HC01_MOE_VC86","HC02_EST_VC86","HC02_MOE_VC86","HC01_EST_VC87","HC01_MOE_VC87","HC02_EST_VC87","HC02_MOE_VC87","HC01_EST_VC89","HC01_MOE_VC89","HC02_EST_VC89","HC02_MOE_VC89","HC01_EST_VC90","HC01_MOE_VC90","HC02_EST_VC90","HC02_MOE_VC90","HC01_EST_VC91","HC01_MOE_VC91","HC02_EST_VC91","HC02_MOE_VC91","HC01_EST_VC92","HC01_MOE_VC92","HC02_EST_VC92","HC02_MOE_VC92","HC01_EST_VC93","HC01_MOE_VC93","HC02_EST_VC93","HC02_MOE_VC93","HC01_EST_VC94","HC01_MOE_VC94","HC02_EST_VC94","HC02_MOE_VC94","HC01_EST_VC95","HC01_MOE_VC95","HC02_EST_VC95","HC02_MOE_VC95","HC01_EST_VC96","HC01_MOE_VC96","HC02_EST_VC96","HC02_MOE_VC96","HC01_EST_VC98","HC01_MOE_VC98","HC02_EST_VC98","HC02_MOE_VC98","HC01_EST_VC99","HC01_MOE_VC99","HC02_EST_VC99","HC02_MOE_VC99","HC01_EST_VC100","HC01_MOE_VC100","HC02_EST_VC100","HC02_MOE_VC100","HC01_EST_VC101","HC01_MOE_VC101","HC02_EST_VC101","HC02_MOE_VC101","HC01_EST_VC102","HC01_MOE_VC102","HC02_EST_VC102","HC02_MOE_VC102","HC01_EST_VC103","HC01_MOE_VC103","HC02_EST_VC103","HC02_MOE_VC103","HC01_EST_VC104","HC01_MOE_VC104","HC02_EST_VC104","HC02_MOE_VC104","HC01_EST_VC106","HC01_MOE_VC106","HC02_EST_VC106","HC02_MOE_VC106","HC01_EST_VC107","HC01_MOE_VC107","HC02_EST_VC107","HC02_MOE_VC107","HC01_EST_VC108","HC01_MOE_VC108","HC02_EST_VC108","HC02_MOE_VC108","HC01_EST_VC110","HC01_MOE_VC110","HC02_EST_VC110","HC02_MOE_VC110","HC01_EST_VC111","HC01_MOE_VC111","HC02_EST_VC111","HC02_MOE_VC111","HC01_EST_VC112","HC01_MOE_VC112","HC02_EST_VC112","HC02_MOE_VC112","HC01_EST_VC113","HC01_MOE_VC113","HC02_EST_VC113","HC02_MOE_VC113","HC01_EST_VC114","HC01_MOE_VC114","HC02_EST_VC114","HC02_MOE_VC114","HC01_EST_VC115","HC01_MOE_VC115","HC02_EST_VC115","HC02_MOE_VC115","HC01_EST_VC116","HC01_MOE_VC116","HC02_EST_VC116","HC02_MOE_VC116","HC01_EST_VC118","HC01_MOE_VC118","HC02_EST_VC118","HC02_MOE_VC118","HC01_EST_VC119","HC01_MOE_VC119","HC02_EST_VC119","HC02_MOE_VC119","HC01_EST_VC120","HC01_MOE_VC120","HC02_EST_VC120","HC02_MOE_VC120","HC01_EST_VC121","HC01_MOE_VC121","HC02_EST_VC121","HC02_MOE_VC121","HC01_EST_VC122","HC01_MOE_VC122","HC02_EST_VC122","HC02_MOE_VC122","HC01_EST_VC123","HC01_MOE_VC123","HC02_EST_VC123","HC02_MOE_VC123","HC01_EST_VC124","HC01_MOE_VC124","HC02_EST_VC124","HC02_MOE_VC124","HC01_EST_VC126","HC01_MOE_VC126","HC02_EST_VC126","HC02_MOE_VC126","HC01_EST_VC127","HC01_MOE_VC127","HC02_EST_VC127","HC02_MOE_VC127","HC01_EST_VC128","HC01_MOE_VC128","HC02_EST_VC128","HC02_MOE_VC128","HC01_EST_VC129","HC01_MOE_VC129","HC02_EST_VC129","HC02_MOE_VC129","HC01_EST_VC130","HC01_MOE_VC130","HC02_EST_VC130","HC02_MOE_VC130","HC01_EST_VC131","HC01_MOE_VC131","HC02_EST_VC131","HC02_MOE_VC131","HC01_EST_VC132","HC01_MOE_VC132","HC02_EST_VC132","HC02_MOE_VC132","HC01_EST_VC133","HC01_MOE_VC133","HC02_EST_VC133","HC02_MOE_VC133","HC01_EST_VC134","HC01_MOE_VC134","HC02_EST_VC134","HC02_MOE_VC134","HC01_EST_VC135","HC01_MOE_VC135","HC02_EST_VC135","HC02_MOE_VC135","HC01_EST_VC136","HC01_MOE_VC136","HC02_EST_VC136","HC02_MOE_VC136","HC01_EST_VC137","HC01_MOE_VC137","HC02_EST_VC137","HC02_MOE_VC137","HC01_EST_VC139","HC01_MOE_VC139","HC02_EST_VC139","HC02_MOE_VC139","HC01_EST_VC140","HC01_MOE_VC140","HC02_EST_VC140","HC02_MOE_VC140","HC01_EST_VC141","HC01_MOE_VC141","HC02_EST_VC141","HC02_MOE_VC141","HC01_EST_VC142","HC01_MOE_VC142","HC02_EST_VC142","HC02_MOE_VC142","HC01_EST_VC143","HC01_MOE_VC143","HC02_EST_VC143","HC02_MOE_VC143","HC01_EST_VC144","HC01_MOE_VC144","HC02_EST_VC144","HC02_MOE_VC144","HC01_EST_VC145","HC01_MOE_VC145","HC02_EST_VC145","HC02_MOE_VC145","HC01_EST_VC146","HC01_MOE_VC146","HC02_EST_VC146","HC02_MOE_VC146","HC01_EST_VC147","HC01_MOE_VC147","HC02_EST_VC147","HC02_MOE_VC147","HC01_EST_VC148","HC01_MOE_VC148","HC02_EST_VC148","HC02_MOE_VC148","HC01_EST_VC149","HC01_MOE_VC149","HC02_EST_VC149","HC02_MOE_VC149","HC01_EST_VC150","HC01_MOE_VC150","HC02_EST_VC150","HC02_MOE_VC150","HC01_EST_VC151","HC01_MOE_VC151","HC02_EST_VC151","HC02_MOE_VC151","HC01_EST_VC152","HC01_MOE_VC152","HC02_EST_VC152","HC02_MOE_VC152","HC01_EST_VC153","HC01_MOE_VC153","HC02_EST_VC153","HC02_MOE_VC153","HC01_EST_VC154","HC01_MOE_VC154","HC02_EST_VC154","HC02_MOE_VC154","HC01_EST_VC155","HC01_MOE_VC155","HC02_EST_VC155","HC02_MOE_VC155","HC01_EST_VC156","HC01_MOE_VC156","HC02_EST_VC156","HC02_MOE_VC156","HC01_EST_VC157","HC01_MOE_VC157","HC02_EST_VC157","HC02_MOE_VC157","HC01_EST_VC158","HC01_MOE_VC158","HC02_EST_VC158","HC02_MOE_VC158","HC01_EST_VC159","HC01_MOE_VC159","HC02_EST_VC159","HC02_MOE_VC159","HC01_EST_VC160","HC01_MOE_VC160","HC02_EST_VC160","HC02_MOE_VC160","HC01_EST_VC161","HC01_MOE_VC161","HC02_EST_VC161","HC02_MOE_VC161","HC01_EST_VC162","HC01_MOE_VC162","HC02_EST_VC162","HC02_MOE_VC162","HC01_EST_VC163","HC01_MOE_VC163","HC02_EST_VC163","HC02_MOE_VC163","HC01_EST_VC164","HC01_MOE_VC164","HC02_EST_VC164","HC02_MOE_VC164","HC01_EST_VC165","HC01_MOE_VC165","HC02_EST_VC165","HC02_MOE_VC165","HC01_EST_VC166","HC01_MOE_VC166","HC02_EST_VC166","HC02_MOE_VC166"]
trainingErrors = []
testingErrors = []
enviroFeatures = ["HC02_EST_VC04","HC02_EST_VC08","HC02_EST_VC29","HC02_EST_VC31","HC02_EST_VC40","HC02_EST_VC49","HC02_EST_VC68","HC02_EST_VC70",]
crimeFeatures = ["HC02_EST_VC21","HC02_EST_VC25","HC02_EST_VC28","HC02_EST_VC29","HC02_EST_VC30","HC02_EST_VC61","HC02_EST_VC67","HC02_EST_VC68","HC02_EST_VC73","HC02_EST_VC104","HC02_EST_VC108","HC02_EST_VC114","HC02_EST_VC119","HC02_EST_VC121","HC02_EST_VC130","HC02_EST_VC137","HC02_EST_VC139","HC02_EST_VC149","HC02_EST_VC154","HC02_EST_VC164"]
societyFeatures = ["HC02_EST_VC25","HC02_EST_VC118"]
NUM_ITERS = 10
NUM_BASE_ITERS = 100
MAX_FEATURE_VECTOR_LENGTH = 10

def get_testing_error(tag, features, numIters):
    testingError = 0
    for i in range(numIters):
        new_training_error, new_testing_error = test_features(tag, features)
        testingError += new_testing_error
    print "Tag: %s \t Features: %s \t TestingError: %s" % (tag, features, str(testingError/numIters))
    return testingError/numIters

def find_best_features(tag, baseline_testing_error, features):
    bestFeatures = []
    for feature in features:
        if feature[:8] == "HC02_EST":
            try:
                # print feature
                testingError = get_testing_error(tag, [feature], NUM_ITERS)
                if testingError/NUM_ITERS < baseline_testing_error:
                    bestFeatures.append(feature)
            except ValueError, KeyError:
                pass
    print "Best Features Length: %s" % (len(bestFeatures))
    if len(bestFeatures) > MAX_FEATURE_VECTOR_LENGTH:
        bestFeatures = find_best_features(tag, baseline_testing_error-.01, bestFeatures)
    elif len(bestFeatures) == 0:
        bestFeatures = ["HC02_EST_VC02"]
    return bestFeatures

def tag_feature_selector(tag):
    print tag
    baseline_testing_error = get_testing_error(tag, ['HC02_EST_VC02'], NUM_BASE_ITERS)
    print "Baseline Testing Error: %s" % (baseline_testing_error)
    best_features = find_best_features(tag, baseline_testing_error, all_features)
    testing_error = get_testing_error(tag, best_features, NUM_ITERS*10)
    print "Tag: %s \n Features: %s \n TestingError: %s \t Baseline Testing Error: %s" % (tag, best_features, testing_error, baseline_testing_error) 
    return baseline_testing_error, testing_error, best_features

class FeatureSelectorThread(threading.Thread):

    def __init__(self,tag):
        super(FeatureSelectorThread, self).__init__()
        self.tag = tag
        self.baseline_error = 0
        self.testing_error = 0
        self.best_features = []

    def run(self):
        self.baseline_error, self.testing_error, self.best_features = tag_feature_selector(self.tag)

threads = [FeatureSelectorThread('crime'),FeatureSelectorThread('education'),FeatureSelectorThread('infra'),FeatureSelectorThread('environment'),FeatureSelectorThread('society'),FeatureSelectorThread('politics'),FeatureSelectorThread('corporate')]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
# thread1 = FeatureSelectorThread('crime')
# thread2 = FeatureSelectorThread('education')
# thread3 = FeatureSelectorThread('infra')
# thread4 = FeatureSelectorThread('environment',
# thread5 = FeatureSelectorThread('gambling')
# thread6 = FeatureSelectorThread('society')
# thread7 = FeatureSelectorThread('politics')
# thread8 = FeatureSelectorThread('corporate')
# thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()
# thread5.start()
# thread6.start()
# thread7.start()
# thread8.start()
# thread1.join()
# thread2.join()
# thread3.join()
# thread4.join()
# thread5.join()
# thread6.join()
# thread7.join()
# thread8.join()


# run_feature_selector()
