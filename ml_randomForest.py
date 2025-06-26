import numpy as np
import pandas as pd
from time import time
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import confusion_matrix, mean_squared_error, mean_absolute_error


# Function to convert labels into intervals
def convert_labels_to_intervals(labels):
    intervals = []
    for label in labels:
        if label == 0:
            intervals.append("0-10")
        elif label == 1:
            intervals.append("10-20")
        elif label == 2:
            intervals.append("20-30")
        elif label == 3:
            intervals.append("30-40")
        elif label == 4:
            intervals.append("40-50")
        elif label == 5:
            intervals.append("50-60")
        elif label == 6:
            intervals.append("60-70")
        elif label == 7:
            intervals.append("70-80")
        elif label == 8:
            intervals.append("80-90")
        elif label == 9:
            intervals.append("90-100")
    return intervals


before = time()
accuracyRes = []

numResultClean = pd.read_csv('resultTables/numResultClean.csv')

X = numResultClean.drop('exam', axis=1)
y = numResultClean['exam']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=42)

rf = RandomForestRegressor()
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
score = rf.score(X_test, y_test)
accuracyRes.append(score)

df = pd.DataFrame({'RandomForest_Result': accuracyRes})
df.to_csv('resultTables/resultRandomForest.csv')

y_test = pd.qcut(y_test, q=10, labels=False, duplicates='drop')
y_pred = pd.qcut(y_pred, q=10, labels=False, duplicates='drop')

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Convert real labels and predictions into intervals
y_true_intervals = convert_labels_to_intervals(y_test)
y_pred_intervals = convert_labels_to_intervals(y_pred)

# Calculate confusion matrix using intervals
cm = confusion_matrix(y_true_intervals, y_pred_intervals)

fig, ax = plt.subplots()

# Show confusion matrix using blue color palette
im = ax.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
plt.colorbar(im)

# Define axes labels
classes = np.unique(y_true_intervals)
ax.set(xticks=np.arange(len(classes)),
       yticks=np.arange(len(classes)),
       xticklabels=classes,
       yticklabels=classes,
       title='Confusion matrix',
       ylabel='Real values',
       xlabel='Predicted values')

# Show colors of cells in matrix
thresh = cm.max() / 2.
for i in range(len(classes)):
    for j in range(len(classes)):
        ax.text(j, i, format(cm[i, j], 'd'),
                ha="center", va="center",
                color="white" if cm[i, j] > thresh else "black")

plt.tight_layout()
plt.show()

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print("### Random Forest ###")
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("Score:", score)

after = time()
print("ml_randomForest.py finished in ", after - before, " seconds")
