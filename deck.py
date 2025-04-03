import pygame
import random
from card import Cards

class Deck:
    
    def __init__(self):
        self.cards = Cards().cards

    def build_deck(self):
        self.cards.add()

    def shuffle_deck(self):
        shuffled_cards = list(self.cards)
        random.shuffle(shuffled_cards)
        self.cards = pygame.sprite.Group(shuffled_cards)

    def draw_card_from_deck(self):
        if self.cards:
            card = random.choice(list(self.cards))
            return card
        else:
            return None

    def remove_card(self, card):
        self.cards.remove(card)








