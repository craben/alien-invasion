# -*- coding:utf-8 -*-
# Author:gaoy
# Time  :2020/3/3  上午 11:00

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载外星人图像，并设置其rect属性
        self.image = pygame.image.load(ai_settings.alien_address)
        self.rect = self.image.get_rect()
        # 初始化位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 存储外星人的准确位置
        self.x = float(self.rect.x)
        # self.y = float(self.rect.y)

    # 绘制外星人
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    # 向左或右移动外星人
    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    # 检查外星人是否撞到边缘,如果撞到边缘返回True
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

