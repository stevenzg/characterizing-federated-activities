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

# Create subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

# Plot PDF
ax1.plot(bin_centers, hist)
ax1.set_title('PDF of User Count accross instances')
ax1.set_xlabel('User Count')
ax1.set_ylabel('Probability Density Function of User Count')

# Plot CDF
ax2.plot(bin_centers, cdf)
ax2.set_title('CDF of User Count accross instances')
ax2.set_xlabel('User Count')
ax2.set_ylabel('Cumulative Probability Function of User Count')

# Adjust layout and display
plt.tight_layout()
plt.show()

# Print some statistics
print(f"Total number of domains: {len(df)}")
print(f"Mean user count: {user_counts.mean():.2f}")
print(f"Median user count: {user_counts.median():.2f}")
print(f"Max user count: {user_counts.max()}")
print(f"Min user count: {user_counts.min()}")
