# Import libraries
import pandas as pd

# Create a DataFrame with missing values
data = {'Country': ['USA', 'UK', 'Canada', None],
        'GDP': [21.43, 2.83, 1.74, 0.3]}
df = pd.DataFrame(data)

# Exercise 2: clean the missing values and sort by GDP
df_cleaned = df.dropna(subset=['Country'])  # Drop rows with missing 'Country'
df_sorted = df_cleaned.sort_values(by='GDP', ascending=False)  # Sort by GDP in descending order

# Exercise 3: calculate the total GDP
total_gdp = df['GDP'].sum()

# Display results
print("Sorted DataFrame by GDP:")
print(df_sorted)
print("\nTotal GDP:", total_gdp)
