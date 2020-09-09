import time, pygame

from pygame.math import Vector2
from coreScripts.gameConstants import *

class newWorldPart(pygame.sprite.Sprite):
    def __init__(self, gameInstance, pygame, x, y, xPos, yPos):
        #Initialize
        pygame.sprite.Sprite.__init__(self)

        #Properties
        self.image = pygame.Surface((x, y))
        self.image.fill(GROUND_COLOR)
        self.rect = self.image.get_rect()

        self.rect.x = xPos
        self.rect.y = yPos# idk what it's saying. he said /2 cuz it's weird but weird flex but ok

    def update(self):
        pass