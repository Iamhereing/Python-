import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard(): # 定义得分的一些设置

    def __init__(self, ai_settings, screen, stats): # 包含这些形参，使之能够报告跟踪的值
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score() # 将显示的文本和最高分转换为图像
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        rounded_score = int(round(self.stats.score, -1))
        # 函数round（）通常让小数精确到小数点后多少位，其中小鼠
        # 位数是由第二个实参指定的。若第二个实参为负数，round()
        # 将圆整到最近的10,100,1000等整数倍。此处为整到10的整数倍
        score_str = "{:,}".format(rounded_score)
        # 该处使用一个字符串格式设置指令，它让python将数值转换为
        # 字符串时在其中插入逗号，例如1,000,000
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)
        # 将字符串得分传递给创建图像的render（），为在屏幕上清晰
        # 的显示得分，向该方法传递了屏幕背景色及文本颜色

        self.score_rect = self.score_image.get_rect() # 得分框矩形
        self.score_rect.right = self.screen_rect.right - 20 # 得分框矩形的右边与屏幕右边间隔20个像素
        self.score_rect.top = 20 # 距离屏幕顶部20个像素

    def prep_high_score(self): # 定义最高分的函数
        high_score = int(round(self.stats.high_score, -1)) # 最高分是10的整数
        high_score_str = "{:,}".format(high_score) # 最高分加入逗号
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color, self.ai_settings.bg_color)
                                                                                    # 加载最高分的图像

        self.high_score_rect = self.high_score_image.get_rect() # 载入最高分的矩形框
        self.high_score_rect.centerx = self.screen_rect.centerx # 放在屏幕中央
        self.high_score_rect.top = self.score_rect.top #放在屏幕顶部

    def prep_level(self): # 定义等级的函数
        self.level_image = self.font.render(str(self.stats.level), True,
                                            self.text_color, self.ai_settings.bg_color)
                                                                     # 将等级转换为渲染的图像

        self.level_rect = self.level_image.get_rect() # 加载等级的矩形框
        self.level_rect.right = self.score_rect.right # 将等级的右边与分数的右边重合
        self.level_rect.top = self.score_rect.bottom + 10 # 将等级的矩形与分数的矩形间隔10个像素

    def prep_ships(self): # 显示还剩下多少艘飞船
        self.ships = Group() # 创建飞船编组
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen) # 载入飞船
            ship.rect.x = 10 + ship_number * ship.rect.width # 飞船矩形X值=距离屏幕左边缘10个像素+飞船个数×飞船的宽度
            ship.rect.y = 10 #飞船距离屏幕顶部10个像素
            self.ships.add(ship) # 将每艘飞船加入编组中

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        # 通过方法blit（）将得分图像放在score_rect指定的位置
        self.screen.blit(self.high_score_image, self.high_score_rect)  # 放入最高分的图像
        self.screen.blit(self.level_image, self.level_rect) # 放入等级
        self.ships.draw(self.screen)  # 绘制飞船

