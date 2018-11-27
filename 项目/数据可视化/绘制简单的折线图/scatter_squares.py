import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=2)
# 设置点的坐标及点的像素大小,c是点的颜色，edgecolor是外轮廓的颜色

plt.title("Square Numbers", fontsize=24) # 设置图表的标题及字号
plt.xlabel("Value", fontsize=14) # 设置X值的属性及其文本字号
plt.ylabel("Square of Value", fontsize=14) # 设置Y值的属性及其文本字号

plt.tick_params(axis='both', which='major', labelsize=14) # 设置XY的刻度及其大小

plt.axis([0, 1100, 0, 1100000]) # 设置每个坐标轴的取值范围

plt.show()