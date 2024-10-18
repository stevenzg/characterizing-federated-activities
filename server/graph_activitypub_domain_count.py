import pandas as pd
import matplotlib.pyplot as plt

# 读取 CSV 文件
file_path = 'domain_request_counts.csv'
data = pd.read_csv(file_path)

# 排序，获取最活跃的前 10 个域名
top_domains = data.sort_values(by='count', ascending=False).head(10)

# 绘制前 10 个最活跃域名的柱状图
plt.figure(figsize=(10, 6))
plt.bar(top_domains['domain'], top_domains['count'], color='#00467f')
plt.xticks(rotation=45, ha='right')
plt.title("Top 10 Active Instances by Request Count")
plt.xlabel("Instance")
plt.ylabel("Request Count")
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
