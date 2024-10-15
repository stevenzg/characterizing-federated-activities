import pandas as pd

# Read the most_followed_users.csv file
df_most_followed = pd.read_csv('./most_followed_users.csv')

# Calculate the total number of users in most_followed_users.csv
total_users_mfu = len(df_most_followed)

print(f"Total number of users in most_followed_users.csv: {total_users_mfu}")

# Read the user_count_distribution.csv file
df_user_count = pd.read_csv('./user_count_distribution.csv')

# Calculate the total user count from user_count_distribution.csv
total_users_ucd = (df_user_count['user_count'] * df_user_count['domain_count']).sum()

print(f"Total user count from user_count_distribution.csv: {total_users_ucd}")

# Read the domain_distribution.csv file
df_domain = pd.read_csv('./domain_distribution.csv')

# Calculate the total user count from domain_distribution.csv
total_users_dd = df_domain['user_count'].sum()

print(f"Total user count from domain_distribution.csv: {total_users_dd}")

# Compare the results
if total_users_mfu == total_users_ucd == total_users_dd:
    print("The total user counts from all three files match.")
else:
    print("The total user counts from the three files do not match.")
    print(f"Differences:")
    print(f"most_followed_users.csv vs user_count_distribution.csv: {abs(total_users_mfu - total_users_ucd)}")
    print(f"most_followed_users.csv vs domain_distribution.csv: {abs(total_users_mfu - total_users_dd)}")
    print(f"user_count_distribution.csv vs domain_distribution.csv: {abs(total_users_ucd - total_users_dd)}")
