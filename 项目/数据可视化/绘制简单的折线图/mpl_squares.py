import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.plot(input_values, squares, linewidth=5) # 导入列表，linewidth决定线条的粗细

plt.title("Square Numbers", fontsize=24) # 设置图表标题并设置其字号
plt.xlabel("Value", fontsize=14) # 设置X轴上的文本并设置其字号
plt.ylabel("Square of Value", fontsize=14) # 设置Y轴上的文本并设置其字号

plt.tick_params(axis='both', labelsize=14) # 设置X轴和Y轴上的刻度，并设置其字号

plt.show()