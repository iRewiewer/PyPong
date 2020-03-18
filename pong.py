import sys, pygame, shutil, os
from pygame.locals import *
from pygame.font import *
from random import random as rng
from msvcrt import getche

from game import game
from highscores import highscores

pygame.init()
pygame.display.set_caption('Pong')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)


#set_screen
try:
    window_size = 1000, 600
    screen = pygame.display.set_mode(window_size)
except:
    print("Error: Line 15, pong.py, Screen Size Setting Error")
    sys.exit()
    
#color palette
colors = {
            "black":(0, 0, 0),
            "white":(255,255,255),
            "random":(int(rng() * 1000 % 256), int(rng() * 1000 % 256), int(rng() * 1000 % 256) )
         }

background_color = colors["black"]

#define_fps
clock = pygame.time.Clock()

#read_highscores
try:
    file = open("highscores.yml", "r")
    
    highscores_list = file.read()
    highscores_list = highscores_list.split("\n")
    
    #print(len(highscores_list))
    #x = getche()
    
    for i in range (0,len(highscores_list)):
        highscores_list[i] = highscores_list[i].split(":")

except:
    print("Error: Line 36, pong.py, read_highscores error")
    sys.exit()

finally:
    file.close()

#define_text_colors
text_color = colors["white"]
text_bg = colors["black"]

#define fonts
title_font = Font('Scream.ttf', 72)
button_font = Font('LCD.ttf', 32)
credits_font = Font('LCD.ttf', 14)

#starting button
button = 0

#buttons_position_constants (y axis)
base_pos = 230
const = 70

#title
title = title_font.render("PONG", True, text_color, text_bg)
title_object = title.get_rect()
title_object.center = (window_size[0] // 2, 100)
    
#credits
credits = credits_font.render("Made by iRewiewer", True, text_color, text_bg)
credits_object = credits.get_rect()
credits_object.center = (80, window_size[1] - 10)

while True:

    #set fps
    clock.tick(60)

    keys_pressed = pygame.key.get_pressed() #array of all keys pressed
    
    #keys_events
    for event in pygame.event.get():
    
        #exit events
        if ((keys_pressed[pygame.K_RALT] or keys_pressed[pygame.K_LALT]) and keys_pressed[pygame.K_F4]) or keys_pressed[pygame.K_ESCAPE]: sys.exit()         
        if event.type == pygame.QUIT: sys.exit()
        
        if keys_pressed[pygame.K_w]: #previous button
            if button != 0: button -= 1
            else: button = 4
            
        if keys_pressed[pygame.K_s]: #next button
            if button != 4: button += 1
            else: button = 0

    #button0 - singleplayer
    if button == 0:
        button0 = button_font.render(">> 1 Player <<", True, text_color, text_bg)
        if keys_pressed[pygame.K_RETURN]: game(screen, window_size, background_color, colors, 0, highscores_list)
    else:
        button0 = button_font.render("1 Player", True, text_color, text_bg)
    
    #button1 - multiplayer
    if button == 1:
        button1 = button_font.render(">> 2 Players <<", True, text_color, text_bg)
        if keys_pressed[pygame.K_RETURN]: game(screen, window_size, background_color, colors, 1, highscores_list)
    else:
        button1 = button_font.render("2 Players", True, text_color, text_bg)
    
    #button2 - endless
    if button == 2:
        button2 = button_font.render(">> Endless <<", True, text_color, text_bg)
        if keys_pressed[pygame.K_RETURN]: game(screen, window_size, background_color, colors, 2, highscores_list)
    else: button2 = button_font.render("Endless", True, text_color, text_bg)
    
    #button3 - highscores
    if button == 3:
        button3 = button_font.render(">> Highscores <<", True, text_color, text_bg)
        if keys_pressed[pygame.K_RETURN]: highscores(screen, window_size, background_color, colors, highscores_list)
    else: button3 = button_font.render("Highscores", True, text_color, text_bg)
    
    #button4 - exit
    if button == 4:
        button4 = button_font.render(">> Exit <<", True, text_color, text_bg)
        if keys_pressed[pygame.K_RETURN]:
            sys.exit()
    else: button4 = button_font.render("Exit", True, text_color, text_bg)

    #update objects
    button0_object = button0.get_rect()
    button0_object.center = (window_size[0] // 2, base_pos + const * 0)
    button1_object = button1.get_rect()
    button1_object.center = (window_size[0] // 2, base_pos + const * 1)
    button2_object = button2.get_rect()
    button2_object.center = (window_size[0] // 2, base_pos + const * 2)
    button3_object = button3.get_rect()
    button3_object.center = (window_size[0] // 2, base_pos + const * 3)    
    button4_object = button4.get_rect()
    button4_object.center = (window_size[0] // 2, base_pos + const * 4)
    
    #printing
    screen.fill(background_color)
    screen.blit(title, title_object)
    screen.blit(credits, credits_object)
    screen.blit(button0, button0_object)
    screen.blit(button1, button1_object)
    screen.blit(button2, button2_object)
    screen.blit(button3, button3_object)
    screen.blit(button4, button4_object)

    #update screen
    pygame.display.flip()