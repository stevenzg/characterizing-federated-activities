import pandas as pd
from collections import defaultdict

# Read the CSV file
df = pd.read_csv('./most_followed_users.csv')

# Create defaultdicts to store domain statistics
domain_user_count = defaultdict(int)
domain_follower_count = defaultdict(int)

# Iterate through the DataFrame to collect statistics
for _, row in df.iterrows():
    domain = row['domain']
    followers = row['followers']
    
    domain_user_count[domain] += 1
    domain_follower_count[domain] += followers

# Create a new DataFrame with the collected statistics
result_df = pd.DataFrame({
    'domain': list(domain_user_count.keys()),
    'user_count': list(domain_user_count.values()),
    'followers_count': list(domain_follower_count.values())
})

# Sort the DataFrame by user_count in descending order
result_df = result_df.sort_values('user_count', ascending=False)

# Save the result to a new CSV file
result_df.to_csv('domain_distribution.csv', index=False)

print("Domain distribution analysis complete. Results saved to 'domain_distribution.csv'.")
