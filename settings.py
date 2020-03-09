# -*- coding:utf-8 -*-
# Author:gaoy
# Time  :2020/3/2  下午 12:17
# 存储《外星入侵》中所有设置类


class Settings():
    # 初始化游戏设置

    def __init__(self):
        # 游戏名称设置
        self.caption = 'Alien Invasion'

        #  屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船图片设置
        self.ship_address = 'image/ship.bmp'
        # 飞船移动因子
        self.ship_speed = 1
        self.ship_limit = 3

        # 外星人图片设置
        self.alien_address = 'image/alien.bmp'
        # 外星人移动因子
        self.alien_speed_factor = 1  # 外星人向左右移动速度
        self.fleet_drop_speed = 10  # 外星人向下移动速度
        self.fleet_direction = 1  # 区分左右方向

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        # 游戏难度调节
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.bullets_allowed = 10
        # 分值
        self.alien_points = 10

    # 提高游戏速度设置
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bullets_allowed *= self.speedup_scale
        self.alien_points = int(self.speedup_scale * self.alien_points)
