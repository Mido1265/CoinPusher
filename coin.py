import pygame
import math
from typing import Union
from abc import ABCMeta, abstractmethod
from Common_Variables import *



# マップ(親クラス)
class Coin(metaclass=ABCMeta):

    # オブジェクト生成時自動格納するリストを設定する関数
    @classmethod
    def set_list(cls, list):
        cls.list = list

    # オブジェクトを映すカメラを設定する関数
    @classmethod
    def set_camera(cls, camera):
        cls.camera = camera

    def __init__(self, x, y, dx, dy, r, color, mass):
        self.x = x * self.camera.size#x座標
        self.y = y * self.camera.size#y座標
        self.r = r * self.camera.size#半径
        self.dx = dx # 1step先の相対x座標
        self.dy = dy # 1step先の相対y座標
        self.color = color # コインの色
        self.mass = mass # 質量(1が基準)
        
    # 座標を移動させる関数
    def move_coin(self, x, y):
        self.x += x
        self.y += y
    
    # 座標を変更する関数
    def warp_coin(self, x, y):
        self.x = x
        self.y = y

    # 状態の更新
    @abstractmethod
    def update(self, time):
        pass

    # 描画
    @abstractmethod
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.r)

################################################################

# 普通のコイン
class Normal_coin(Coin):
    def __init__(self, x, y, dx, dy):
        # self.str = ""
        self.list.append(self)
        super().__init__(x, y,  dx, dy, NORMALCOIN_R, NORMALCOIN_COLOR, NORMALCOIN_MASS)

    def update(self, time):
        # Pusherの上から落ちたかどうかの判定
        # if self.x - self.r <= 0 or self.x + self.r >= width:
        #     self.dx = -self.dx
        # if self.y - self.r <= 0 or self.y + self.r >= height:
        #     self.dy = -self.dy

        # 摩擦力の適用
        self.dx *= 1 - COFF
        self.dy *= 1 - COFF

        # 速度が一定以下の場合、円を停止させる
        if abs(self.dx) < 0.1:
            self.dx = 0
        if abs(self.dy) < 0.1:
            self.dy = 0

        # 速度の更新
        self.x += self.dx
        self.y += self.dy

    def draw(self, screen, x, y):
        # コンクリート地面
        pygame.draw.circle(screen, self.color, (self.x + x, self.y + y), self.r)

# class Rare_coin(Coin):
#     def __init__(self, x, y, r, dx, dy, color):
#         # self.str = ""
#         self.list.append(self)
#         super().__init__(x, y, r, dx, dy, color)
#         self.color = color

#     def update(self, time):
#         pass

#     def draw(self, screen, x, y):
#         # コンクリート地面
#         pygame.draw.circle(screen, self.color, (self.x + x, self.y + y), self.r)

        
    