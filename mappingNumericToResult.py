# Creates dictionaries to every string value in table result
# Translates numResult numeric value  to  every character result value
import pandas as pd
from time import time

before = time()

result = pd.read_csv('resultTables/numResultClean.csv')

code_module_mapping = {1: 'AAA', 2: 'BBB', 3: 'CCC', 4: 'DDD', 5: 'EEE', 6: 'FFF', 7: 'GGG'}

age_band_mapping = {1: '55<=', 2: '35-55', 3: '0-35'}

code_presentation_mapping = {1: '2013J', 2: '2014J', 3: '2013B', 4: '2014B'}

disability_mapping = {1: 'N', 2: 'Y'}

final_result_mapping = {1: 'Pass', 2: 'Withdrawn', 3: 'Fail', 4: 'Distinction'}

highest_education_mapping = {1: 'HE Qualification', 2: 'A Level or Equivalent', 3: 'Lower Than A Level',
                             4: 'Post Graduate Qualification', 5: 'No Formal quals'}

result['code_module'].replace(code_module_mapping, inplace=True)
result['age_band'].replace(age_band_mapping, inplace=True)
result['code_presentation'].replace(code_presentation_mapping, inplace=True)
result['disability'].replace(disability_mapping, inplace=True)
result['final_result'].replace(final_result_mapping, inplace=True)
result['highest_education'].replace(highest_education_mapping, inplace=True)

result.to_csv('resultTables/mergedTestNoNum.csv', index=False)

after = time()
print("mappingNumericToResult.py finished in ", after - before, " seconds")
