# Creates table with code_module, id_assessment, assessment_type == Exam, id_student, score
# Students' exam scores by modules
# There are only results of 'DDD' module
import pandas as pd
from time import time

before = time()

# Dataset values
studentAssessment = pd.read_csv('dataset/studentAssessment.csv')
studentInfo = pd.read_csv('dataset/studentInfo.csv')
assessment = pd.read_csv('dataset/assessments.csv')

assessment = assessment.dropna()
studentAssessment = studentAssessment.drop(columns=["date_submitted", "is_banked"])
assessment = assessment.drop(columns=["date", "weight", "code_presentation"])

# Students with 'Withdraw' status hadn't finished module
studentInfo = studentInfo[studentInfo.final_result != 'Withdraw']

# code_module,id_assessment,assessment_type
# Exam identifiers from every module
assessmentExam = assessment[assessment.assessment_type == 'Exam']
assessmentExam.to_csv('intermediateTables/assessmentsExam.csv', index=False)

# (2095) code_module,id_assessment,assessment_type,id_student,score
# Student scores of every exam
examJoin = pd.merge(assessmentExam, studentAssessment, on='id_assessment')
examJoin.to_csv('intermediateTables/examJointure.csv', index=False)

# (2159) code_module,id_student,exam
result = pd.merge(examJoin, studentInfo, on=['id_student', 'code_module'])
result = result.drop(columns=['gender', 'region', 'imd_band', 'studied_credits',
                              'id_assessment', 'assessment_type', 'code_presentation',
                              'highest_education', 'age_band', 'num_of_prev_attempts',
                              'final_result', 'disability'])
result = result.rename(columns={'score': 'exam'})
result.to_csv('resultTables/resultExamOnly.csv', index=False)

after = time()
print("examonly.py finished in ", after - before, " seconds")
