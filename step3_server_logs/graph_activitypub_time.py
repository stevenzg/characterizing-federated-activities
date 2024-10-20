import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Read the CSV file
df = pd.read_csv('activitypub_inbox_create.csv')

# Convert the 'time' column to datetime
df['time'] = pd.to_datetime(df['time'], format='%b %d %H:%M:%S')

# Extract hour and minute
df['hour'] = df['time'].dt.hour
df['minute'] = df['time'].dt.minute

# Create a histogram of the distribution of times
plt.figure(figsize=(12, 6))
plt.hist2d(df['hour'], df['minute'], bins=(24, 60), cmap='YlOrRd')
plt.colorbar(label='Frequency')

plt.title('Distribution of ActivityPub Inbox Create Times')
plt.xlabel('Hour of Day')
plt.ylabel('Minute of Hour')

plt.xticks(range(0, 24, 2))
plt.yticks(range(0, 60, 10))

plt.tight_layout()
plt.show()

# Calculate and print some statistics
total_entries = len(df)
unique_days = df['time'].dt.date.nunique()
busiest_hour = df['hour'].mode().values[0]
busiest_minute = df['minute'].mode().values[0]

print(f"Total entries: {total_entries}")
print(f"Number of unique days: {unique_days}")
print(f"Busiest hour of the day: {busiest_hour}:00")
print(f"Busiest minute of the hour: {busiest_minute}")

# Create a line plot of activity over time
df['datetime'] = pd.to_datetime(df['time'].dt.strftime('%Y-%m-%d %H:%M'))
activity_counts = df.groupby('datetime').size().resample('10min').sum().fillna(0)

plt.figure(figsize=(12, 6))
plt.plot(activity_counts.index, activity_counts.values, color='#00467f')

plt.title('ActivityPub Inbox Create Activity Over Time')
plt.xlabel('Time')
plt.ylabel('Number of Activities')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
