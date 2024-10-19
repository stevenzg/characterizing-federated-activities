import pandas as pd
import matplotlib.pyplot as plt

# 读取 CSV 文件
file_path = 'user_request_counts.csv'
data = pd.read_csv(file_path)

# 获取前 10 个最活跃的用户
top_users = data.sort_values(by='count', ascending=False).head(10)

# 绘制前 10 个最活跃用户的柱状图
plt.figure(figsize=(12, 6))
plt.bar(top_users['username'], top_users['count'], color='#00467f')
plt.title("Top 10 Active Users by Request Count")
plt.xlabel("Username")
plt.ylabel("Request Count")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 分析 count 的分布
plt.figure(figsize=(10, 6))
plt.hist(data['count'], bins=50, edgecolor='black', color='#00467f', alpha=0.7)
plt.title("Distribution of User Request Counts")
plt.xlabel("Request Count")
plt.ylabel("Frequency")
plt.grid(True, which="both", ls="-", alpha=0.2)
plt.tight_layout()
plt.show()

# 打印统计信息
print("Count Statistics:")
print(data['count'].describe())
