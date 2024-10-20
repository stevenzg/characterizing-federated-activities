import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file
df = pd.read_csv('./domain_distribution.csv')

# Sort the dataframe by user_count in descending order
df_sorted = df.sort_values('user_count', ascending=True)

# Calculate the cumulative sum of user_count
df_sorted['cumulative_users'] = df_sorted['user_count'].cumsum()

# Calculate the total number of users
total_users = df_sorted['user_count'].sum()

# Calculate the cumulative percentage
df_sorted['cumulative_percentage'] = df_sorted['cumulative_users'] / total_users * 100

# Create the CDF plot
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(df_sorted) + 1), df_sorted['cumulative_percentage'], color='#00467f')
plt.title('CDF of User Count across Instances')
plt.xlabel('Number of Instances')
plt.ylabel('Cumulative Percentage of Users')
plt.grid(True)

# Add percentage labels on y-axis
plt.yticks(range(0, 101, 10), [f'{i}%' for i in range(0, 101, 10)])

# Show the plot
plt.tight_layout()
plt.show()

# Print some statistics
print(f"Total number of domains: {len(df)}")
print(f"Total number of users: {total_users}")
print(f"Domain with most users: {df_sorted.iloc[0]['domain']} ({df_sorted.iloc[0]['user_count']} users)")
print(f"Domain with least users: {df_sorted.iloc[-1]['domain']} ({df_sorted.iloc[-1]['user_count']} users)")
