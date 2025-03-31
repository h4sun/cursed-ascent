import pygame
import random
from card import Card

class Deck:
    
    def __init__(self):
        self.cards = pygame.sprite.Group()
        card_images = [
            "assets/Cards/card_1.png",
            "assets/Cards/card_2.png",
            "assets/Cards/card_3.png",
            "assets/Cards/card_4.png",
            "assets/Cards/card_5.png",
        ]
        for img in card_images:
            card = Card(img)
            self.cards.add(card)

    def shuffle_deck(self):
        shuffled_cards = list(self.cards)
        random.shuffle(shuffled_cards)
        self.cards = pygame.sprite.Group(shuffled_cards)

    def draw_card(self):
        if self.cards:
            card = random.choice(list(self.cards))
            return card
        else:
            return None

    def remove_card(self, card):
        self.cards.remove(card)








