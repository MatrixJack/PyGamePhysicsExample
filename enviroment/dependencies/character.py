#> Imports
import time, pygame

from pygame.math import Vector2
from coreScripts.gameConstants import *

class newCharacterObject(pygame.sprite.Sprite):
    def __init__(self, gameInstance, pygame):
        #Initialize
        pygame.sprite.Sprite.__init__(self)

        #Properties
        self.image = pygame.Surface(PLAYER_SIZE)
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()

        self.position = Vector2(X_AXIS_BOUND / 2, Y_AXIS_BOUND / 2)
        self.acceleration = Vector2(0, 0)
        self.velocity = Vector2(0, 0)
        
        self.floor = False

        #Variables
        self.jumpHeight = 10
        self.characterSpeed = 100

        self.characterState = PLAYER_STATES.get("IDLE")

        self.pyGame = pygame
        self.gameInstance = gameInstance

        # Registration
        self.gameInstance.userInputClass.connect("KeyDown", self.keyDown)

    def update(self):
        self.acceleration += self.velocity * PLAYER_FRICTION
        self.velocity += self.acceleration
        self.position += self.velocity + .5 * self.acceleration

        if self.position.x > X_AXIS_BOUND + (PLAYER_SIZE[0] / 2):
            self.position.x = 0 + (PLAYER_SIZE[0] / 2) - PLAYER_SIZE[0] / 3
            pass

        if self.position.x < 0 - (PLAYER_SIZE[0] / 2):
            self.position.x = X_AXIS_BOUND - (PLAYER_SIZE[0] / 2) + PLAYER_SIZE[0] / 3
            pass

        self.rect.midbottom = self.position

        if self.floor: self.acceleration = Vector2(0, 0)
        else: self.acceleration = Vector2(0, 1.5)

    def keyDown(self, event):
        aPressed = self.gameInstance.userInputClass.isKeyDown("a")
        dPressed = self.gameInstance.userInputClass.isKeyDown("d")
        spacePressed = self.gameInstance.userInputClass.isKeyDown("space")

        while self.characterState == PLAYER_STATES.get("ACTIVE"): time.sleep(.001)
        self.characterState = PLAYER_STATES.get("ACTIVE")

        if aPressed:
            while True:
                if not self.gameInstance.userInputClass.isKeyDown("a"): break
                
                self.acceleration.x = -2.5
                time.sleep(1 / self.characterSpeed)

        if dPressed:
            while True:
                if not self.gameInstance.userInputClass.isKeyDown("d"): break
                
                self.acceleration.x = 2.5
                time.sleep(1 / self.characterSpeed)

        if spacePressed:
            pass

        self.characterState = PLAYER_STATES.get("IDLE")