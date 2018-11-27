import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()  # 调用fill_walk（），填充点

    plt.figure(dpi=128, figsize=(20,12)) # 设置绘图窗口的尺寸

    point_numbers = list(range(rw.num_points)) # 使点数生成一个列表
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
                cmap=plt.cm.Blues, edgecolors='none', s=1)
    # 颜色范围是这个列表，是用蓝色进行颜色映射 ，没有外轮廓颜色
    # 列表的作用是使颜色根据点的顺序来

    plt.scatter(0, 0, c='green', edgecolors='none', s=100) # 设置起点的位置 及颜色和点数
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    # 设置终点的位置及颜色和点数

    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    # 隐藏坐标轴

    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break
