import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'activitypub_inbox_create.csv'
data = pd.read_csv(file_path)

# Calculate the Interquartile Range (IQR) to define outliers
Q1 = data['db'].quantile(0.25)
Q3 = data['db'].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds for non-outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter the data to exclude outliers
filtered_data = data[(data['db'] > lower_bound) & (data['db'] <= upper_bound)]

# Create a histogram for the filtered 'db' data
plt.figure(figsize=(10, 6))
plt.hist(filtered_data['db'], bins=30, edgecolor='black', color='#00467f')
plt.title('Distribution of DB Values (Excluding Outliers)')
plt.xlabel('DB Values')
plt.ylabel('Frequency')
plt.grid(True)

# Show the plot
plt.show()

# Create a histogram for the data above Q3
above_q3_data = data[data['db'] > Q3]
plt.figure(figsize=(10, 6))
plt.hist(above_q3_data['db'], bins=30, edgecolor='black', color='#ff6600')
plt.title('Distribution of DB Values Above Q3')
plt.xlabel('DB Values')
plt.ylabel('Frequency')
plt.grid(True)

# Show the plot
plt.show()

# Calculate statistical values
mean_db = filtered_data['db'].mean()
std_dev_db = filtered_data['db'].std()
median_db = filtered_data['db'].median()
q1_db = filtered_data['db'].quantile(0.25)
q3_db = filtered_data['db'].quantile(0.75)

# Calculate max and min db values from the original data
max_db = data['db'].max()
min_db = data['db'].min()

# Print results
print(f"Mean DB Value: {mean_db}")
print(f"Standard Deviation: {std_dev_db}")
print(f"Median DB Value: {median_db}")
print(f"Q1 DB Value: {q1_db}")
print(f"Q3 DB Value: {q3_db}")
print(f"Maximum DB Value: {max_db}")
print(f"Minimum DB Value: {min_db}")

# Calculate and print statistics for data above Q3
mean_above_q3 = above_q3_data['db'].mean()
std_dev_above_q3 = above_q3_data['db'].std()
median_above_q3 = above_q3_data['db'].median()

print("\nStatistics for data above Q3:")
print(f"Mean DB Value: {mean_above_q3}")
print(f"Standard Deviation: {std_dev_above_q3}")
print(f"Median DB Value: {median_above_q3}")

# Get the top 50 requests with the highest db values
top_50_db = data.nlargest(50, 'db')

# Write the top 50 requests to a CSV file
output_file = 'top_50_db_requests.csv'
top_50_db.to_csv(output_file, index=False)

print(f"\nTop 50 requests with highest db values have been written to {output_file}")
