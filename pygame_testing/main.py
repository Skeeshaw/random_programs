import pygame
import modules
from modules import * # pylint: disable=wildcard-import
from pygame.locals import *

# --------------=<Constants>=-------------- #

BLACK = (0,0,0)
GRAY = (127,127,127)
WHITE = (255,255,255)

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)

# --------------=</Constants>=-------------- #

def test1():
    #test 1 of pygame's basic functions
    
    #setting initial background color
    background = GRAY

    #dictionary defining keys to their colors
    key_dict = {K_k:BLACK, K_r:RED, K_g:GREEN, K_b:BLUE, K_y:YELLOW, K_c:CYAN, K_m:MAGENTA, K_w:WHITE} #pylint disable:undefined-variable
    #initialize all pygame modules
    pygame.init()

    #set screen var and open a window
    screen = pygame.display.set_mode((1000,600))

    #var to end while loop
    running = True
    
    #so program can shut down
    while running:
        
        #event loop
        for event in pygame.event.get():
            
            #if program is attempted to be closed then end while loop
            #will not close without this
            if event.type == pygame.QUIT:
                running = False
            
            #if key is pressed
            if event.type == KEYDOWN:
                
                #change background to color based on key dictionary
                if event.key in key_dict:
                    background = key_dict[event.key]
                    
                
            
            #set title of window and fill background
            #pygame requires calling display.update() to show updates
            pygame.display.set_caption("background color: " + str(background))
            screen.fill(background)
            pygame.display.update()
            
                
    #basically if while loop is ended then quit window
    pygame.quit()

# ------------------------------------------ #

def ball_move():
    
    #init all pygame modules
    pygame.init()

    #defined in this manner because ball needs to stay in the boundaries of screen
    size = 640, 320
    width, height = size

    #constants for color
    GREEN = (150, 255, 150)
    RED = (255, 0, 0)

    #define screen
    screen = pygame.display.set_mode(size)
    running = True

    #define ball image
    ball = pygame.image.load("ball.gif")
    rect = ball.get_rect()

    #set speed of ball (will use later)
    speed = [100,1]

    while running:
        for event in pygame.event.get():
            
            #quit loop if program is closed
            if event.type == QUIT:
                running = False
                
            rect = rect.move(speed)
            if rect.left < 0 or rect.right > width:
                speed[0] = -speed[0]
            if rect.top < 0 or rect.bottom > height:
                speed[1] = -speed[1]
                
            
        screen.fill(GREEN)
        pygame.draw.rect(screen,RED,rect,1)
        screen.blit(ball,rect)
        pygame.display.update()

    pygame.quit()

# ------------------------------------------ #

def chess():
    pygame.init()
    
    n = 8
    surface_sz = 700
    screen = pygame.display.set_mode((surface_sz,surface_sz))
    running = True

    modules.chessboard(screen,surface_sz,n)
            
    while running:
        for event in pygame.event.get():
            
            
            if event.type == QUIT:
                running = False



        pygame.display.update()
    pygame.quit()


chess()

