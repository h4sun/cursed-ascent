import os
import pygame

class Card(pygame.sprite.Sprite):

    def __init__(self, image_path, type):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = pygame.image.load(image_path).convert()
        self.image = pygame.image.load(image_path).convert()
        self.type = type
        self.rect = self.image.get_rect()



class Cards:
    def __init__(self):
        self.cards = pygame.sprite.Group()
        self.load_cards()

    def load_cards(self):
        card_images = os.listdir(path="assets/cards")

        for index, image in enumerate(card_images):
            if index % 2 == 0:
                image = Card(f"assets/cards/{image}", "attack")
            else:
                image = Card(f"assets/cards/{image}", "defense")
            self.cards.add(image)
