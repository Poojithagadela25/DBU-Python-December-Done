# Import libraries
import pandas as pd

# Create a DataFrame
data = {'Product': ['A', 'B', 'C'], 'Sales': [100, 200, 300]}
df = pd.DataFrame(data)

# Print DataFrame
print("Original DataFrame:")
print(df)

# Sort by Sales
df_sorted = df.sort_values('Sales', ascending=False)
print("\nDataFrame Sorted by Sales:")
print(df_sorted)

# Exercise 1: modify the script to add a new column for "Profit" and sort by it.

# Adding a new column for Profit
df['Profit'] = [30, 50, 70]

# Print DataFrame with Profit column
print("\nDataFrame with Profit:")
print(df)

# Sort by Profit
df_sorted = df.sort_values('Profit', ascending=False)

# Print the sorted DataFrame
print("\nDataFrame Sorted by Profit:")
print(df_sorted)