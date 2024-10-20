import pandas as pd

# Read the CSV file
df = pd.read_csv('./domain_distribution.csv')

# Group by user_count and count the domains
grouped = df.groupby('user_count').size().reset_index(name='domain_count')

# Sort by user_count in descending order
grouped = grouped.sort_values('user_count', ascending=False)

# Save the result to a new CSV file
grouped.to_csv('user_count_distribution.csv', index=False, columns=['user_count', 'domain_count'])

print("User count distribution analysis complete. Results saved to 'user_count_distribution.csv'.")
