# -*- coding:utf-8 -*-
# Author:gaoy
# Time  :2020/3/3  下午 9:03


class GameStates():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        # 让游戏开始处于非活动状态
        self.game_active = False
        self.high_score = 0
        self.reset_stats()

    def reset_stats(self):
        self.ships_life = self.ai_settings.ship_limit
        # 得分设置
        self.score = 0
