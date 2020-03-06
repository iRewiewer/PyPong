import sys, pygame, shutil, os
from pygame.locals import *
from pygame.font import *
from random import random as rng
from msvcrt import getche

pygame.init()
pygame.display.set_caption('Pong')

#set_screen
window_size = 1000, 600
screen = pygame.display.set_mode(window_size)

#defining color array
colors = {
            "black":(0, 0, 0),
            "white":(255,255,255),
            "random":(int(rng() * 1000 % 256), int(rng() * 1000 % 256), int(rng() * 1000 % 256) )
         }

background_color = colors["black"]

#objects speeds
player_speed = 4
enemy_speed = 3
ball_speed = 4

#game_over
endgame = False

#text_color_setup
text_color = colors["white"]
text_bg = colors["black"]

#score_display
player_score = 0
enemy_score = 0

#font
score_font = Font('LCD.ttf', 42)

#define fps
clock = pygame.time.Clock()

#game loop + object preset
while True:
    
    #setting up scene
    #game happens in the sub loop

    #images & objects
    player = pygame.image.load("paddle.png")
    player_object = player.get_rect()
    player_object = player_object.move(100,230)
    player_pos = [100, 230]

    ball = pygame.image.load("ball.png")
    ball_object = ball.get_rect()
    ball_object = ball_object.move(500,290)
    ball_pos = [500, 290]

    enemy = pygame.image.load("paddle.png")
    enemy_object = enemy.get_rect()
    enemy_object = enemy_object.move(900,230)
    enemy_pos = [900, 230]
    
    vertical_left_wall = pygame.image.load("vertical_wall.png")
    vertical_left_wall_object = vertical_left_wall.get_rect()
    vertical_left_wall_object = vertical_left_wall_object.move(0,0)

    vertical_right_wall = pygame.image.load("vertical_wall.png")
    vertical_right_wall_object = vertical_right_wall.get_rect()
    vertical_right_wall_object = vertical_right_wall_object.move(999,0)

    horizontal_up_wall = pygame.image.load("horizontal_wall.png")
    horizontal_up_wall_object = horizontal_up_wall.get_rect()
    horizontal_up_wall_object = horizontal_up_wall_object.move(0,0)

    horizontal_down_wall = pygame.image.load("horizontal_wall.png")
    horizontal_down_wall_object = horizontal_down_wall.get_rect()
    horizontal_down_wall_object = horizontal_down_wall_object.move(0,599)

    separator = pygame.image.load("separator.png")
    separator_object = separator.get_rect()
    separator_object = separator_object.move(499,0)
    
    #define ball start velocity
    start_vel_rng = int(rng() * 100)

    if start_vel_rng % 4 == 0: #down right v> #takes 6 turns for the player to win (4-4-3) speed
        start_vel = ball_speed, ball_speed
        ball_mode = 0
    elif start_vel_rng % 4 == 1: #up right ^> #takes 16 turns for the player to win (4-4-3) speed
        start_vel = ball_speed, -ball_speed
        ball_mode = 1
        
    elif start_vel_rng % 4 == 2: #down left <v #takes 69 turns for the player to win (4-4-3) speed
        start_vel = -ball_speed, ball_speed
        ball_mode = 2
        
    elif start_vel_rng % 4 == 3: #up left <^ #takes 59 turns for the player to win (4-4-3) speed
        start_vel = -ball_speed, -ball_speed
        ball_mode = 3

    else: pass
    
    #reset_turn (turn is used for debug purposes)
    turn = 1
    
    #debug
    #print("")
    #if ball_mode == 0: print("Starting ball direction: Down Right (v>)")
    #if ball_mode == 1: print("Starting ball direction: Up Right (^>)")
    #if ball_mode == 2: print("Starting ball direction: Down Left (<v)")
    #if ball_mode == 3: print("Starting ball direction: Up Left (<^)")
    #print("")

    #game loop
    while True:
    
        #set fps
        clock.tick(60)
        
        #fill_background_color
        screen.fill(background_color)
        
        #array of all keys pressed
        keys_pressed = pygame.key.get_pressed()
        
        #utility keys
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        if ((keys_pressed[pygame.K_RALT] or keys_pressed[pygame.K_LALT]) and keys_pressed[pygame.K_F4]) or keys_pressed[pygame.K_ESCAPE]: sys.exit()
                            
        #player_movement
        elif keys_pressed[pygame.K_w]:
            if not player_object.colliderect(horizontal_up_wall_object):
                player_object = player_object.move(0,-player_speed)
            
        elif keys_pressed[pygame.K_s]:
            if not player_object.colliderect(horizontal_down_wall_object):
                player_object = player_object.move(0,player_speed)
        else:
            pass
        
        #ball_movement
        
        #collide_left_wall
        if ball_object.colliderect(vertical_left_wall_object):
            enemy_score += 1
            break
            
        #collide_right_wall
        if ball_object.colliderect(vertical_right_wall_object):
            player_score += 1
            break
            
        #singleplayer or multiplayer game over
        if player_score == 7 or enemy_score == 7:
            endgame = True
            break

        if ball_mode == 0: #down right v>
            if ball_object.colliderect(horizontal_down_wall_object): ball_mode = 1
            if ball_object.colliderect(enemy_object):
                ball_mode = 2
                
                #print("Turn: " + str(turn))
                turn += 1
                
                #print(ball_speed)

            else:
                ball_object = ball_object.move(ball_speed, ball_speed)
                enemy_object = enemy_object.move(0, enemy_speed)
                #player_object = player_object.move(0, player_speed) #debug
            
            
        if ball_mode == 1: #up right ^>
            if ball_object.colliderect(horizontal_up_wall_object): ball_mode = 0
            if ball_object.colliderect(enemy_object):
                ball_mode = 3
                
                #print("Turn: " + str(turn))
                turn += 1
                
                #print(ball_speed)
                
            else:
                ball_object = ball_object.move(ball_speed, -ball_speed)
                enemy_object = enemy_object.move(0, -enemy_speed)
                #player_object = player_object.move(0, -player_speed) #debug
            
            
        if ball_mode == 2: #down left <v
            if ball_object.colliderect(horizontal_down_wall_object): ball_mode = 3
            if ball_object.colliderect(player_object):
                ball_mode = 0
                
                #print("Turn: " + str(turn))
                turn += 1
                
                
            else:
                ball_object = ball_object.move(-ball_speed, ball_speed)
                enemy_object = enemy_object.move(0, enemy_speed)
                #player_object = player_object.move(0, player_speed) #debug
            
            
        if ball_mode == 3: #up left <^
            if ball_object.colliderect(horizontal_up_wall_object): ball_mode = 2
            if ball_object.colliderect(player_object):
                ball_mode = 1
                
                #print("Turn: " + str(turn))
                turn += 1
                
                #print(ball_speed) #debug
                
            else:
                ball_object = ball_object.move(-ball_speed, -ball_speed)
                enemy_object = enemy_object.move(0, -enemy_speed)
                #player_object = player_object.move(0, -player_speed) #debug

                
        #score system
        
        #display_player_score
        player_score_display = score_font.render(str(player_score), True, text_color, text_bg)
        player_score_display_object = player_score_display.get_rect()
        player_score_display_object.center = (window_size[0] // 2 - 200, 75)

        #display_enemy_score
        enemy_score_display = score_font.render(str(enemy_score), True, text_color, text_bg)
        enemy_score_display_object = enemy_score_display.get_rect()
        enemy_score_display_object.center = (window_size[0] // 2 + 200, 75)
        
        #render UI elements
        screen.blit(separator, separator_object)
        screen.blit(player_score_display, player_score_display_object)
        screen.blit(enemy_score_display, enemy_score_display_object)
        
        #render entities
        screen.blit(player, player_object)
        screen.blit(enemy, enemy_object)
        screen.blit(ball, ball_object)
        
        #render walls
        screen.blit(vertical_left_wall, vertical_left_wall_object)
        screen.blit(vertical_right_wall, vertical_right_wall_object)
        screen.blit(horizontal_up_wall, horizontal_up_wall_object)
        screen.blit(horizontal_down_wall, horizontal_down_wall_object)
        
        #pygame.display.update()
        pygame.display.flip()
        
    #out of game loop, inside setup loop
    if endgame == True:
        break