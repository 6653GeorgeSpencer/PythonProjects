import pygame

from ui import uiEle, uiList


class myEvents:
    def buttonClicked(self, event, game):

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for i in uiList["buttons"]:
                if i.rect.collidepoint(pos) and i.name == "StartMenu":
                    print("I hate this")
                    game.mainMenuBool = False
                    game.level1Bool = True
                elif i.rect.collidepoint(pos) and i.name == "OptionsButton":
                    print("hehe")
                    uiEle.optionMenuBackGround.surface.set_alpha(200)
                elif i.rect.collidepoint(pos) and i.name == "menuQuitButton":
                    pygame.quit()