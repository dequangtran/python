###
""" Key Differences from Linear Regression
Output: Predicts probabilities (0 to 1) instead of continuous values
Model: Uses a logistic (sigmoid) function to squash outputs between 0 and 1
Use Case: Classification (e.g., pass/fail) rather than predicting numbers
Prediction: predict_proba() gives probabilities; predict() gives class labels (0 or 1 based on a 0.5 threshold)

How It Works
Logistic Regression fits a curve like this:

Probability = 1 / (1 + e^-(mx + b))
Where m is the slope (coef_) and b is the intercept (intercept_)
If probability > 0.5, it predicts 1; otherwise, 0 """

#
# Import required libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import os

# Read data from CSV file
try:
    data = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'student_data.csv'))
except FileNotFoundError:
    print("Error: 'student_data.csv' file not found. Please create it with 'hours,pass' columns.")
    exit()

# Prepare the data
X = data[['hours']].values  # 2D array for input (hours studied)
y = data['pass'].values     # 1D array for output (0 = fail, 1 = pass)

# Create and train the logistic regression model
# Logistic regression is a statistical method used for binary classification tasks, 
# where the goal is to predict the probability that an instance belongs to a given class or not. 
# It is a supervised machine learning algorithm that analyzes the relationship between a dependent 
# variable and one or more independent variables.

#Types of Logistic Regression: There are three main types of logistic regression models:
# 1. Binary Logistic Regression: Used when the dependent variable has two possible outcomes (e.g., spam or not spam).
# 2. Multinomial Logistic Regression: Used when the dependent variable has three or more unordered outcomes (e.g., predicting the genre of a movie).
# 3. Ordinal Logistic Regression: Used when the dependent variable has three or more ordered outcomes (e.g., rating scales from 1 to 5).

model = LogisticRegression()
model.fit(X, y)

# Make predictions for new values
X_test = np.array([[0.5], [2.5], [4.5]])
probabilities = model.predict_proba(X_test)[:, 1]  # Probability of passing (class 1)
predictions = model.predict(X_test)                # Final 0/1 prediction

# Print results
print("Model Parameters:")
print(f"Slope (coefficient): {model.coef_[0][0]:.2f}")
print(f"Intercept: {model.intercept_[0]:.2f}")
print("\nPredictions:")
for i, (prob, pred) in enumerate(zip(probabilities, predictions)):
    print(f"Hours: {X_test[i][0]}, Probability of Passing: {prob:.2f}, Prediction: {pred}")

# Visualize the data and decision boundary
plt.scatter(X, y, color='blue', label='Training data from file')
X_range = np.linspace(0, 6, 100).reshape(-1, 1)
y_prob = model.predict_proba(X_range)[:, 1]
plt.plot(X_range, y_prob, color='red', label='Probability curve')
plt.axhline(y=0.5, color='gray', linestyle='--', label='Decision boundary (0.5)')
plt.xlabel('Hours Studied')
plt.ylabel('Pass Probability')
plt.title('Logistic Regression: Pass/Fail Prediction')
plt.legend()
plt.show()