import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'activitypub_inbox_create.csv'
data = pd.read_csv(file_path)

# Calculate the Interquartile Range (IQR) to define outliers
Q1 = data['allocations'].quantile(0.25)
Q3 = data['allocations'].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds for non-outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter the data to exclude outliers
filtered_data = data[(data['allocations'] > lower_bound) & (data['allocations'] <= upper_bound)]

# Create a histogram for the filtered 'allocations' data
plt.figure(figsize=(10, 6))
plt.hist(filtered_data['allocations'], bins=30, edgecolor='black', color='#00467f')
plt.title('Distribution of Allocations (Excluding Outliers)')
plt.xlabel('Allocations')
plt.ylabel('Frequency')
plt.grid(True)

# Show the plot
plt.show()

# Calculate statistical values
mean_allocations = filtered_data['allocations'].mean()
std_dev_allocations = filtered_data['allocations'].std()
median_allocations = filtered_data['allocations'].median()
q1_allocations = filtered_data['allocations'].quantile(0.25)
q3_allocations = filtered_data['allocations'].quantile(0.75)

# Calculate max and min allocations from the original data
max_allocations = data['allocations'].max()
min_allocations = data['allocations'].min()

# Print results
print(f"Mean Allocations: {mean_allocations}")
print(f"Standard Deviation: {std_dev_allocations}")
print(f"Median Allocations: {median_allocations}")
print(f"Q1 Allocations: {q1_allocations}")
print(f"Q3 Allocations: {q3_allocations}")
print(f"Maximum Allocations: {max_allocations}")
print(f"Minimum Allocations: {min_allocations}")
