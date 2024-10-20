import pandas as pd
import matplotlib.pyplot as plt

# 读取 CSV 文件
file_path = 'domain_request_counts.csv'
data = pd.read_csv(file_path)

# 排序，获取最活跃的前 20 个域名
top_domains = data.sort_values(by='count', ascending=False).head(20)

# 绘制前 20 个最活跃域名的柱状图
plt.figure(figsize=(15, 10))
fig, ax1 = plt.subplots(figsize=(15, 8))

# 绘制请求数量的柱状图
ax1.bar(top_domains['domain'], top_domains['count'], color='#00467f', label='Request Count')
ax1.set_xlabel("Instance")
ax1.set_ylabel("Request Count", color='#00467f')
ax1.tick_params(axis='y', labelcolor='#00467f')

# 创建第二个y轴
ax2 = ax1.twinx()

# 绘制用户数量的线图
ax2.plot(top_domains['domain'], top_domains['user_count'], color='orange', marker='o', label='User Count')
ax2.set_ylabel("User Count", color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

# 在用户数量线图上显示具体的用户数
for i, v in enumerate(top_domains['user_count']):
    ax2.text(i, v, str(v), ha='center', va='bottom', color='orange')

# 设置x轴标签
plt.xticks(rotation=45, ha='right')
fig.autofmt_xdate()  

# 设置标题和图例
plt.title("Top 20 Active Instances by Request Count and User Count")
fig.legend(loc="upper right", bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)

plt.tight_layout()
plt.show()

# 分析所有域名请求数量的分布
plt.figure(figsize=(8, 5))
plt.scatter(data.index, data['count'], alpha=0.5, color='#00467f')
plt.title("Distribution of Request Counts Across Instances")
plt.xlabel("Number of Instances")
plt.ylabel("Request Count")
plt.xscale('log')
plt.yscale('log')
plt.tight_layout()
plt.show()

# 新增图表：比较前20个域名的user_count和followers_count
plt.figure(figsize=(15, 8))
fig, ax1 = plt.subplots(figsize=(15, 8))

# 绘制user_count的线图
ax1.plot(top_domains['domain'], top_domains['user_count'], color='#00467f', marker='o', label='User Count')
ax1.set_xlabel("Instance")
ax1.set_ylabel("User Count", color='#00467f')
ax1.tick_params(axis='y', labelcolor='#00467f')

# 创建第二个y轴
ax2 = ax1.twinx()

# 绘制followers_count的线图
ax2.plot(top_domains['domain'], top_domains['followers_count'], color='orange', marker='s', label='Followers Count')
ax2.set_ylabel("Followers Count", color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

# 在user_count线图上显示具体的数值
for i, v in enumerate(top_domains['user_count']):
    ax1.text(i, v, str(v), ha='center', va='bottom', color='#00467f', rotation=45)

# 在followers_count线图上显示具体的数值
for i, v in enumerate(top_domains['followers_count']):
    ax2.text(i, v, f'{v:,}', ha='center', va='bottom', color='orange', rotation=45)

# 设置x轴标签
plt.xticks(rotation=45, ha='right')
fig.autofmt_xdate()

# 设置标题和图例
plt.title("Top 20 Active Instances: User Count vs Followers Count")
fig.legend(loc="upper right", bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)

plt.tight_layout()
plt.show()
