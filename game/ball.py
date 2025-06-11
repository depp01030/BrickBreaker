import pygame
import math
from game import settings


class Ball:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.radius = 10
        
        # 球的起始位置 (放在畫面底部中間偏上)
        self.x = settings.SCREEN_WIDTH // 2
        self.y = settings.SCREEN_HEIGHT - 100
        
        # 建立球的矩形碰撞區域
        self.rect = pygame.Rect(
            self.x - self.radius, 
            self.y - self.radius,
            self.radius * 2, 
            self.radius * 2
        )
        
        # 球的移動速度與方向
        self.speed = 5
        angle = math.radians(45)
        self.dx = self.speed * math.cos(angle)  # 45度角發射
        self.dy = -self.speed * math.sin(angle)  # 負值表示向上移動
        
        # 球的顏色
        self.color = (255, 255, 0)  # 黃色

    def move(self):
        # 更新球的位置
        self.x += self.dx
        self.y += self.dy
        
        # 更新碰撞檢測用的矩形
        self.rect.centerx = int(self.x)
        self.rect.centery = int(self.y)

    def check_wall_collision(self):
        # 檢查左牆碰撞
        if self.rect.left <= 0:
            self.rect.left = 0
            self.x = self.rect.centerx
            self.dx = abs(self.dx)  # 反彈向右
        
        # 檢查右牆碰撞
        elif self.rect.right >= settings.SCREEN_WIDTH:
            self.rect.right = settings.SCREEN_WIDTH
            self.x = self.rect.centerx
            self.dx = -abs(self.dx)  # 反彈向左
        
        # 檢查上牆碰撞
        if self.rect.top <= 0:
            self.rect.top = 0
            self.y = self.rect.centery
            self.dy = abs(self.dy)  # 反彈向下
        
        # 檢查下牆碰撞 (可以加入遊戲結束邏輯)
        elif self.rect.bottom >= settings.SCREEN_HEIGHT:
            self.rect.bottom = settings.SCREEN_HEIGHT
            self.y = self.rect.centery
            self.dy = -abs(self.dy)  # 反彈向上
            # 這裡可以加入失敗或生命減少的邏輯

    def check_paddle_collision(self, paddle):
        if self.rect.colliderect(paddle.rect):
            # 計算碰撞點在paddle上的相對位置
            hit_pos = (self.rect.centerx - paddle.rect.left) / paddle.rect.width
            
            # 根據碰撞位置改變反彈角度
            angle = math.pi * (0.25 + 0.5 * hit_pos)  # 從15度到75度
            
            # 設置新的速度方向
            self.dx = self.speed * math.cos(angle)
            self.dy = -self.speed * math.sin(angle)  # 負值讓球往上
            
            # 確保球不會卡在paddle裡
            self.rect.bottom = paddle.rect.top
            self.y = self.rect.centery

    def check_bricks_collision(self, bricks):
        # 檢查球是否與任何磚塊碰撞
        for brick in bricks.bricks[:]:  # 使用副本避免迭代時修改
            if self.rect.colliderect(brick.rect):
                # 判斷碰到磚塊的哪一側
                overlap_left = self.rect.right - brick.rect.left
                overlap_right = brick.rect.right - self.rect.left
                overlap_top = self.rect.bottom - brick.rect.top
                overlap_bottom = brick.rect.bottom - self.rect.top
                
                # 找出最小重疊部分
                min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)
                
                # 根據碰撞側更改球的方向
                if min_overlap == overlap_left or min_overlap == overlap_right:
                    self.dx = -self.dx  # 水平反彈
                else:
                    self.dy = -self.dy  # 垂直反彈

                # 產生粒子特效
                if hasattr(self.game, 'spawn_particle_effect'):
                    self.game.spawn_particle_effect(brick.rect.center, brick.color)
                
                # 從磚塊列表中移除被碰撞的磚塊
                bricks.bricks.remove(brick)
                
                # 每次只處理一個碰撞，避免穿過多個磚塊
                break

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)