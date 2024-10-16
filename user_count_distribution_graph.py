import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
df = pd.read_csv('user_count_distribution.csv')

# Create a figure with two subplots, stacked vertically
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 16))

# Plot 1: Bar plot for domains with more than 50 users
top_domains = df[df['user_count'] > 0]
sns.barplot(x='user_count', y='domain_count', data=top_domains, ax=ax1)
ax1.set_title('Distribution of Instances by Number of Users')
ax1.set_xlabel('Number of Users')
ax1.set_ylabel('Number of Instances')

# Plot 2: Distribution of domains by user count (log scale)
sns.histplot(data=df, x='user_count', weights='domain_count', ax=ax2, bins=50, log_scale=(True, True))
ax2.set_title('Distribution of Instances by User Count')
ax2.set_xlabel('Number of Users (log scale)')
ax2.set_ylabel('Number of Instances (log scale)')

plt.tight_layout()
plt.show()

print("Graph generated and saved as 'user_count_distribution.png'")
