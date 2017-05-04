import pygame
from Flames import Flames
import os
from ExtraFeatures import Features

def start_threads():
    flame_obj1.start()
    flame_obj2.start()
    flame_obj3.start()
    flame_obj4.start()
    flame_obj5.start()

def close_threads():
    flame_obj1.run_flame = False
    flame_obj2.run_flame = False
    flame_obj3.run_flame = False
    flame_obj4.run_flame = False
    flame_obj5.run_flame = False

# sets basic game features
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
x_Display = 1200
y_Display = 600
gameDisplay = pygame.display.set_mode((x_Display, y_Display))
game_border = gameDisplay.get_rect()
game_border2 = (5, 5, x_Display - 10, y_Display - 10)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BRIGHT_BLUE = (0, 0, 255)
BLUE = (0, 0, 150)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# five fire ball threads
flame_obj1 = Flames(gameDisplay)
flame_obj2 = Flames(gameDisplay)
flame_obj3 = Flames(gameDisplay)
flame_obj4 = Flames(gameDisplay)
flame_obj5 = Flames(gameDisplay)

# file for highscore
file_read = open("Highscore.txt", 'r')
highscore = 0
string = file_read.read()
if (string == ''):
    highscore = 0
else:
    highscore = int(string)
file_write = open("Highscore.txt", 'w')

# extra features of the game
feature = Features(gameDisplay)

# square movements and body
movement_speed = 10
jump_speed = 13
x_change = 0
y_change = 0

rect = pygame.rect.Rect((0, 550, 50, 50))
rect2 = pygame.rect.Rect((5, 555, 40, 40))

can_jump = True
jump = 100
jump_count = 0
go_up = False

'''
jump_time = 0
gravity = 14
'''

# beginning game features
keepPlaying = True
gameLose = False
clock = pygame.time.Clock()
start_threads()

while keepPlaying:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepPlaying = False
            close_threads()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change -= movement_speed
            if event.key == pygame.K_RIGHT:
                x_change += movement_speed
            if event.key == pygame.K_UP:
                if (jump_count == 0):
                    go_up = True
                    can_jump = False
                #if (jump_time == 0):
                 #   go_up = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = 0

        elif event.type == pygame.MOUSEBUTTONDOWN and gameLose:
            pos = pygame.mouse.get_pos()
            if 650 < pos[0] < 1010 and 270 < pos[1] < 325:
                keepPlaying = True
                gameLose = False
                flame_obj1 = Flames(gameDisplay)
                flame_obj2 = Flames(gameDisplay)
                flame_obj3 = Flames(gameDisplay)
                flame_obj4 = Flames(gameDisplay)
                flame_obj5 = Flames(gameDisplay)
                start_threads()
            elif 650 < pos[0] < 800 and 370 < pos[1] < 435:
                keepPlaying = False
                break;
    '''
    # jump restrictions
    if (jump_time >= 4):
        go_up = False
        jump_time = 0
        y_change = 0
    if go_up:
        y_change = jump_speed + 0.5 * gravity * jump_time* jump_time
        jump_time += 0.1
    '''

    # jump restrictions
    if (jump_count >= jump/2 - 1):
        go_up = False
    if go_up:
        if not can_jump:
            y_change = -jump_speed
            jump_count += 1
    else:
        if not can_jump:
            y_change = jump_speed
            jump_count += 1
        if jump_count >= jump - 1:
            jump_count = 0
            y_change = 0
            can_jump = True

    rect.move_ip(x_change, y_change)
    rect2.move_ip(x_change, y_change)

    # when square collides with fire balls
    if (rect.colliderect(flame_obj1.fire_rect) or
            rect.colliderect(flame_obj2.fire_rect) or
            rect.colliderect(flame_obj3.fire_rect) or
            rect.colliderect(flame_obj4.fire_rect) or
            rect.colliderect(flame_obj5.fire_rect)):
        gameLose = True
        close_threads()

        # keeps track of highscore
        if (score >= highscore and gameLose == True):
            highscore = score
        file_write = open("Highscore.txt", 'w')
        file_write.write("" + str(highscore))

    # display score at top left corner
    score = flame_obj1.level
    msg = "Score: " + str(score)

    rect.clamp_ip(game_border)
    rect2.clamp_ip(game_border2)
    gameDisplay.fill(GREEN)
    pygame.draw.rect(gameDisplay, BLACK, rect)
    pygame.draw.rect(gameDisplay, WHITE, rect2)
    pygame.draw.ellipse(gameDisplay, RED, rect2, 15)
    gameDisplay.blit(feature.message_to_screen(msg, BLUE, 100), [10, 10])

    if gameLose == True:
        gameDisplay.blit(feature.message_to_screen("GG", BLUE, 500), [80, 150])
        gameDisplay.blit(feature.message_to_screen("Highscore: " + str(highscore), BLUE, 100), [650, 170])

        mouse = pygame.mouse.get_pos()

        if 650 < mouse[0] < 1010 and 270 < mouse[1] < 325:
            gameDisplay.blit(feature.message_to_screen("Play Again", BRIGHT_BLUE, 100), [650, 270])
        else:
            gameDisplay.blit(feature.message_to_screen("Play Again", BLUE, 100), [650, 270])

        if 650 < mouse[0] < 800 and 370 < mouse[1] < 435:
            gameDisplay.blit(feature.message_to_screen("Quit", BRIGHT_BLUE, 100), [650, 370])
        else:
            gameDisplay.blit(feature.message_to_screen("Quit", BLUE, 100), [650, 370])

    pygame.display.update()
    clock.tick(60)

file_read.close()
file_write.close()
pygame.quit()
quit()
