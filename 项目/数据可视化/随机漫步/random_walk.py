from random import choice

class RandomWalk(): # 创建随机漫步的类

    def __init__(self, num_points=5000): #默认点数设置为5000
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]
        #创建两个用于存储X和Y值的列表，并让每次漫步都从点（0,0）出发

    def fill_walk(self): # 计算随机漫步包含的所有点

        while len(self.x_values) < self.num_points:
            # 当X值的点数小于默认指定的点数时即未完成随机漫步时
            x_direction = choice([1, -1]) # 随机选择x轴的方向，即是向右走还是向左走
            x_distance = choice([0, 1, 2, 3, 4]) # 随机选择在列表里的距离
            x_step = x_direction * x_distance # 点的步数就是方向乘以距离，y轴同理

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0: # 如果在原地踏步，则继续这个循环
                continue

            next_x = self.x_values[-1] + x_step # 下一步X的值=计算好的X值的距离和方向+X值列表中最后一个值
            next_y = self.y_values[-1] + y_step # Y值同理

            self.x_values.append(next_x) # 在X值列表中增加这个值
            self.y_values.append(next_y)

