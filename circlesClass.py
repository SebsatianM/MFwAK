import settings
import random
import pygame
import math
screen = pygame.display.set_mode((settings.SCREEN_W, settings.SCREEN_H))
ay = -settings.g

class Circle:
    def __init__(self):
        self.r = random.randint(10, settings.CIRCLE_MAX_RADIUS)
        self.Vx = random.uniform(-settings.CIRCLE_MAX_SPEED,settings.CIRCLE_MAX_SPEED)
        self.Vy = random.uniform(-settings.CIRCLE_MAX_SPEED,settings.CIRCLE_MAX_SPEED)

        self.xBorderProtect = self.r+settings.BORDER_PADDING+settings.FPS+math.ceil(self.Vx)
        self.yBorderProtect = self.r+settings.BORDER_PADDING+settings.FPS+math.ceil(self.Vy)

        self.x = random.randint(self.xBorderProtect,settings.SCREEN_W-(self.xBorderProtect))
        self.y = random.randint(self.yBorderProtect,settings.SCREEN_H-(self.yBorderProtect))
        self.c = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
        self.w = self.r*1/4
        self.Vypom = 0
        self.F = self.w*-ay*(720-self.y)
    def drawCircle(self):
        pygame.draw.circle(screen, self.c,(self.x,self.y),self.r)

    def describe(self):
        print(self.r,self.x,self.y,self.c)

    def moveCircles(self,dT):
            self.x = self.x + self.Vx * dT
            self.y = self.y + self.Vy * dT

            self.Vy  = (self.Vy  - ay*self.w * dT)

            if (self.y - self.r) + self.Vy *dT< 0 or self.y +self.r + self.Vy*dT > settings.SCREEN_H:
                self.Vy = -self.Vy*0.9
            if self.x-self.r + self.Vx*dT < 0 or self.x+self.r + self.Vx*dT > settings.SCREEN_W:
                self.Vx = -self.Vx


        
    def checkCollision(self,dT):
        pass