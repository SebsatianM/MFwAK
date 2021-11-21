import settings
import random
import pygame
import math
screen = pygame.display.set_mode((settings.SCREEN_W, settings.SCREEN_H))
cx = settings.SCREEN_W/2
cy = settings.SCREEN_H/2
class Circle:
    def __init__(self,r=None,Vx=None,Vy=None,x=None,y=None,c=None,w=None):
        self.r = r if r is not None else random.randint(10, settings.CIRCLE_MAX_RADIUS)
        self.Vx = Vx if Vx is not None else random.uniform(-settings.CIRCLE_MAX_SPEED,settings.CIRCLE_MAX_SPEED)
        self.Vy = Vy if Vy is not None else random.uniform(-settings.CIRCLE_MAX_SPEED,settings.CIRCLE_MAX_SPEED)
        self.xBorderProtect = self.r+settings.BORDER_PADDING+settings.FPS+math.ceil(self.Vx)
        self.yBorderProtect = self.r+settings.BORDER_PADDING+settings.FPS+math.ceil(self.Vy)
        self.x = x if x is not None else random.randint(self.xBorderProtect,settings.SCREEN_W-(self.xBorderProtect))
        self.y = y if y is not None else random.randint(self.yBorderProtect,settings.SCREEN_H-(self.yBorderProtect))
        self.c = c if c is not None else [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
        self.w = w if w is not None else self.r
        self.Vypom = 0
        self.Fx = 0 
        self.Fy = 0
        self.Dx = 0 
        self.Dy = 0  

    def drawCircle(self):
        pygame.draw.circle(screen, self.c,(self.x,self.y),self.r)

    def describe(self):
        print(self.r,self.x,self.y,self.c)

    def moveCircles(self,dT):
        self.x = self.x + self.Vx 
        self.y = self.y + self.Vy 
        self.checkCollision(dT)

    def moveCirclesGravity(self,dT):
        self.x = self.x + self.Vx * dT
        self.y = self.y + self.Vy * dT
        if self.y+self.r > settings.SCREEN_H*0.96:
            self.Vy  = (self.Vy  + settings.g * self.w * dT)*0.9
        else:
            self.Vy  = (self.Vy  + settings.g * self.w * dT)*0.99
        self.checkCollision(dT)
        
    def moveCirclesMassCenter(self,dT):
        pygame.draw.circle(screen,[0,0,0],(math.ceil(settings.SCREEN_W/2),math.ceil(settings.SCREEN_H/2)),50)
        self.R = math.sqrt(pow((cy-self.y),2)+pow((cx-self.x),2))
        self.Fy = -1*((settings.G*settings.CENTER_MASS_WEIGHT*self.w*(self.y-cy))/pow(self.R,3))
        self.Fx = -1*((settings.G*settings.CENTER_MASS_WEIGHT*self.w*(self.x-cx))/pow(self.R,3))

        self.Vx += self.Fx
        self.Vy += self.Fy
        
        if self.x > settings.SCREEN_W or self.x <= 0 and self.y >= settings.SCREEN_H or self.y < 0:
            self.x += self.Vx+(cx-self.x)*0.005
            self.y += self.Vy+(cy-self.y)*0.005
        else: 
            self.x += self.Vx
            self.y += self.Vy

    def moveCirclesAerodynamics(self,dT):
        #Metanol	0,587 η / mPa*s w temp. 20°C
        self.Dx = -6 * math.pi * (0.587 * 0.001 * dT) * self.r * self.Vx
        self.Dy = -6 * math.pi * (0.587 * 0.001 * dT) * self.r * self.Vy
        
        self.Vx += self.Dx
        self.Vy += self.Dy

        self.x += self.Vx
        self.y += self.Vy

        self.checkCollision(dT)

    def checkCollision(self,dT):
        if (self.y - self.r) + self.Vy * dT < 0 or self.y +self.r + self.Vy*dT > settings.SCREEN_H:
            self.Vy = -self.Vy
        if self.x-self.r + self.Vx*dT < 0 or self.x+self.r + self.Vx*dT > settings.SCREEN_W:
            self.Vx = -self.Vx


