import pandas as pd
import matplotlib.pyplot as plt

# 读取 CSV 文件
file_path = 'user_request_counts.csv'
data = pd.read_csv(file_path)

# 获取前 20 个最活跃的用户
top_users = data.sort_values(by='count', ascending=False).head(20)

# 绘制前 20 个最活跃用户的柱状图
fig, ax1 = plt.subplots(figsize=(15, 8))

# 绘制请求数量的柱状图
ax1.bar(top_users['username'], top_users['count'], color='#00467f')
ax1.set_xlabel("Username")
ax1.set_ylabel("Request Count", color='#00467f')
ax1.tick_params(axis='y', labelcolor='#00467f')

# 创建第二个y轴
ax2 = ax1.twinx()

# 绘制followers数量的折线图
ax2.plot(top_users['username'], top_users['followers'], color='orange', marker='o')
ax2.set_ylabel("Followers Count", color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

# 在线上显示对应 followers 的数量
for i, v in enumerate(top_users['followers']):
    ax2.text(i, v, str(v), ha='center', va='bottom', color='orange')

plt.title("Top 20 Active Users by Request Count and Their Followers")
plt.xticks(rotation=45, ha='right')
fig.autofmt_xdate()  

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
