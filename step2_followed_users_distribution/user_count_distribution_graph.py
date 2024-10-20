import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
df = pd.read_csv('user_count_distribution.csv')

# Plot 1: Bar plot for domains with more than 50 users
plt.figure(figsize=(12, 8))
top_domains = df[df['user_count'] > 0]
sns.barplot(x='user_count', y='domain_count', data=top_domains)
plt.title('Distribution of Instances by Number of Users')
plt.xlabel('Number of Users')
plt.ylabel('Number of Instances')
plt.tight_layout()
plt.show()

# Plot 2: Distribution of domains by user count (log scale)
plt.figure(figsize=(12, 8))
sns.histplot(data=df, x='user_count', weights='domain_count', bins=50, log_scale=(True, True))
plt.title('Distribution of Instances by User Count')
plt.xlabel('Number of Users (log scale)')
plt.ylabel('Number of Instances (log scale)')
plt.tight_layout()
plt.show()

print("Graphs generated and displayed")
