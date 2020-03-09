# -*- coding:utf-8 -*-
# Author:gaoy
# Time  :2020/3/2 下午 2:21
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    # 初始化飞船并设置其初位置
    def __init__(self, ai_settings, screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.ship_set = ai_settings
        # 飞船移动标识位
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load(self.ship_set.ship_address)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每搜飞船放置在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 50
        # print(self.screen_rect.bottom)

        # 初始化center与bottom
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

    def blitme(self):
        # 在制定位置绘制飞船
        self.screen.blit(self.image, self.rect)

    # 根据移动标志位状态调整飞船的位置
    def update(self):
        # 更新飞船的center值，而不是rect值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ship_set.ship_speed
            # print('cent', self.center)
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ship_set.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.bottom -= self.ship_set.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ship_set.ship_speed
        # 根据self.center,self.bottom 更新rect对象
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom


    # 让飞船在屏幕上居中
    def center_ship(self):
        self.center = self.screen_rect.centerx
        self.bottom = self.screen_rect.bottom - 50





