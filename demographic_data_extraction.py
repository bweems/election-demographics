import csv
import numpy as np


column_names = []


# Estimate; HOUSEHOLDS BY TYPE - Total households	
# Margin of Error; HOUSEHOLDS BY TYPE - Total households	
# Estimate; HOUSEHOLDS BY TYPE - Total households - Family households (families)	
# Margin of Error; HOUSEHOLDS BY TYPE - Total households - Family households (families)	
# Estimate; HOUSEHOLDS BY TYPE - Total households - Family households (families) - With own children under 18 years	
# Margin of Error; HOUSEHOLDS BY TYPE - Total households - Family households (families) - With own children under 18 years	

# Estimate; HOUSEHOLDS BY TYPE - Total households - Married-couple families	
# Margin of Error; HOUSEHOLDS BY TYPE - Total households - Married-couple families	
# Estimate; HOUSEHOLDS BY TYPE - Total households - Married-couple families - With own children under 18 years	
# Margin of Error; HOUSEHOLDS BY TYPE - Total households - Married-couple families - With own children under 18 years	
# Estimate; HOUSEHOLDS BY TYPE - Total households - Male householder, no wife present	
# Margin of Error; HOUSEHOLDS BY TYPE - Total households - Male householder, no wife present	
# Estimate; HOUSEHOLDS BY TYPE - Total households - Male householder, no wife present - With own children under 18 years	
# Margin of Error; HOUSEHOLDS BY TYPE - Total households - Male householder, no wife present - With own children under 18 years	
# Estimate; HOUSEHOLDS BY TYPE - Total households - Female householder, no husband present	
# Margin of Error; HOUSEHOLDS BY TYPE - Total households - Female householder, no husband present	
# Estimate; HOUSEHOLDS BY TYPE - Total households - Female householder, no husband present - With own children under 18 years	
# Margin of Error; HOUSEHOLDS BY TYPE - Total households - Female householder, no husband present - With own children under 18 years	
# Estimate; HOUSEHOLDS BY TYPE - Total households - Nonfamily households	
# Margin of Error; HOUSEHOLDS BY TYPE - Total households - Nonfamily households	
# Estimate; HOUSEHOLDS BY TYPE - Total households - Nonfamily households - Householder living alone	
# Margin of Error; HOUSEHOLDS BY TYPE - Total households - Nonfamily households - Householder living alone	
# Estimate; HOUSEHOLDS BY TYPE - Total households - Nonfamily households - Householder living alone - 65 years and over	
# Margin of Error; HOUSEHOLDS BY TYPE - Total households - Nonfamily households - Householder living alone - 65 years and over	
# Estimate; HOUSEHOLDS BY TYPE - Total households - Households with one or more people under 18 years	
# Margin of Error; HOUSEHOLDS BY TYPE - Total households - Households with one or more people under 18 years	
# Estimate; HOUSEHOLDS BY TYPE - Total households - Households with one or more people 65 years and over	
# Margin of Error; HOUSEHOLDS BY TYPE - Total households - Households with one or more people 65 years and over	
# Estimate; HOUSEHOLDS BY TYPE - Total households - Average household size	
# Margin of Error; HOUSEHOLDS BY TYPE - Total households - Average household size	
# Estimate; HOUSEHOLDS BY TYPE - Total households - Average family size	
# Margin of Error; HOUSEHOLDS BY TYPE - Total households - Average family size	
# Estimate; RELATIONSHIP - Household population	
# Margin of Error; RELATIONSHIP - Household population	
# Estimate; RELATIONSHIP - Household population - Householder	
# Margin of Error; RELATIONSHIP - Household population - Householder	
# Estimate; RELATIONSHIP - Household population - Spouse	
# Margin of Error; RELATIONSHIP - Household population - Spouse	
# Estimate; RELATIONSHIP - Household population - Child	
# Margin of Error; RELATIONSHIP - Household population - Child	
# Estimate; RELATIONSHIP - Household population - Other relatives	
# Margin of Error; RELATIONSHIP - Household population - Other relatives	
# Estimate; RELATIONSHIP - Household population - Nonrelatives	
# Margin of Error; RELATIONSHIP - Household population - Nonrelatives	
# Estimate; RELATIONSHIP - Household population - Nonrelatives - Unmarried partner	
# Margin of Error; RELATIONSHIP - Household population - Nonrelatives - Unmarried partner	
# Estimate; MARITAL STATUS - Males 15 years and over	
# Margin of Error; MARITAL STATUS - Males 15 years and over	
# Estimate; MARITAL STATUS - Males 15 years and over - Never married	
# Margin of Error; MARITAL STATUS - Males 15 years and over - Never married	
# Estimate; MARITAL STATUS - Males 15 years and over - Now married, except separated	
# Margin of Error; MARITAL STATUS - Males 15 years and over - Now married, except separated	
# Estimate; MARITAL STATUS - Males 15 years and over - Separated	
# Margin of Error; MARITAL STATUS - Males 15 years and over - Separated	
# Estimate; MARITAL STATUS - Males 15 years and over - Widowed	
# Margin of Error; MARITAL STATUS - Males 15 years and over - Widowed	
# Estimate; MARITAL STATUS - Males 15 years and over - Divorced	
# Margin of Error; MARITAL STATUS - Males 15 years and over - Divorced	
# Estimate; MARITAL STATUS - Females 15 years and over	
# Margin of Error; MARITAL STATUS - Females 15 years and over	
# Estimate; MARITAL STATUS - Females 15 years and over - Never married	
# Margin of Error; MARITAL STATUS - Females 15 years and over - Never married	
# Estimate; MARITAL STATUS - Females 15 years and over - Now married, except separated	
# Margin of Error; MARITAL STATUS - Females 15 years and over - Now married, except separated	
# Estimate; MARITAL STATUS - Females 15 years and over - Separated	
# Margin of Error; MARITAL STATUS - Females 15 years and over - Separated	
# Estimate; MARITAL STATUS - Females 15 years and over - Widowed	
# Margin of Error; MARITAL STATUS - Females 15 years and over - Widowed	
# Estimate; MARITAL STATUS - Females 15 years and over - Divorced	
# Margin of Error; MARITAL STATUS - Females 15 years and over - Divorced	
# Estimate; FERTILITY - Number of women 15 to 50 years old who had a birth in the past 12 months	
# Margin of Error; FERTILITY - Number of women 15 to 50 years old who had a birth in the past 12 months	
# Estimate; FERTILITY - Number of women 15 to 50 years old who had a birth in the past 12 months - Unmarried women (widowed, divorced, and never married)	
# Margin of Error; FERTILITY - Number of women 15 to 50 years old who had a birth in the past 12 months - Unmarried women (widowed, divorced, and never married)	
# Estimate; FERTILITY - Number of women 15 to 50 years old who had a birth in the past 12 months - Unmarried women (widowed, divorced, and never married) - Per 1,000 unmarried women	
# Margin of Error; FERTILITY - Number of women 15 to 50 years old who had a birth in the past 12 months - Unmarried women (widowed, divorced, and never married) - Per 1,000 unmarried women	
# Estimate; FERTILITY - Number of women 15 to 50 years old who had a birth in the past 12 months - Per 1,000 women 15 to 50 years old	
# Margin of Error; FERTILITY - Number of women 15 to 50 years old who had a birth in the past 12 months - Per 1,000 women 15 to 50 years old	
# Estimate; FERTILITY - Number of women 15 to 50 years old who had a birth in the past 12 months - Per 1,000 women 15 to 19 years old	
# Margin of Error; FERTILITY - Number of women 15 to 50 years old who had a birth in the past 12 months - Per 1,000 women 15 to 19 years old	
# Estimate; FERTILITY - Number of women 15 to 50 years old who had a birth in the past 12 months - Per 1,000 women 20 to 34 years old	
# Margin of Error; FERTILITY - Number of women 15 to 50 years old who had a birth in the past 12 months - Per 1,000 women 20 to 34 years old	
# Estimate; FERTILITY - Number of women 15 to 50 years old who had a birth in the past 12 months - Per 1,000 women 35 to 50 years old	
# Margin of Error; FERTILITY - Number of women 15 to 50 years old who had a birth in the past 12 months - Per 1,000 women 35 to 50 years old	
# Estimate; GRANDPARENTS - Number of grandparents living with own grandchildren under 18 years	
# Margin of Error; GRANDPARENTS - Number of grandparents living with own grandchildren under 18 years	
# Estimate; GRANDPARENTS - Number of grandparents living with own grandchildren under 18 years - Responsible for grandchildren	
# Margin of Error; GRANDPARENTS - Number of grandparents living with own grandchildren under 18 years - Responsible for grandchildren	
# Estimate; GRANDPARENTS - Number of grandparents living with own grandchildren under 18 years - Years responsible for grandchildren - Less than 1 year	
# Margin of Error; GRANDPARENTS - Number of grandparents living with own grandchildren under 18 years - Years responsible for grandchildren - Less than 1 year	
# Estimate; GRANDPARENTS - Number of grandparents living with own grandchildren under 18 years - Years responsible for grandchildren - 1 or 2 years	
# Margin of Error; GRANDPARENTS - Number of grandparents living with own grandchildren under 18 years - Years responsible for grandchildren - 1 or 2 years	
# Estimate; GRANDPARENTS - Number of grandparents living with own grandchildren under 18 years - Years responsible for grandchildren - 3 or 4 years	
# Margin of Error; GRANDPARENTS - Number of grandparents living with own grandchildren under 18 years - Years responsible for grandchildren - 3 or 4 years	
# Estimate; GRANDPARENTS - Number of grandparents living with own grandchildren under 18 years - Years responsible for grandchildren - 5 or more years	
# Margin of Error; GRANDPARENTS - Number of grandparents living with own grandchildren under 18 years - Years responsible for grandchildren - 5 or more years	
# Estimate; GRANDPARENTS - Characteristics of grandparents responsible for own grandchildren under 18 years - Who are female	
# Margin of Error; GRANDPARENTS - Characteristics of grandparents responsible for own grandchildren under 18 years - Who are female	
# Estimate; GRANDPARENTS - Characteristics of grandparents responsible for own grandchildren under 18 years - Who are married	
# Margin of Error; GRANDPARENTS - Characteristics of grandparents responsible for own grandchildren under 18 years - Who are married	
# Estimate; SCHOOL ENROLLMENT - Population 3 years and over enrolled in school	
# Margin of Error; SCHOOL ENROLLMENT - Population 3 years and over enrolled in school	
# Estimate; SCHOOL ENROLLMENT - Population 3 years and over enrolled in school - Nursery school, preschool	
# Margin of Error; SCHOOL ENROLLMENT - Population 3 years and over enrolled in school - Nursery school, preschool	
# Estimate; SCHOOL ENROLLMENT - Population 3 years and over enrolled in school - Kindergarten	
# Margin of Error; SCHOOL ENROLLMENT - Population 3 years and over enrolled in school - Kindergarten	
# Estimate; SCHOOL ENROLLMENT - Population 3 years and over enrolled in school - Elementary school (grades 1-8)	
# Margin of Error; SCHOOL ENROLLMENT - Population 3 years and over enrolled in school - Elementary school (grades 1-8)	
# Estimate; SCHOOL ENROLLMENT - Population 3 years and over enrolled in school - High school (grades 9-12)	
# Margin of Error; SCHOOL ENROLLMENT - Population 3 years and over enrolled in school - High school (grades 9-12)	
# Estimate; SCHOOL ENROLLMENT - Population 3 years and over enrolled in school - College or graduate school	
# Margin of Error; SCHOOL ENROLLMENT - Population 3 years and over enrolled in school - College or graduate school	
# Estimate; EDUCATIONAL ATTAINMENT - Population 25 years and over	
# Margin of Error; EDUCATIONAL ATTAINMENT - Population 25 years and over	
# Estimate; EDUCATIONAL ATTAINMENT - Population 25 years and over - Less than 9th grade	
# Margin of Error; EDUCATIONAL ATTAINMENT - Population 25 years and over - Less than 9th grade	
# Estimate; EDUCATIONAL ATTAINMENT - Population 25 years and over - 9th to 12th grade, no diploma	
# Margin of Error; EDUCATIONAL ATTAINMENT - Population 25 years and over - 9th to 12th grade, no diploma	
# Estimate; EDUCATIONAL ATTAINMENT - Population 25 years and over - High school graduate (includes equivalency)	
# Margin of Error; EDUCATIONAL ATTAINMENT - Population 25 years and over - High school graduate (includes equivalency)	
# Estimate; EDUCATIONAL ATTAINMENT - Population 25 years and over - Some college, no degree	
# Margin of Error; EDUCATIONAL ATTAINMENT - Population 25 years and over - Some college, no degree	
# Estimate; EDUCATIONAL ATTAINMENT - Population 25 years and over - Associate's degree	
# Margin of Error; EDUCATIONAL ATTAINMENT - Population 25 years and over - Associate's degree	
# Estimate; EDUCATIONAL ATTAINMENT - Population 25 years and over - Bachelor's degree	
# Margin of Error; EDUCATIONAL ATTAINMENT - Population 25 years and over - Bachelor's degree	
# Estimate; EDUCATIONAL ATTAINMENT - Population 25 years and over - Graduate or professional degree	
# Margin of Error; EDUCATIONAL ATTAINMENT - Population 25 years and over - Graduate or professional degree	
# Estimate; EDUCATIONAL ATTAINMENT - Population 25 years and over - Percent high school graduate or higher	
# Margin of Error; EDUCATIONAL ATTAINMENT - Population 25 years and over - Percent high school graduate or higher	
# Estimate; EDUCATIONAL ATTAINMENT - Population 25 years and over - Percent bachelor's degree or higher	
# Margin of Error; EDUCATIONAL ATTAINMENT - Population 25 years and over - Percent bachelor's degree or higher	
# Estimate; VETERAN STATUS - Civilian population 18 years and over	
# Margin of Error; VETERAN STATUS - Civilian population 18 years and over	
# Estimate; VETERAN STATUS - Civilian population 18 years and over - Civilian veterans	
# Margin of Error; VETERAN STATUS - Civilian population 18 years and over - Civilian veterans	
# Estimate; DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION - Population 5 years and over	
# Margin of Error; DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION - Population 5 years and over	
# Estimate; DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION - Population 5 years and over - With a disability	
# Margin of Error; DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION - Population 5 years and over - With a disability	
# Estimate; DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION - Population 5 to 15 years	
# Margin of Error; DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION - Population 5 to 15 years	
# Estimate; DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION - Population 5 to 15 years - With a disability	
# Margin of Error; DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION - Population 5 to 15 years - With a disability	
# Estimate; DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION - Population 16 to 64 years	
# Margin of Error; DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION - Population 16 to 64 years	
# Estimate; DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION - Population 16 to 64 years - With a disability	
# Margin of Error; DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION - Population 16 to 64 years - With a disability	
# Estimate; DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION - Population 65 years and over	
# Margin of Error; DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION - Population 65 years and over	
# Estimate; DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION - Population 65 years and over - With a disability	
# Margin of Error; DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION - Population 65 years and over - With a disability	
# Estimate; RESIDENCE 1 YEAR AGO - Population 1 year and over	
# Margin of Error; RESIDENCE 1 YEAR AGO - Population 1 year and over	
# Estimate; RESIDENCE 1 YEAR AGO - Population 1 year and over - Same house	
# Margin of Error; RESIDENCE 1 YEAR AGO - Population 1 year and over - Same house	
# Estimate; RESIDENCE 1 YEAR AGO - Population 1 year and over - Different house in the U.S.	
# Margin of Error; RESIDENCE 1 YEAR AGO - Population 1 year and over - Different house in the U.S.	
# Estimate; RESIDENCE 1 YEAR AGO - Population 1 year and over - Different house in the U.S. - Same county	
# Margin of Error; RESIDENCE 1 YEAR AGO - Population 1 year and over - Different house in the U.S. - Same county	
# Estimate; RESIDENCE 1 YEAR AGO - Population 1 year and over - Different house in the U.S. - Different county	
# Margin of Error; RESIDENCE 1 YEAR AGO - Population 1 year and over - Different house in the U.S. - Different county	
# Estimate; RESIDENCE 1 YEAR AGO - Population 1 year and over - Different house in the U.S. - Different county - Same state	
# Margin of Error; RESIDENCE 1 YEAR AGO - Population 1 year and over - Different house in the U.S. - Different county - Same state	
# Estimate; RESIDENCE 1 YEAR AGO - Population 1 year and over - Different house in the U.S. - Different county - Different state	
# Margin of Error; RESIDENCE 1 YEAR AGO - Population 1 year and over - Different house in the U.S. - Different county - Different state	
# Estimate; RESIDENCE 1 YEAR AGO - Population 1 year and over - Abroad	
# Margin of Error; RESIDENCE 1 YEAR AGO - Population 1 year and over - Abroad	
# Estimate; PLACE OF BIRTH - Total population	
# Margin of Error; PLACE OF BIRTH - Total population	
# Estimate; PLACE OF BIRTH - Total population - Native	
# Margin of Error; PLACE OF BIRTH - Total population - Native	
# Estimate; PLACE OF BIRTH - Total population - Native - Born in United States	
# Margin of Error; PLACE OF BIRTH - Total population - Native - Born in United States	
# Estimate; PLACE OF BIRTH - Total population - Native - Born in United States - State of residence	
# Margin of Error; PLACE OF BIRTH - Total population - Native - Born in United States - State of residence	
# Estimate; PLACE OF BIRTH - Total population - Native - Born in United States - Different state	
# Margin of Error; PLACE OF BIRTH - Total population - Native - Born in United States - Different state	
# Estimate; PLACE OF BIRTH - Total population - Native - Born in Puerto Rico, U.S. Island areas, or born abroad to American parent(s)	
# Margin of Error; PLACE OF BIRTH - Total population - Native - Born in Puerto Rico, U.S. Island areas, or born abroad to American parent(s)	
# Estimate; PLACE OF BIRTH - Total population - Foreign born	
# Margin of Error; PLACE OF BIRTH - Total population - Foreign born	
# Estimate; U.S. CITIZENSHIP STATUS - Foreign-born population	
# Margin of Error; U.S. CITIZENSHIP STATUS - Foreign-born population	
# Estimate; U.S. CITIZENSHIP STATUS - Foreign-born population - Naturalized U.S. citizen	
# Margin of Error; U.S. CITIZENSHIP STATUS - Foreign-born population - Naturalized U.S. citizen	
# Estimate; U.S. CITIZENSHIP STATUS - Foreign-born population - Not a U.S. citizen	
# Margin of Error; U.S. CITIZENSHIP STATUS - Foreign-born population - Not a U.S. citizen	
# Estimate; YEAR OF ENTRY - Population born outside the United States	
# Margin of Error; YEAR OF ENTRY - Population born outside the United States	
# Estimate; YEAR OF ENTRY - Population born outside the United States - Native	
# Margin of Error; YEAR OF ENTRY - Population born outside the United States - Native	
# Estimate; YEAR OF ENTRY - Population born outside the United States - Native - Entered 2000 or later	
# Margin of Error; YEAR OF ENTRY - Population born outside the United States - Native - Entered 2000 or later	
# Estimate; YEAR OF ENTRY - Population born outside the United States - Native - Entered before 2000	
# Margin of Error; YEAR OF ENTRY - Population born outside the United States - Native - Entered before 2000	
# Estimate; YEAR OF ENTRY - Population born outside the United States - Foreign born	
# Margin of Error; YEAR OF ENTRY - Population born outside the United States - Foreign born	
# Estimate; YEAR OF ENTRY - Population born outside the United States - Foreign born - Entered 2000 or later	
# Margin of Error; YEAR OF ENTRY - Population born outside the United States - Foreign born - Entered 2000 or later	
# Estimate; YEAR OF ENTRY - Population born outside the United States - Foreign born - Entered before 2000	
# Margin of Error; YEAR OF ENTRY - Population born outside the United States - Foreign born - Entered before 2000	
# Estimate; WORLD REGION OF BIRTH OF FOREIGN BORN - Foreign-born population, excluding population born at sea	
# Margin of Error; WORLD REGION OF BIRTH OF FOREIGN BORN - Foreign-born population, excluding population born at sea	
# Estimate; WORLD REGION OF BIRTH OF FOREIGN BORN - Foreign-born population, excluding population born at sea - Europe	
# Margin of Error; WORLD REGION OF BIRTH OF FOREIGN BORN - Foreign-born population, excluding population born at sea - Europe	
# Estimate; WORLD REGION OF BIRTH OF FOREIGN BORN - Foreign-born population, excluding population born at sea - Asia	
# Margin of Error; WORLD REGION OF BIRTH OF FOREIGN BORN - Foreign-born population, excluding population born at sea - Asia	
# Estimate; WORLD REGION OF BIRTH OF FOREIGN BORN - Foreign-born population, excluding population born at sea - Africa	
# Margin of Error; WORLD REGION OF BIRTH OF FOREIGN BORN - Foreign-born population, excluding population born at sea - Africa	
# Estimate; WORLD REGION OF BIRTH OF FOREIGN BORN - Foreign-born population, excluding population born at sea - Oceania	
# Margin of Error; WORLD REGION OF BIRTH OF FOREIGN BORN - Foreign-born population, excluding population born at sea - Oceania	
# Estimate; WORLD REGION OF BIRTH OF FOREIGN BORN - Foreign-born population, excluding population born at sea - Latin America	
# Margin of Error; WORLD REGION OF BIRTH OF FOREIGN BORN - Foreign-born population, excluding population born at sea - Latin America	
# Estimate; WORLD REGION OF BIRTH OF FOREIGN BORN - Foreign-born population, excluding population born at sea - Northern America	
# Margin of Error; WORLD REGION OF BIRTH OF FOREIGN BORN - Foreign-born population, excluding population born at sea - Northern America	
# Estimate; LANGUAGE SPOKEN AT HOME - Population 5 years and over	
# Margin of Error; LANGUAGE SPOKEN AT HOME - Population 5 years and over	
# Estimate; LANGUAGE SPOKEN AT HOME - Population 5 years and over - English only	
# Margin of Error; LANGUAGE SPOKEN AT HOME - Population 5 years and over - English only	
# Estimate; LANGUAGE SPOKEN AT HOME - Population 5 years and over - Language other than English	
# Margin of Error; LANGUAGE SPOKEN AT HOME - Population 5 years and over - Language other than English	
# Estimate; LANGUAGE SPOKEN AT HOME - Population 5 years and over - Language other than English - Speak English less than "very well"	
# Margin of Error; LANGUAGE SPOKEN AT HOME - Population 5 years and over - Language other than English - Speak English less than "very well"	
# Estimate; LANGUAGE SPOKEN AT HOME - Population 5 years and over - Spanish	
# Margin of Error; LANGUAGE SPOKEN AT HOME - Population 5 years and over - Spanish	
# Estimate; LANGUAGE SPOKEN AT HOME - Population 5 years and over - Spanish - Speak English less than "very well"	
# Margin of Error; LANGUAGE SPOKEN AT HOME - Population 5 years and over - Spanish - Speak English less than "very well"	
# Estimate; LANGUAGE SPOKEN AT HOME - Population 5 years and over - Other Indo-European languages	
# Margin of Error; LANGUAGE SPOKEN AT HOME - Population 5 years and over - Other Indo-European languages	
# Estimate; LANGUAGE SPOKEN AT HOME - Population 5 years and over - Other Indo-European languages - Speak English less than "very well"	
# Margin of Error; LANGUAGE SPOKEN AT HOME - Population 5 years and over - Other Indo-European languages - Speak English less than "very well"	
# Estimate; LANGUAGE SPOKEN AT HOME - Population 5 years and over - Asian and Pacific Islander languages	
# Margin of Error; LANGUAGE SPOKEN AT HOME - Population 5 years and over - Asian and Pacific Islander languages	
# Estimate; LANGUAGE SPOKEN AT HOME - Population 5 years and over - Asian and Pacific Islander languages - Speak English less than "very well"	
# Margin of Error; LANGUAGE SPOKEN AT HOME - Population 5 years and over - Asian and Pacific Islander languages - Speak English less than "very well"	
# Estimate; LANGUAGE SPOKEN AT HOME - Population 5 years and over - Other languages	
# Margin of Error; LANGUAGE SPOKEN AT HOME - Population 5 years and over - Other languages	
# Estimate; LANGUAGE SPOKEN AT HOME - Population 5 years and over - Other languages - Speak English less than "very well"	
# Margin of Error; LANGUAGE SPOKEN AT HOME - Population 5 years and over - Other languages - Speak English less than "very well"	
# Estimate; ANCESTRY - Total population	
# Margin of Error; ANCESTRY - Total population	
# Estimate; ANCESTRY - Total population - American	
# Margin of Error; ANCESTRY - Total population - American	
# Estimate; ANCESTRY - Total population - Arab	
# Margin of Error; ANCESTRY - Total population - Arab	
# Estimate; ANCESTRY - Total population - Czech	
# Margin of Error; ANCESTRY - Total population - Czech	
# Estimate; ANCESTRY - Total population - Danish	
# Margin of Error; ANCESTRY - Total population - Danish	
# Estimate; ANCESTRY - Total population - Dutch	
# Margin of Error; ANCESTRY - Total population - Dutch	
# Estimate; ANCESTRY - Total population - English	
# Margin of Error; ANCESTRY - Total population - English	
# Estimate; ANCESTRY - Total population - French (except Basque)	
# Margin of Error; ANCESTRY - Total population - French (except Basque)	
# Estimate; ANCESTRY - Total population - French Canadian	
# Margin of Error; ANCESTRY - Total population - French Canadian	
# Estimate; ANCESTRY - Total population - German	
# Margin of Error; ANCESTRY - Total population - German	
# Estimate; ANCESTRY - Total population - Greek	
# Margin of Error; ANCESTRY - Total population - Greek	
# Estimate; ANCESTRY - Total population - Hungarian	
# Margin of Error; ANCESTRY - Total population - Hungarian	
# Estimate; ANCESTRY - Total population - Irish	
# Margin of Error; ANCESTRY - Total population - Irish	
# Estimate; ANCESTRY - Total population - Italian	
# Margin of Error; ANCESTRY - Total population - Italian	
# Estimate; ANCESTRY - Total population - Lithuanian	
# Margin of Error; ANCESTRY - Total population - Lithuanian	
# Estimate; ANCESTRY - Total population - Norwegian	
# Margin of Error; ANCESTRY - Total population - Norwegian	
# Estimate; ANCESTRY - Total population - Polish	
# Margin of Error; ANCESTRY - Total population - Polish	
# Estimate; ANCESTRY - Total population - Portuguese	
# Margin of Error; ANCESTRY - Total population - Portuguese	
# Estimate; ANCESTRY - Total population - Russian	
# Margin of Error; ANCESTRY - Total population - Russian	
# Estimate; ANCESTRY - Total population - Scotch-Irish	
# Margin of Error; ANCESTRY - Total population - Scotch-Irish	
# Estimate; ANCESTRY - Total population - Scottish	
# Margin of Error; ANCESTRY - Total population - Scottish	
# Estimate; ANCESTRY - Total population - Slovak	
# Margin of Error; ANCESTRY - Total population - Slovak	
# Estimate; ANCESTRY - Total population - Subsaharan African	
# Margin of Error; ANCESTRY - Total population - Subsaharan African	
# Estimate; ANCESTRY - Total population - Swedish	
# Margin of Error; ANCESTRY - Total population - Swedish	
# Estimate; ANCESTRY - Total population - Swiss	
# Margin of Error; ANCESTRY - Total population - Swiss	
# Estimate; ANCESTRY - Total population - Ukrainian	
# Margin of Error; ANCESTRY - Total population - Ukrainian	
# Estimate; ANCESTRY - Total population - Welsh	
# Margin of Error; ANCESTRY - Total population - Welsh	
# Estimate; ANCESTRY - Total population - West Indian (excluding Hispanic origin groups)	
# Margin of Error; ANCESTRY - Total population - West Indian (excluding Hispanic origin groups)

def construct_design_matrix(year, demographics, county):

	
	fileStr = 'demographic_csvs/ACS_' + str('%02d') % (year%100) + '_1YR_DP2_with_ann.csv'
	print fileStr
	with open(fileStr, 'rb') as csvfile:
		spamreader = csv.reader(csvfile)
		designArray = []

		for index, row in enumerate(spamreader):
		
			if(row[2]==county):

				nextFeatureVector = []
				for dem in demographics:
					nextFeatureVector.append(row[dem])

				designArray.append(nextFeatureVector)

		print np.matrix(designArray)

construct_design_matrix(2007, [10,11,12], "Alameda County, California")

# with open('demographic_csvs/ACS_07_1YR_DP2_with_ann.csv', 'rb') as csvfile:
# 	spamreader = csv.reader(csvfile)

# 	designMatrix = construct_design_matrix(spamreader)

# 	print designMatrix
# # 
# list of rows in order
# specify which issues looking at
# specify which counties looking at
# year, yes/no

