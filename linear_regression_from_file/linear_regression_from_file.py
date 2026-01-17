import pandas as pd
import numpy as np
import os
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#Read from file
try:
    input = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.csv')
    data = pd.read_csv(input)
except FileNotFoundError:
    print("Error: 'input.csv' file not found.  Please create it with 'input, output' columns")
    exit()

x = data['input'].values
X = data[['input']].values #Double brackets to make it 2D
Y = data['output'].values
y = data[['output']].values 

model = LinearRegression()
model.fit(X, y)

X_test = np.array([[6], [7], [8]])
predictions = model.predict(X_test)


#Print results
print("\n")
print("Linear Regression has the formular as y = mx + b where m is the slope/coefficient and b is the Intercept")

for i, pred in enumerate(predictions):
    print(f"Input: {X_test[i][0]}, Predicted output: {pred}")
print(f"coef/slope: {model.coef_}")
print(f"intercept: {model.intercept_}")

#Optional: Visualize the data and predictions
plt.scatter(X, y, color='blue', label='Training data')
plt.plot(X_test, predictions, color='red', label='Predictions')
plt.xlabel('Input')
plt.ylabel('Ouput')
plt.title('Simple AI Linear Regression from Grok')
plt.legend()
plt.show()