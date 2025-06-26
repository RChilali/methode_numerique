# Creates the correlation matrix from resultTable with only numeric values
from time import time
import pandas as pd
import matplotlib.pyplot as plt

before = time()
# Input : table with numeric values
numResult = pd.read_csv('resultTables/numResult.csv')

numResult = numResult.drop(
    ['1752', '1753', '1754', '1755', '1756', '1758', '1759', '1760', '1761', '1762', '14984', '14985', '14986',
     '14987', '14988', '14989', '14991', '14992', '14993', '14994', '14995', '15008', '15009', '15010', '15011',
     '15012', '15013', '15015', '15016', '15017', '15018', '15019', '30714', '30715', '30716', '30717', '34873',
     '34874', '34875', '34876', '34877', '34878', '34879', '34880', '34881', '34882', '34883', '34884', '37415',
     '37416', '37417', '37418', '37419', '37420', '37421', '37422', '37423', '37425', '37426', '37427', '37428',
     '37429', '37430', '37431', '37432', '37433', '37435', '37436', '37437', '37438', '37439', '37440', '37441',
     '37442', '37443'], axis=1)

result = numResult.corr()

result.to_csv('intermediateTables/correlationMatrix.csv', index=True)
numResult.to_csv('resultTables/numResultClean.csv', index=True)

# Plotting the correlation matrix
f = plt.figure(figsize=(19, 15))
plt.matshow(result.corr(), fignum=f.number)
plt.xticks(range(result.select_dtypes(['number']).shape[1]), result.select_dtypes(['number']).columns, fontsize=14,
           rotation=45)
plt.yticks(range(result.select_dtypes(['number']).shape[1]), result.select_dtypes(['number']).columns, fontsize=14)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
plt.title('Correlation Matrix', fontsize=16)
plt.show()

after = time()
print("correlationMatrix.py finished in ", after - before, "seconds")
