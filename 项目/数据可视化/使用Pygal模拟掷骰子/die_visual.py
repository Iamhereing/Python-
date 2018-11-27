import pygal
from die import Die

die = Die()

results = []
for roll_num in range(1000): # 设置投骰子的次数
    result = die.roll() # 每次投骰子结果
    results.append(result) # 将投骰子的结果放到列表

frequencies = [] # 分析结果
for value in range(1, die.num_sides+1):
    frequency = results.count(value) # 计算每个数出现的次数
    frequencies.append(frequency)

hist = pygal.Bar() # 对结果进行可视化

hist.title = "Results of rolling one D6 1000 times." # 设置直方图的标题
hist.x_labels = ['1', '2', '3', '4', '5', '6'] # 将掷骰子的可能结果用作x轴的标签
hist.x_title = "Result" # 设置xy轴的标题
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies) # 添加指定标签和列表
hist.render_to_file('die_visual.svg') # 将图表渲染成一个SVG文件，这种文件的扩展名必须为.svg