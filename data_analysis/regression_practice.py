import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

x = np.arange(10).reshape(-1,1)
y = np.array([0,0,0,0,1,1,1,1,1,1])

model = LogisticRegression(solver='liblinear', C=10, random_state=0)

model.fit(x,y)

#model predictions

print(model.predict_proba(x))
#print(model.predict(x))

print(model.score(x,y))

#print(confusion_matrix(y, model.predict(x)))
#print(classification_report(y, model.predict(x)))

plt.scatter(x, y, c=y, cmap='rainbow')
plt.title("Scatter Plot of Logistics Regression")
plt.plot(x, model.predict_proba(x))
plt.show()