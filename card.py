import os
import pygame

class Card(pygame.sprite.Sprite):

    def __init__(self, image_path, type = None):
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

        for image in card_images:
            card = Card(f"assets/cards/{image}")
            if image.endswith("attack.png"):
                card.type = "attack"
            else:
                card.type = "defense"
            self.cards.add(card)
