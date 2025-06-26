import pandas as pd
from matplotlib import pyplot as plt

for i in range(1, 5):
    df = pd.read_csv('resultTables/tableRes/table_res_rf' + str(i) + '.csv')
    plt.plot(df['id'], df['score'])
    plt.title('Залежність точності методу від кількості характеристик (' + str(i) + ')', fontsize=16)
    plt.xlabel('Кількість характеристик')
    plt.ylabel('Точність методу випадкового лісу')
    plt.show()
