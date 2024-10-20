import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'user_request_counts.csv'
data = pd.read_csv(file_path)

# Calculate the Interquartile Range (IQR) to define outliers
Q1 = data['count'].quantile(0.25)
Q3 = data['count'].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds for non-outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter the data to exclude outliers
filtered_data = data[(data['count'] >= lower_bound) & (data['count'] <= upper_bound)]

# Create a histogram for the filtered 'count' data
plt.figure(figsize=(10, 6))
plt.hist(filtered_data['count'], bins=30, edgecolor='black', color='#00467f')
plt.title('Distribution of User Request Counts (Excluding Outliers)')
plt.xlabel('Request Count')
plt.ylabel('Frequency')
plt.grid(True)

# Show the plot
plt.show()

# Calculate statistical values
mean_count = filtered_data['count'].mean()
std_dev_count = filtered_data['count'].std()
median_count = filtered_data['count'].median()
q1_count = filtered_data['count'].quantile(0.25)
q3_count = filtered_data['count'].quantile(0.75)

# Print results
print(f"Mean Count: {mean_count}")
print(f"Standard Deviation: {std_dev_count}")
print(f"Median Count: {median_count}")
print(f"Q1 Count: {q1_count}")
print(f"Q3 Count: {q3_count}")
