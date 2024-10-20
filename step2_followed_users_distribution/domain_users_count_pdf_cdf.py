import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file
df = pd.read_csv('./domain_distribution.csv')

# Extract user_count data
user_counts = df['user_count']

# Calculate PDF using numpy's histogram function
hist, bin_edges = np.histogram(user_counts, bins='auto', density=True)
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

# Calculate CDF
cdf = np.cumsum(hist) * np.diff(bin_edges)

# Plot PDF
plt.figure(figsize=(10, 6))
plt.plot(bin_centers, hist)
plt.title('PDF of User Count across instances')
plt.xlabel('User Count')
plt.ylabel('Probability Density Function of User Count')
plt.show()

# Plot CDF
plt.figure(figsize=(10, 6))
plt.plot(bin_centers, cdf)
plt.title('CDF of User Count across instances')
plt.xlabel('User Count')
plt.ylabel('Cumulative Probability Function of User Count')
plt.show()

# Print some statistics
print(f"Total number of domains: {len(df)}")
print(f"Mean user count: {user_counts.mean():.2f}")
print(f"Median user count: {user_counts.median():.2f}")
print(f"Max user count: {user_counts.max()}")
print(f"Min user count: {user_counts.min()}")
