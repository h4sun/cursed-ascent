import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__
        self.image = pygame.image.load("assets/enemies/angry_man.png").convert()
        self.rect = self.image.get_rect()
        self.adjust_enemy_position(720)


    def adjust_enemy_position(self, screen_height):
        self.rect.top = (screen_height - self.rect.height) // 2
        self.rect.left = 1050