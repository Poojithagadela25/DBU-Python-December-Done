import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Define dataset size
data_size = 100

# Generate random data for each variable
data = pd.DataFrame({
    'Variable_A': np.random.randn(data_size),  # Normal distribution
    'Variable_B': np.random.rand(data_size),   # Uniform distribution between 0 and 1
    'Variable_C': np.random.randint(0, 100, size=data_size),  # Random integers between 0 and 100
    'Variable_D': np.random.randn(data_size) * 10  # Normal distribution with higher variance
})

# Create a pairplot of the dataset
sns.pairplot(data)

# Show the plot
plt.show()

# Optionally, save the plot as a PNG file
# plt.savefig('pairplot_output.png')
