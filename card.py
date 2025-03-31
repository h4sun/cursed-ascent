import os
import pygame

class Card(pygame.sprite.Sprite):
    def __init__(self, image_path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path).convert()
        self.rect = self.image.get_rect()

class Cards:
    def __init__(self):
        self.cards = pygame.sprite.Group()
        self.load_cards()

    def load_cards(self):
        card_images = os.listdir(path="assets/cards")

        for card in card_images:
            card = Card(f"assets/cards/{card}")
            self.cards.add(card)

    def select_card(self, card): 
        pass