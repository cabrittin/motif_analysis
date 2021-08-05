import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
import csv

df = pd.read_csv('ffl_common_occurrence.csv')
#print(df["FFL?"])

with open("ffl_common_occurrence.csv", "r") as inp:
    read = csv.reader(inp)
    list = list(read)


i = 1
binary = []
while i < len(list):
    element = list[i]
    binary.append(element[1])
    
    i = i + 1
#print(len(binary))
    

x = np.arange(len(binary)).reshape(-1,1)
y = np.array(binary)

model = LogisticRegression(solver='liblinear', C=10, random_state=0)

model.fit(x,y)

#model predictions

print(model.predict_proba(x))
print(model.predict(x))

print(model.score(x,y))

print(confusion_matrix(y, model.predict(x)))
print(classification_report(y, model.predict(x)))

plt.scatter(x, y, c=y, cmap='rainbow')
plt.title("Scatter Plot of Logistics Regression")
plt.plot(x, model.predict_proba(x))
plt.show()