#import libraries
import pygame
#initialize pygame
pygame.init()
#game window
SCREEN_WIDTH=400
SCREEN_HEIGHT=600
#create game window
screen=pygame.display.set_mode(SCREEN_WIDTH,SCREEN_HEIGHT)
pygame.display.set_caption('Jumpy')
#game loop
run=True
while run:
    #event hadler
    for event in pygame.event.get():
        if even.type==pygame.QUIT:
            run=False

pygame.quit() 
