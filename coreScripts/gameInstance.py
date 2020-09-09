#> Imports
import pygame, sys, logging

from enviroment.dependencies.userInput import newIOClass
from enviroment.dependencies.character import newCharacterObject
from enviroment.worldPart import newWorldPart

from coreScripts.gameConstants import *

#> Classes
class gameInstance():
    def __init__(self):
        #> initialize certain things
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(GAME_CAPTION)

        #> Properties
        self.gameStatus = True

        self.gameDisplay = pygame.display.set_mode((X_AXIS_BOUND, Y_AXIS_BOUND))
        self.gameClock = pygame.time.Clock()

        #> Register Classes
        self.userInputClass = newIOClass(self, pygame)
        self.userInputClass.connect("Quit", self.close)

        #> Start General Loop
        self.new()

    def close(self, event):
        self.gameStatus = None
        
        pygame.quit()
        sys.exit(0)

    def new(self):
        self.enviromentSprites = pygame.sprite.Group()
        self.liveSprites = pygame.sprite.Group()

        self.player = newCharacterObject(self, pygame)
        self.base0 = newWorldPart(self, pygame, X_AXIS_BOUND, 25, 0, Y_AXIS_BOUND - 25)
        self.base1 = newWorldPart(self, pygame, 250, 25, X_AXIS_BOUND / 2 - (250 / 2), 250)

        self.enviromentSprites.add(self.base0)
        self.enviromentSprites.add(self.base1)

        self.liveSprites.add(self.player)

        self.run()

    def run(self):
        while self.gameStatus:
            self.gameClock.tick(SET_SCREEN_FPS)
            for event in pygame.event.get(): self.userInputClass.distribute(event)
            
            self.update()
            self.draw()

    def update(self):
        #self.enviromentSprites.update()
        self.liveSprites.update()

        hitsDetected = pygame.sprite.spritecollide(self.player, self.enviromentSprites, False)
        
        if hitsDetected:
            self.player.position.y = hitsDetected[0].rect.top + 1
            self.player.floor = True
            self.player.velocity.y = 0
        else:
            self.player.floor = False

    def draw(self):
        self.gameDisplay.fill(BACKGROUND_COLOR)

        self.liveSprites.draw(self.gameDisplay)
        self.enviromentSprites.draw(self.gameDisplay)

        pygame.display.update()