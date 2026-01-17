#Import required libraries
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#Sample training data
#X is our input (features), y is our output (what we want to predict)
X = np.array([[1], [2], [3], [4], [5]]) #Input numbers
y = np.array([2, 4, 6, 8, 10]) #Ouput: double the input

#Create training model
model = LinearRegression()
model.fit(X, y)

#Make predictions
X_test = np.array([[6], [5], [4]])
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
