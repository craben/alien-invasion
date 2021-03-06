# -*- coding:utf-8 -*-
# Author:gaoy
# Time  :2020/3/3  下午 9:50

import pygame.font


class Button():
    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # 初始化按钮的尺寸
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        # 创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.bottom = self.screen_rect.bottom / 2
        # 按钮的标签只需要创建一次
        self.prep_msg(msg)


    def prep_msg(self, msg):
        # font.render()将存储在msg中的文本转化为图像，True是启用反锯齿功能
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

