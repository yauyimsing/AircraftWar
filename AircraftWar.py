#coding=utf-8
import pygame
import os
import time
from pygame.locals import *
import random
#
class HeroPlane(object):
    def __init__(self, screen_temp):
        self.x = 210
        self.y = 600
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/hero1.png")
        self.bullet_list = []

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        del_bullet_list = []
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge(): # judge if the bullet out of bounder
                del_bullet_list.append(bullet)
        for del_bullet in del_bullet_list:
            self.bullet_list.remove(del_bullet)

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def move_up(self):
        self.y -= 5

    def move_down(self):
        self.y += 5

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))
#
class EnemyPlane(object):
    def __init__(self, screen_temp):
        self.x = 0
        self.y = 0
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/enemy0.png")
        self.bullet_list = []
        self.direction = "right"

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        del_bullet_list = []
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge(): # judge if the bullet out of bounder
                del_bullet_list.append(bullet)
        for del_bullet in del_bullet_list:
            self.bullet_list.remove(del_bullet)

    def move(self):
        if self.direction == "right":
            self.x += 5
        elif self.direction == "left":
            self.x -= 5
        if self.x > 480-50:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"

    def fire(self):
        random_num = random.randint(1, 100)
        if random_num == 1 or random_num == 50:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))

class Bullet(object):
    def __init__(self, screen_temp, x, y):
        self.x = x + 40
        self.y = y - 20
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/bullet.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 5

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False
class EnemyBullet(object):
    def __init__(self, screen_temp, x, y):
        self.x = x + 25
        self.y = y + 40
        self.screen = screen_temp
        self.image = pygame.image.load("./feiji/bullet1.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += 5

    def judge(self):
        if self.y > 852:
            return True
        else:
            return False

def key_control(hero_temp):
    # get the key from the keybord
    for event in pygame.event.get():
        if event.type == QUIT:
            print("exit")
            exit()
        elif event.type == KEYDOWN:
            #print('key %s'%event.key)
            if event.key == K_a or event.key == K_LEFT:
                hero_temp.move_left()
            elif event.key == K_d or event.key == K_RIGHT:
                hero_temp.move_right()
            elif event.key == K_w or event.key == K_UP:
                hero_temp.move_up()
            elif event.key == K_s or event.key == K_DOWN:
                hero_temp.move_down()
            elif event.key == K_SPACE:
                hero_temp.fire()
            else:
                pass

def main():
    print('##############')
    #os.environ"SDLVIDEODRIVER"="dummy"
    #pygame.init()
    #pygame.display.list_modes()

    print('##############')

    #1. create a window to display contents
    screen = pygame.display.set_mode((480, 852), 0, 32)
    #2. fill the window with a picture 
    background = pygame.image.load("./feiji/background.png")
    #3 create a aircraft
    hero = HeroPlane(screen)
    # create a enemy
    enemy = EnemyPlane(screen)

    while True:
        #set the background
        screen.blit(background, (0, 0))
        hero.display()
        enemy.display()
        enemy.move()
        enemy.fire()
        #update more needed contents
        pygame.display.update()
        key_control(hero)
        
        time.sleep(0.01)    



if __name__ == "__main__":
    main()
