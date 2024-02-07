import sys

import pygame

import levels
import uiLogic
import player
from ui import uiEle
import sprite

events = uiLogic.myEvents()
levels.tileStuff()

# constants
tileSize = 50

player1 = player.Player()
sprite.player_sprite.add(player1)

camera = pygame.Rect(0, 0, 700, 500)


class game():
    def __init__(self) -> None:
        # setting simple scren stuff
        pygame.init()
        self.gravity = 32
        self.offsetX = 0
        pygame.key.set_repeat(60)
        self.clock = pygame.time.Clock()
        self.surface = pygame.Surface((1980, 1080), pygame.SRCALPHA)
        self.screen = pygame.display.set_mode((1280, 720))
        self.playerCanMove = True

        # phases
        self.mainMenuBool = True
        self.level1Bool = False

        # Game phase bools
        self.optionMenu = False

    def mainMenu(self):
        # setting the background colour in the case that the background image fails to load
        self.backgroundColour = (255, 255, 255)

        while self.mainMenuBool:
            # Allows for listen events and processes them
            for event in pygame.event.get():
                # allows the player to quit
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                uiLogic.myEvents().buttonClicked(event, self)

            uiEle.drawMainScreen(self)
            pygame.display.flip()
            self.clock.tick(60)

    def level1(self):
        aKey = False
        dKey = False
        spaceKey = False
        xKey = False
        menu = False
        tileSprites = levels.tile_sprite


        self.backgroundColour = (38, 153, 199)
        print(levels.tile_sprite)
        print(len(levels.tileList))
        while self.level1Bool:
            dt = self.clock.tick(75) * .001 * 75
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        player1.w_key = True
                    if event.key == pygame.K_a:
                        player1.a_KEY = True
                    if event.key == pygame.K_d:
                        player1.d_KEY = True
                    if event.key == pygame.K_SPACE:
                        player1.jump()
                    if event.key == pygame.K_f:
                        player1.dash()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        player1.w_key = False
                    if event.key == pygame.K_a:
                        player1.a_KEY = False
                    if event.key == pygame.K_d:
                        player1.d_KEY = False
                    if event.key == pygame.K_SPACE:
                        spaceKey = False
                    if event.key == pygame.K_ESCAPE:
                        if menu:
                            menu = False
                        else:
                            menu = True

                uiLogic.myEvents().buttonClicked(event, self)
            if self.playerCanMove:
                player1.update(dt, self.offsetX)

            if player1.pos.x > (self.screen.get_width() / 4) * 2.75 and player1.isTouching == False:
                self.offsetX = player1.pos.x - (self.screen.get_width() / 4 * 2.75)

            self.screen.fill(self.backgroundColour)

            player1.draw(self.screen, self.offsetX)

            for i in tileSprites:
                i.draw(self.screen, self.offsetX)


            tileSprites.update()






            if menu:
                self.screen.set_alpha(100)
                uiEle.drawMenu(self)
                self.playerCanMove = False
            else:
                self.playerCanMove = True


            pygame.display.flip()


runtime = game()
runtime.mainMenu()
runtime.level1()

