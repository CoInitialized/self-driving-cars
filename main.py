import os
import random
import pygame
from pygame.locals import * # Constants
import math
import sys

os.environ["SDL_VIDEO_CENTERED"] = "1"

screen = pygame.display.set_mode((1600, 1000))
pygame.display.set_caption("LEVEL 2 = Find the Correct Square!")

clock = pygame.time.Clock()



class Player(object):
    def __init__(self):
        self.img = pygame.image.load('self-driving-cars/car.png').convert()
        self.dist = 10
        self.last_key = (K_RIGHT,False)
        self.exit = False
        self.ticks = 60
        self.clock = pygame.time.Clock()
        self.position = (0,0)
        self.angle = 0



    def handle_keys(self):
        while not self.exit:
            dt = self.clock.get_time() / 1000
            # Event queue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                self.angle -=1
                self.draw_rect(self.position)
            if pressed[pygame.K_RIGHT]:
                self.angle += 1
                self.draw_rect(self.position)
            if pressed[pygame.K_UP]:
                self.position = (self.position[0] +1, self.position[1] + math.sin(self.angle/255))
                self.draw_rect(self.position)
            if pressed[pygame.K_DOWN]:
                self.position = (self.position[0] + -1, self.position[1] + math.sin(self.angle/255))
                self.draw_rect(self.position)
            if pressed == K_ESCAPE:
                pygame.quit(); exit()
            self.clock.tick(self.ticks)

    def draw_rect(self,pos):
        screen.fill((0, 0, 0))
        rect = self.img.get_rect()
        rect.center = pos
        screen.blit(self.img, rect)
        pygame.display.update()

    def draw(self, surface):
        rect = self.img.get_rect()
        rect.center = (0, 0)
        screen.blit(self.img, rect)

pygame.init()

player = Player()
#clock = pygame.time.Clock()
screen.fill((0, 0, 0))
player.draw(screen)
pygame.display.update()

while True:
  player.handle_keys()