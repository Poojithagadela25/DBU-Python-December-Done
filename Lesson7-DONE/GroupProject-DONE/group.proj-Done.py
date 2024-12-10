# Objective: Apply data science concepts on a dataset of your choice.

# Tasks:
    # Acquire, clean, and preprocess data.
    # Perform EDA and visualize key insights.
	# Build and evaluate a machine learning model.

# Requirements:
    # Work on this as a group (Same team as the previous GIT exercise).
    # Use a dataset that is not used in the class.
    # Use at least 3 different visualization techniques.
    # Use at least 1 different machine learning algorithms.
    # Use at least 2 different evaluation metrics.
    # Use at least 2 different preprocessing techniques.

# Submission Timeline:
    # Submit the code and a report in 3 weeks.
    # The report should include:
        # Introduction to the dataset.
        # Data cleaning and preprocessing steps.
        # EDA and key insights.
        # Machine learning model building and evaluation.
        # Conclusion.
        # References (if any).



# SOLUTION CODE :-

# Importing necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

"""# Step 1: Data Acquisition and Preprocessing"""

# Loading the Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
df.head()

# Display basic information about the dataset
df.info()

df.head()

df.describe()

"""**Data Cleaning and Preprocessing**"""

# Handling the missing values
imputer = SimpleImputer(strategy="most_frequent")
df['Age'] = imputer.fit_transform(df[['Age']])

# Droping columns that won't be used in model
df = df.drop(columns=['Name', 'Ticket', 'Cabin'])

# Handling the categorical features
label_encoder = LabelEncoder()
df['Sex'] = label_encoder.fit_transform(df['Sex'])
df['Embarked'] = label_encoder.fit_transform(df['Embarked'])

# Splitting the dataset into training and testing sets
X = df.drop(columns=['Survived'])
y = df['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

"""# Step 2: Exploratory Data Analysis (EDA)"""

# Visualizing the distribution of 'Age' and 'Fare'
plt.figure(figsize=(12, 6))
sns.histplot(df['Age'], kde=True, bins=30, color='blue')
plt.title('Age Distribution')
plt.show()

# Visualizing the survival rate
sns.countplot(x='Survived', data=df, palette='Set2')
plt.title('Survival Count')
plt.show()

# Correlation heatmap to understand relationships between features
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

"""# Step 3: Machine Learning Model Building and Evaluation"""

# Initializing and training the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Making predictions
y_pred = model.predict(X_test)

# Evaluation metrics: Accuracy, Confusion Matrix, and Classification Report
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.title('Confusion Matrix')
plt.show()

# Classification Report
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Step 4: Conclusion mentioned in Report.