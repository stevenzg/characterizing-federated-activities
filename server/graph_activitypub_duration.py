import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'activitypub_inbox_create.csv'
data = pd.read_csv(file_path)

# Calculate the Interquartile Range (IQR) to define outliers
Q1 = data['duration'].quantile(0.25)
Q3 = data['duration'].quantile(0.75)
IQR = Q3 - Q1

# Define the lower and upper bounds for non-outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter the data to exclude outliers
filtered_data = data[(data['duration'] > 30) & (data['duration'] <= 100)]

# Create a histogram for the filtered 'duration' data
plt.figure(figsize=(10, 6))
plt.hist(filtered_data['duration'], bins=30, edgecolor='black', color='#00467f')
plt.title('Distribution of Duration (Excluding Outliers)')
plt.xlabel('Duration (ms)')
plt.ylabel('Frequency')
plt.grid(True)

# Show the plot
plt.show()

# Calculate statistical values
mean_duration = filtered_data['duration'].mean()
std_dev_duration = filtered_data['duration'].std()
median_duration = filtered_data['duration'].median()
q1_duration = filtered_data['duration'].quantile(0.25)
q3_duration = filtered_data['duration'].quantile(0.75)

# Print results
print(f"Mean Duration: {mean_duration}")
print(f"Standard Deviation: {std_dev_duration}")
print(f"Median Duration: {median_duration}")
print(f"Q1 Duration: {q1_duration}")
print(f"Q3 Duration: {q3_duration}")
