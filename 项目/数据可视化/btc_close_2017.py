import json
import pygal
import math
from itertools import groupby

filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)

dates = []
months = []
weeks = []
weekdays = []
close = []
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))

line_chart = pygal.Line(x_lable_rotation=20, show_minor_x_labels=False)
# 第一个实参让X轴上的日期标签沿顺时针旋转20‘，第二个实参告诉图形
# 不用显示所有的X轴标签
line_chart.title = '收盘价对数变换（￥）'
line_chart.x_labels = dates
N = 20
line_chart.x_labels_major = dates[::N]  # 让X轴坐标每隔20天显示一次
close_log = [math.log10(_) for _ in close] # 半对数，用对数变换剔除非线性趋势
line_chart.add('log收盘价', close_log) # 增加属性标签
line_chart.render_to_file('收盘价对数变换折线图（￥）.svg')

def draw_line(x_date, y_date, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_date, y_date)), key=lambda _: _[0]):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title+'.svg')
    return line_chart