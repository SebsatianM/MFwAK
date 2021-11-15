import settings
from circlesClass import Circle
from circlesClass import screen as screen
import pygame
import random as rd 

disks = []

pygame.init()
clock = pygame.time.Clock()

screen.fill((255,255,255))

for x in range(settings.CIRCLES_NUMBER):
    disks.append(Circle())
    disks[x].drawCircle()
    pygame.display.update()  
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            pygamme.quit()

    dT = clock.tick(30) * .0001 * settings.FPS
    screen.fill((255,255,255))

    for disk in disks:
        disk.moveCircles2(dT)
        disk.drawCircle()  
        
    pygame.display.flip()