import pandas as pd
import matplotlib.pyplot as plt

# 加载数据
data = pd.read_csv('activitypub_domain_duration.csv')
request_counts = pd.read_csv('domain_request_counts.csv')

# 合并数据
merged_data = pd.merge(data, request_counts, on='domain', how='left')

# 选取中位数最小的 20 个域名
bottom_20_median = merged_data.nsmallest(20, 'median_duration')

# 设置图形和轴（中位数最小的 20 个）
fig, ax1 = plt.subplots(figsize=(16,8))

# 绘制平均值、中位数和最小值，使用不同颜色
ax1.plot(bottom_20_median['domain'], bottom_20_median['avg_duration'], label='Average Duration', marker='o', color='#00467f')
ax1.plot(bottom_20_median['domain'], bottom_20_median['median_duration'], label='Median Duration', marker='x', color='green')
ax1.plot(bottom_20_median['domain'], bottom_20_median['min_duration'], label='Minimum Duration', marker='s', color='red')

# 设置左侧 y 轴
ax1.set_xlabel('Instance')
ax1.set_ylabel('Duration')
ax1.tick_params(axis='y')

# 创建右侧 y 轴
ax2 = ax1.twinx()
ax2.plot(bottom_20_median['domain'], bottom_20_median['count'], label='Request Count', marker='D', color='purple')
ax2.set_ylabel('Request Count')
ax2.tick_params(axis='y')

# 在 request count 的线上显示对应的 request count
for i, count in enumerate(bottom_20_median['count']):
    ax2.annotate(str(count), (i, count), textcoords="offset points", xytext=(0,5), ha='center')

# 调整 x 轴标签旋转角度和对齐方式
plt.xticks(rotation=45, ha='right')
fig.autofmt_xdate()  # 自动调整日期标签

# 添加标题
plt.title('Bottom 20 Domains by Median Duration: Comparison of Durations and Request Count')

# 添加图例
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

# 显示图形
plt.tight_layout()
plt.show()

# 选取中位数最大的 20 个域名
top_20_median = merged_data.nlargest(20, 'median_duration')

# 设置图形和轴（中位数最大的 20 个）
fig, ax1 = plt.subplots(figsize=(16,8))

# 绘制平均值、中位数和最小值，使用不同颜色
ax1.plot(top_20_median['domain'], top_20_median['avg_duration'], label='Average Duration', marker='o', color='#00467f')
ax1.plot(top_20_median['domain'], top_20_median['median_duration'], label='Median Duration', marker='x', color='green')
ax1.plot(top_20_median['domain'], top_20_median['min_duration'], label='Minimum Duration', marker='s', color='red')

# 设置左侧 y 轴
ax1.set_xlabel('Instance')
ax1.set_ylabel('Duration')
ax1.tick_params(axis='y')

# 创建右侧 y 轴
ax2 = ax1.twinx()
ax2.plot(top_20_median['domain'], top_20_median['count'], label='Request Count', marker='D', color='purple')
ax2.set_ylabel('Request Count')
ax2.tick_params(axis='y')

# 在 request count 的线上显示对应的 request count
for i, count in enumerate(top_20_median['count']):
    ax2.annotate(str(count), (i, count), textcoords="offset points", xytext=(0,5), ha='center')

# 调整 x 轴标签旋转角度和对齐方式
plt.xticks(rotation=45, ha='right')
fig.autofmt_xdate()  # 自动调整日期标签

# 添加标题
plt.title('Top 20 Domains by Median Duration: Comparison of Durations and Request Count')

# 添加图例
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

# 显示图形
plt.tight_layout()
plt.show()

# 选取所有 duration 中位数附近的 20 个域名
median_duration = merged_data['median_duration'].median()
middle_20_domains = merged_data.iloc[(merged_data['median_duration'] - median_duration).abs().argsort()[:20]]

# 设置图形和轴（中位数附近的 20 个域名）
fig, ax1 = plt.subplots(figsize=(16,8))

# 绘制平均值、中位数和最小值，使用不同颜色
ax1.plot(middle_20_domains['domain'], middle_20_domains['avg_duration'], label='Average Duration', marker='o', color='#00467f')
ax1.plot(middle_20_domains['domain'], middle_20_domains['median_duration'], label='Median Duration', marker='x', color='green')
ax1.plot(middle_20_domains['domain'], middle_20_domains['min_duration'], label='Minimum Duration', marker='s', color='red')

# 设置左侧 y 轴
ax1.set_xlabel('Instance')
ax1.set_ylabel('Duration')
ax1.tick_params(axis='y')

# 创建右侧 y 轴
ax2 = ax1.twinx()
ax2.plot(middle_20_domains['domain'], middle_20_domains['count'], label='Request Count', marker='D', color='purple')
ax2.set_ylabel('Request Count')
ax2.tick_params(axis='y')

# 在 request count 的线上显示对应的 request count
for i, count in enumerate(middle_20_domains['count']):
    ax2.annotate(str(count), (i, count), textcoords="offset points", xytext=(0,5), ha='center')

# 调整 x 轴标签旋转角度和对齐方式
plt.xticks(rotation=45, ha='right')
fig.autofmt_xdate()  # 自动调整日期标签

# 添加标题
plt.title('20 Domains Near Median Duration: Comparison of Durations and Request Count')

# 添加图例
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

# 显示图形
plt.tight_layout()
plt.show()
