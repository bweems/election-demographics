import csv
import numpy as np


column_names = []


def construct_design_matrix(spamreader):

	designArray = []

	for index, row in enumerate(spamreader):
		
		if index is 1:
			column_names = row

		if index > 1:

			county_name = row[2]

			nextFeatureVector = []

			# Add percentage of households with children under 18 years
			nextFeatureVector.append(row[13])

			# Add percentage of households with a person 65 years or older
			nextFeatureVector.append(row[57])

			designArray.append(nextFeatureVector)

	return np.matrix(designArray)


with open('demographic_csvs/ACS_07_1YR_DP2_with_ann.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile)

	designMatrix = construct_design_matrix(spamreader)

	print designMatrix

