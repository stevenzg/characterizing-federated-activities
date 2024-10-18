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

# Calculate statistical values
mean_db = filtered_data['db'].mean()
std_dev_db = filtered_data['db'].std()
median_db = filtered_data['db'].median()
q1_db = filtered_data['db'].quantile(0.25)
q3_db = filtered_data['db'].quantile(0.75)

# Print results
print(f"Mean DB Value: {mean_db}")
print(f"Standard Deviation: {std_dev_db}")
print(f"Median DB Value: {median_db}")
print(f"Q1 DB Value: {q1_db}")
print(f"Q3 DB Value: {q3_db}")
