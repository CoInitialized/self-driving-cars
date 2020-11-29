import os
import random
import pygame
from pygame.locals import * # Constants
import math
import sys

os.environ["SDL_VIDEO_CENTERED"] = "1"

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("LEVEL 2 = Find the Correct Square!")

clock = pygame.time.Clock()

class Player(object):
    def __init__(self):
        self.rect = pygame.draw.rect(screen, (0, 0, 128), (10,20,30,40))
        self.dist = 10
        self.last_key = (K_RIGHT,False)
        self.exit = False
        self.ticks = 60
        self.clock = pygame.time.Clock()



    def handle_keys(self):
        while not self.exit:
            dt = self.clock.get_time() / 1000
            # Event queue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                self.draw_rect(-1, 0)
            elif pressed[pygame.K_RIGHT]:
                self.draw_rect(1, 0)
            elif pressed[pygame.K_UP]:
                self.draw_rect(0, -1)
            elif pressed[pygame.K_DOWN]:
                self.draw_rect(0, 1)
            elif pressed == K_ESCAPE:
                pygame.quit(); exit()
            self.clock.tick(self.ticks)

    def draw_rect(self,x,y):
        screen.fill((255, 255, 255))
        self.rect = self.rect.move(x*self.dist, y*self.dist); pygame.draw.rect(screen, (0, 0, 128), self.rect)
        pygame.display.update()

    def draw(self, surface):
        pygame.draw.rect(screen, (0, 0, 128), (10,20,30,40))

pygame.init()

player = Player()
#clock = pygame.time.Clock()
screen.fill((255, 255, 255))
player.draw(screen)
pygame.display.update()

while True:
  player.handle_keys()