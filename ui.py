import pygame

uiList = {"buttons": [],
          "shapes": []}


class uiLibs():
    def __init__(self, colour, x, y, width, height, orin, name):
        # inting simple shape stuff
        self.name = name
        self.colour = colour
        self.pos = (x, y)
        self.width = width
        self.height = height
        self.orin = orin

    def rectInt(self, isCentre, ScreenCenter, x, y, alpha, Isbutton):
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.set_alpha(alpha)
        self.surface.fill(self.colour)

        if isCentre:
            self.pos = self.surface.get_rect(centerx=ScreenCenter[0] + x, centery=ScreenCenter[1] + y)

        self.rect = self.surface.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        if Isbutton:
            uiList["buttons"] += [self]
        else:
            uiList["shapes"] += [self]

    def setAlpha(self, alpha, surface):
        surface.set_alpha(alpha)

    def drawRect(self, screen):
        screen.blit(self.surface, self.pos)


class objs():
    def __init__(self, centre) -> None:
        self.a = uiLibs((0, 0, 0), 100, 100, 300, 50, 0, "StartMenu")
        self.a.rectInt(True, centre, 0, 0, 255, True)

        self.options = uiLibs((0, 0, 0), 100, 100, 300, 50, 0, "OptionsButton")
        self.options.rectInt(True, centre, 0, 100, 255, True)

        self.optionMenuBackGround = uiLibs((50, 50, 50), 0, 0, 550, 350, 0, "OptionMenuBackGround")
        self.optionMenuBackGround.rectInt(True, centre, 0, 0, 0, False)

        self.menuQuitButton = uiLibs((0, 0, 0), 50, 50, 300, 50, 0, "menuQuitButton")
        self.menuQuitButton.rectInt(False, centre, 0, 0, 255, True)
        self.menuBackground = uiLibs((128, 128, 128), 0, 0, 1280, 720, 0, "Background")
        self.menuBackground.rectInt(False, centre, 0, 0, 160, False)
    def drawMainScreen(self, game):
        game.screen.fill(game.backgroundColour)
        game.screen.blit(game.surface, (0, 0))
        self.a.drawRect(game.screen)
        self.options.drawRect(game.screen)
    def drawMenu(self, game):
        self.menuBackground.drawRect(game.screen)
        self.menuQuitButton.drawRect(game.screen)




centre = (700 / 2, 500 / 2)
uiEle = objs(centre)


