class Settings(): # 存储该游戏所有设置的类

    def __init__(self):
        self.screen_width = 1200 # 自定义屏幕的宽
        self.screen_height = 800 # 自定义屏幕的高
        self.bg_color = (230, 230, 230) # 自定义屏幕的背景色

        self.ship_speed_factor = 1.5 # 飞船移动的像素的初始值
        self.ship_limit = 3 # 飞船数量

        self.bullet_speed_factor = 3 # 子弹速度的初始值
        self.bullet_width = 3 # 子弹的宽度
        self.bullet_height = 15 # 子弹的高度
        self.bullet_color = 60, 60, 60 # 子弹的颜色
        self.bullets_allowed = 3 # 设置子弹的个数为3个

        self.alien_speed_factor = 1 # 设置外星人的初始速度
        self.fleet_drop_speed = 100  # 外星人向下移动的速度
        self.fleet_direction = 1 # fleet_direction为1表示向右移，-1向左移
