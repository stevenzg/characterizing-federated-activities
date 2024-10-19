import pandas as pd
import matplotlib.pyplot as plt

# 加载数据
data = pd.read_csv('activitypub_domain_duration.csv')

# 选取中位数最小的 20 个域名
bottom_20_median = data.nsmallest(20, 'median_duration')

# 设置图形和轴（中位数最小的 20 个）
plt.figure(figsize=(10,6))

# 绘制平均值、中位数和最小值，使用不同颜色
plt.plot(bottom_20_median['domain'], bottom_20_median['avg_duration'], label='Average Duration', marker='o', color='#00467f')
plt.plot(bottom_20_median['domain'], bottom_20_median['median_duration'], label='Median Duration', marker='x', color='green')
plt.plot(bottom_20_median['domain'], bottom_20_median['min_duration'], label='Minimum Duration', marker='s', color='red')

# 调整 x 轴标签旋转角度
plt.xticks(rotation=90)

# 添加标签和标题
plt.xlabel('Domain')
plt.ylabel('Duration')
plt.title('Bottom 20 Domains by Median Duration: Comparison of Average, Median, and Minimum Durations')

# 添加图例
plt.legend()

# 显示图形
plt.tight_layout()
plt.show()

# 选取中位数最大的 20 个域名
top_20_median = data.nlargest(20, 'median_duration')

# 设置图形和轴（中位数最大的 20 个）
plt.figure(figsize=(10,6))

# 绘制平均值、中位数和最小值，使用不同颜色
plt.plot(top_20_median['domain'], top_20_median['avg_duration'], label='Average Duration', marker='o', color='#00467f')
plt.plot(top_20_median['domain'], top_20_median['median_duration'], label='Median Duration', marker='x', color='green')
plt.plot(top_20_median['domain'], top_20_median['min_duration'], label='Minimum Duration', marker='s', color='red')

# 调整 x 轴标签旋转角度
plt.xticks(rotation=90)

# 添加标签和标题
plt.xlabel('Domain')
plt.ylabel('Duration')
plt.title('Top 20 Domains by Median Duration: Comparison of Average, Median, and Minimum Durations')

# 添加图例
plt.legend()

# 显示图形
plt.tight_layout()
plt.show()
