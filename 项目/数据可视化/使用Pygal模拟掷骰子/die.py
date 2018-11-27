from random import randint

class Die(): # 定义一个骰子的类

    def __init__(self,num_sides=6): # 设置骰子的面数
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)
    # 方法roll()使用函数randint()来返回一个1和面数之间的随机数。
    # 这个函数可能返回起始值1,，终止值num_sides或这两个值之间的任何整数
