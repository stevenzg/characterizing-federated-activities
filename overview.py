import pandas as pd

# Read the domain_distribution.csv file
df = pd.read_csv('./domain_distribution.csv')

# Count the number of unique domains
domain_count = df['domain'].nunique()

print(f"Total number of unique domains: {domain_count}")
