import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader) # 显示文件即列表的第一行信息

    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        # 将包含日期信息的数据row[0]转换为datetime对象
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

fig = plt.figure(dpi=128, figsize=(10, 6)) # 加载像素为128,宽高为10×6的屏幕
plt.plot(dates, highs, c='red')  # 将列表传输给plot，并将点设置为红色

plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16) # 设置XY轴的属性及字号大小及刻度属性
fig.autofmt_xdate() # 绘制在X轴上斜的日期标签
plt.ylabel("Temperature(F)",fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()



''' 
       for index,column_header in enumerate(header_row):
        # enumerate()获取每个元素的索引及其值
        print(index, column_header)
'''
