class GameStats(): # 跟踪游戏的统计信息
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False  # 游戏刚启动是处于非活动状态
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit # 飞船数量
        # 初始化在游戏运行期间可能变化的统计信息
        self.score = 0 # 重置得分