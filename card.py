import os
import pygame

class Card(pygame.sprite.Sprite):
    def __init__(self, image_path):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = pygame.image.load(image_path).convert()
        self.image = pygame.image.load(image_path).convert()
        self.rect = self.image.get_rect()
        self.selected = False

class Cards:
    def __init__(self):
        self.cards = pygame.sprite.Group()
        self.load_cards()

    def load_cards(self):
        card_images = os.listdir(path="assets/cards")

        for image in card_images:
            image = Card(f"assets/cards/{image}")
            self.cards.add(image)

    def select_card(self, card): 
        pass