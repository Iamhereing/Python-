import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader) # 显示文件即列表的第一行信息

    dates, highs , lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            # 将包含日期信息的数据row[0]转换为datetime对象
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing date')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


fig = plt.figure(dpi=128, figsize=(10, 6)) # 加载像素为128,宽高为10×6的屏幕
plt.plot(dates, highs, c='red', alpha=0.5)  # 将列表传输给plot，并将点设置为红色
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title("Daily high and lows temperatures - 2014\nDeath Valley, CA", fontsize=24)
plt.xlabel('', fontsize=16) # 设置XY轴的属性及字号大小及刻度属性
fig.autofmt_xdate() # 绘制在X轴上斜的日期标签
plt.ylabel("Temperature(F)",fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
