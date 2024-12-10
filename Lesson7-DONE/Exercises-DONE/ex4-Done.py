# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the dataset
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Exercise 4: generate a scatter plot between two features
# Generating scatter plot between 'sepal length (cm)' and 'sepal width (cm)'
x = df['sepal length (cm)']
y = df['sepal width (cm)']

plt.scatter(x, y)
plt.title('Scatter plot of Sepal Length vs Sepal Width')  # Title of the plot
plt.xlabel('Sepal Length (cm)')  # Label for the x-axis
plt.ylabel('Sepal Width (cm)')   # Label for the y-axis
plt.show()  # Display the plot
