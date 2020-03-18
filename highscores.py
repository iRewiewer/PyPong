import sys, pygame, shutil, os
from pygame.locals import *
from pygame.font import *
from random import random as rng
from msvcrt import getche

def highscores(screen, window_size, background_color, colors, highscores_list):
    
    #text_color_setup
    text_color = colors["white"]
    text_bg = colors["black"]
    
    #font
    title_font = Font('Scream.ttf', 62)
    score_font = Font('LCD.ttf', 42)
    
    #buttons_position_constants (y axis)
    base_pos = 230
    const = 60

    screen.fill(background_color)
    
    #title
    title = title_font.render("Highscores", True, text_color, text_bg)
    title_object = title.get_rect()
    title_object.center = (window_size[0] // 2, 75)
    screen.blit(title, title_object)
    
    try:
        #draw_highscores
        for i in range (1,13):
            score = score_font.render(str(highscores_list[i][0]) + " " + str(highscores_list[i][1]), True, text_color, text_bg)
            score_object = score.get_rect()
            
            if i <= 6: score_object = score_object.move(165, 120 + i * const)
            else: score_object = score_object.move(645, 120 + (i-6) * const)
            
            screen.blit(score, score_object)  
    except:
        print("Error: Line 29, highscores.py, draw_highscores error")
        
    pygame.display.flip()
    
    #on key press, return to menu
    quit = False
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                quit = True

        if quit == True: break