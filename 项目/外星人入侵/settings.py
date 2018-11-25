class Settings(): # 存储该游戏所有设置的类

    def __init__(self):
        self.screen_width = 1200 # 自定义屏幕的宽
        self.screen_height = 800 # 自定义屏幕的高
        self.bg_color = (230, 230, 230) # 自定义屏幕的背景色

        self.ship_limit = 3 # 飞船数量

        self.bullet_width = 3 # 子弹的宽度
        self.bullet_height = 15 # 子弹的高度
        self.bullet_color = 60, 60, 60 # 子弹的颜色
        self.bullets_allowed = 3 # 设置子弹的个数为3个

        self.fleet_drop_speed = 10  # 外星人向下移动的速度


        self.speedup_scale = 1.1
        # speedup_scale,用于控制游戏节奏的加快速度：2表示玩家每
        # 提高一个等级，游戏的节奏就翻倍;1表示游戏节奏始终不变。
        # 将其设置为1.1能够将游戏节奏提高到够快，让游戏既有难度，
        # 又u并非不可完成。
        self.score_scale = 1.5 # 外星人点数的提高速度

        self.initialize_dynamic_settings() # 载入这个函数

    def initialize_dynamic_settings(self): # 以初始化随游戏进行而变化的速度属性
        self.ship_speed_factor = 1.5 # 飞船移动的像素的初始值
        self.bullet_speed_factor = 3 # 子弹速度的初始值
        self.alien_speed_factor = 1 # 设置外星人的初始速度

        self.fleet_direction = 1  # fleet_direction为1表示向右移，-1向左移

        self.alien_points = 50 # 指定每个外星人的点数

    def increase_speed(self): # 每当玩家提高一个等级时，使用这个
                                                # 函数来提高飞船 子弹和外星人的速度
        self.ship_speed_factor *= self.speedup_scale  # 都乘以节奏的加快速度
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        # 外星人的点数=外星人初始点数×提高速度

