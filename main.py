import settings
from circlesClass import Circle
from circlesClass import screen as screen
import pygame
import pygame_gui
import random as rd 
import math
disks = []

pygame.init()
manager = pygame_gui.UIManager((settings.SCREEN_W, settings.SCREEN_H))

clock = pygame.time.Clock()

items = ["Normal","Gravity","Central mass","Aerodynamics"]

diskNumberSlider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((0,settings.SCREEN_H/20),(settings.SCREEN_W/5,settings.SCREEN_H/20)),
                                            value_range=(1,1000),
                                            start_value=100,
                                            manager=manager)
diskNumberSliderLabel = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0,0),(settings.SCREEN_W/5,settings.SCREEN_H/20)),
                                            text="Disk Number: 1-1000",
                                            parent_element=diskNumberSlider,
                                            manager=manager)

animationTypeSelectList = pygame_gui.elements.UISelectionList(relative_rect=pygame.Rect((settings.SCREEN_W/5,0),(settings.SCREEN_W/5,settings.SCREEN_H/10)),
                                            item_list=items,
                                            allow_multi_select=False,
                                            manager=manager)

hideUI = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((settings.SCREEN_W-(settings.SCREEN_W/5),0),(settings.SCREEN_W/5,settings.SCREEN_H/20)),
                                            text="Hide UI",
                                            manager=manager)

showUI = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((settings.SCREEN_W-(settings.SCREEN_W/5),0),(settings.SCREEN_W/5,settings.SCREEN_H/20)),
                                            text="Show UI",
                                            manager=manager)

startButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((settings.SCREEN_W-(2*(settings.SCREEN_W/5)),0),(settings.SCREEN_W/5,settings.SCREEN_H/20)),
                                            text="Start",
                                            manager=manager)

stopButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((settings.SCREEN_W-(2*(settings.SCREEN_W/5)),0),(settings.SCREEN_W/5,settings.SCREEN_H/20)),
                                            text="Stop",
                                            manager=manager)

screen.fill((255,255,255))
    
showUI.hide()
stopButton.hide()
is_running = True
run_animation = False

while is_running:
    dT = clock.tick(30) * 0.0001 * settings.FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == hideUI:
                    diskNumberSlider.hide()
                    diskNumberSliderLabel.hide()
                    animationTypeSelectList.hide()
                    hideUI.hide()
                    showUI.show()
                    if run_animation == False:
                        startButton.hide()
                    else:
                        stopButton.hide()
                    
                    screen.fill((255,255,255))


                if event.ui_element == showUI:
                    diskNumberSlider.show()
                    diskNumberSliderLabel.show()
                    animationTypeSelectList.show()
                    hideUI.show()
                    showUI.hide()
                    if run_animation == False:
                        startButton.show()
                        stopButton.hide()
                    else:
                        stopButton.show()
                        startButton.hide()

                if event.ui_element == startButton:
                    run_animation = True
                    stopButton.show()
                    startButton.hide()

                if event.ui_element == stopButton:
                    run_animation = False
                    startButton.show()
                    stopButton.hide()
                    

        manager.process_events(event)

   
    diskNumberValue = diskNumberSlider.get_current_value()
    
    if diskNumberValue < len(disks):
        disks=disks[:-len(disks)-diskNumberValue]
        screen.fill((255,255,255))
        for disk in disks:
            disk.drawCircle()
    elif diskNumberValue > len(disks):
        for _ in range(diskNumberValue-len(disks)):
            disks.append(Circle())
            disks[-1].drawCircle()
    if run_animation == True:
        screen.fill((255,255,255))
        animationType = animationTypeSelectList.get_single_selection()
        if animationType == "Gravity":
            for disk in disks:
                disk.moveCirclesGravity(dT)
                disk.drawCircle()
        elif animationType == "Central mass":
            for disk in disks:
                disk.moveCirclesMassCenter(dT)
                disk.drawCircle()
        elif animationType =="Aerodynamics":
            for disk in disks:
                disk.moveCirclesAerodynamics(dT)
                disk.drawCircle()
        else:
            for disk in disks:
                disk.moveCircles(dT)
                disk.drawCircle()
    else:
        for disk in disks:
                disk.drawCircle()
    manager.update(dT)
    manager.draw_ui(screen)
    pygame.display.flip()