# Creates dictionaries to every string value in table result
# Translates result every character result value to numeric value
import pandas as pd
from time import time

before = time()

result = pd.read_csv('resultTables/result.csv')

code_module_mapping = {
    'AAA': 1,
    'BBB': 2,
    'CCC': 3,
    'DDD': 4,
    'EEE': 5,
    'FFF': 6,
    'GGG': 7
}
age_band_mapping = {
    '55<=': 1,
    '35-55': 2,
    '0-35': 3
}
code_presentation_mapping = {
    '2013J': 1,
    '2014J': 2,
    '2013B': 3,
    '2014B': 4
}
disability_mapping = {
    'N': 1,
    'Y': 2
}
final_result_mapping = {
    'Pass': 1,
    'Withdrawn': 2,
    'Fail': 3,
    'Distinction': 4
}
highest_education_mapping = {
    'HE Qualification': 1,
    'A Level or Equivalent': 2,
    'Lower Than A Level': 3,
    'Post Graduate Qualification': 4,
    'No Formal quals': 5
}

result['code_module'].replace(code_module_mapping, inplace=True)
result['age_band'].replace(age_band_mapping, inplace=True)
result['code_presentation'].replace(code_presentation_mapping, inplace=True)
result['disability'].replace(disability_mapping, inplace=True)
result['final_result'].replace(final_result_mapping, inplace=True)
result['highest_education'].replace(highest_education_mapping, inplace=True)

result.to_csv('resultTables/numResult.csv', index=False)

after = time()
print("mappingResultToNumeric.py finished in ", after - before, " seconds")
