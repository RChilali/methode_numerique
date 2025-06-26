import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv('resultTables/numResultClean.csv')

table1 = df[df.code_presentation == 1]
table2 = df[df.code_presentation == 2]
table3 = df[df.code_presentation == 3]
table4 = df[df.code_presentation == 4]

table1 = table1[['Unnamed: 0', 'code_module', 'code_presentation', 'id_student', 'highest_education', 'age_band',
                 'num_of_prev_attempts', 'disability', 'final_result', '25348', '25349', '25350', '25351', '25352',
                 '25353', 'exam']]
table2 = table2[['Unnamed: 0', 'code_module', 'code_presentation', 'id_student', 'highest_education', 'age_band',
                 'num_of_prev_attempts', 'disability', 'final_result', '25351', '25352',
                 '25362', '25363', '25365', '25366', 'exam']]
table3 = table3[['Unnamed: 0', 'code_module', 'code_presentation', 'id_student', 'highest_education', 'age_band',
                 'num_of_prev_attempts', 'disability', 'final_result', '25342', '25343', '25344', '25345', '25346',
                 '25347', 'exam']]
table4 = table4[['Unnamed: 0', 'code_module', 'code_presentation', 'id_student', 'highest_education', 'age_band',
                 'num_of_prev_attempts', 'disability', 'final_result', '25355', '25356', '25357', '25358', '25359',
                 '25360', 'exam']]

# rename columns
table1 = table1.rename(
    columns={'25348': 'asse1', '25349': 'asse2', '25350': 'asse3', '25351': 'asse4', '25352': 'asse5',
             '25353': 'asse6'})
table2 = table2.rename(
    columns={'25351': 'asse1', '25352': 'asse2', '25362': 'asse3', '25363': 'asse4', '25365': 'asse5',
             '25366': 'asse6'})
table3 = table3.rename(
    columns={'25342': 'asse1', '25343': 'asse2', '25344': 'asse3', '25345': 'asse4', '25346': 'asse5',
             '25347': 'asse6'})
table4 = table4.rename(
    columns={'25355': 'asse1', '25356': 'asse2', '25357': 'asse3', '25358': 'asse4', '25359': 'asse5',
             '25360': 'asse6'})

# Union tables
table_final = pd.concat([table1, table2, table3, table4], ignore_index=True)

table_final.to_csv('intermediateTables/table_merged_final.csv', index=False)

# Some combinations of 6 features in different orders
paramCombinations = [['asse1', 'asse2', 'asse3', 'asse4', 'asse5', 'asse6'],
                     ['asse1', 'asse2', 'asse3', 'asse4', 'asse6', 'asse5'],
                     ['asse1', 'asse2', 'asse3', 'asse5', 'asse4', 'asse6'],
                     ['asse1', 'asse2', 'asse3', 'asse5', 'asse6', 'asse4'],
                     ['asse1', 'asse2', 'asse3', 'asse6', 'asse4', 'asse5'],
                     ['asse2', 'asse1', 'asse3', 'asse4', 'asse5', 'asse6'],
                     ['asse2', 'asse3', 'asse4', 'asse5', 'asse6', 'asse1'],
                     ['asse2', 'asse5', 'asse1', 'asse6', 'asse4', 'asse3'],
                     ['asse2', 'asse5', 'asse4', 'asse3', 'asse6', 'asse1'],
                     ['asse3', 'asse1', 'asse4', 'asse6', 'asse2', 'asse5'],
                     ['asse3', 'asse1', 'asse4', 'asse6', 'asse5', 'asse2'],
                     ['asse3', 'asse1', 'asse5', 'asse2', 'asse4', 'asse6'],
                     ['asse3', 'asse2', 'asse1', 'asse6', 'asse5', 'asse4'],
                     ['asse3', 'asse2', 'asse5', 'asse1', 'asse4', 'asse6'],
                     ['asse3', 'asse2', 'asse5', 'asse1', 'asse6', 'asse4']
                     ]

i = 1
for param in paramCombinations:
    resTab = []
    for toRemove in range(6):
        table_final_num = pd.read_csv('intermediateTables/table_merged_final.csv')
        param.pop()
        table_final_num = table_final_num.drop(param, axis=1)

        X = table_final_num.drop('exam', axis=1)
        y = table_final_num['exam']

        # Splitting the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=42)

        rf = RandomForestRegressor()
        rf.fit(X_train, y_train)
        y_pred = rf.predict(X_test)
        score = rf.score(X_test, y_test)
        resTab.append(((6 - len(param)), score))

    dfRes = pd.DataFrame(resTab, columns=['id', 'score'])
    dfRes.to_csv('resultTables/tableRes/table_res_rf' + str(i) + '.csv', index=False)
    i += 1
