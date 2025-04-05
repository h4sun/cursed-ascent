import pygame

class Button():

    def __init__(self, image_path, x, y):
        self.image = pygame.image.load(image_path).convert()
        #self.image = pygame.transform.scale(self.image, (1280, 720))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()

            if self.rect.collidepoint(mouse_pos):
                return True
