#coding=utf-8
import pygame
import os
import time

def main():
    print('##############')
    #os.environ"SDLVIDEODRIVER"="dummy"
    pygame.init()
    pygame.display.list_modes()

    print('##############')

    #1. create a window to display contents
    screen = pygame.display.set_mode((480, 852), 0, 32)
    #2. fill the window with a picture
    background = pygame.image.load("./feiji/background.png")
    
    while True:
        #set the background
        screen.blit(background, (0, 0))
        #update more needed contents
        pygame.display.update()
        time.sleep(0.01)    



if __name__ == "__main__":
    main()
