import pygal
from die import Die

die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1000): # 设置投骰子的次数
    result = die_1.roll() + die_2.roll()# 每次投骰子结果
    results.append(result) # 将投骰子的结果放到列表

frequencies = [] # 分析结果
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value) # 计算每个数出现的次数
    frequencies.append(frequency)

hist = pygal.Bar() # 对结果进行可视化

hist.title = "Results of rolling two D6 dice 1000 times." # 设置直方图的标题
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'] # 将掷骰子的可能结果用作x轴的标签
hist.x_title = "Result" # 设置xy轴的标题
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies) # 添加指定标签和列表
hist.render_to_file('dice_visual.svg') # 将图表渲染成一个SVG文件，
                                                             # 这种文件的扩展名必须为.svg