import pygame

class Button():

    def __init__(self, x, y):
        self.image = pygame.image.load("assets/buttons/end_turn.png").convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


    def click(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()

            if self.rect.collidepoint(mouse_pos):
                return True



