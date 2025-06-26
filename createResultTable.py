# Main loop of a program
from time import time
import pandas as pd

before = time()

studentAssessment = pd.read_csv('dataset/studentAssessment.csv')
studentInfo = pd.read_csv('dataset/studentInfo.csv')
assessment = pd.read_csv('dataset/assessments.csv')
resultExam = pd.read_csv('resultTables/resultExamOnly.csv')

studentAssessment = studentAssessment.dropna()
assessment = assessment.dropna()

studentAssessment = studentAssessment.drop(columns=["date_submitted", "is_banked"])
assessment = assessment.drop(columns=["date", "weight", "code_presentation"])

studentInfo = studentInfo[studentInfo.final_result != 'Withdrawn']

assessmentWithoutExam = assessment[assessment.assessment_type != 'Exam']
assessmentWithoutExam = assessmentWithoutExam.drop(columns=['code_module'])

assessmentPivot = pd.merge(studentAssessment, assessmentWithoutExam, on='id_assessment')
assessmentPivot = assessmentPivot.pivot_table(index=['id_student'], columns='id_assessment', values='score',
                                              aggfunc='first')
assessmentPivot.to_csv('intermediateTables/assessmentPivot.csv', index=True)

result = pd.merge(studentInfo, assessmentPivot, on='id_student', how='outer')

result = result.merge(resultExam, on=['id_student', 'code_module'], how='outer')
result = result.drop(columns=['gender', 'region', 'imd_band', 'studied_credits'])

result = result.fillna(0)
result = result[result.exam != 0]

result.to_csv('resultTables/result.csv', index=False)

after = time()
print("createResultTable.py finished in ", after - before, " seconds")
