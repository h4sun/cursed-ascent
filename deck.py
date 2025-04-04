import pygame
import random
from card import Cards

class Deck:
    
    def __init__(self, cards):
        self.deck_cards = cards

    def build_deck(self):
        self.deck_cards.add()

    def shuffle_deck(self):
        shuffled_cards = list(self.deck_cards)
        random.shuffle(shuffled_cards)
        self.deck_cards = pygame.sprite.Group(shuffled_cards)

    def draw_card(self):
        if self.deck_cards:
            card = random.choice(list(self.deck_cards))
            return card
        else:
            return None

    def remove_card(self, card):
        self.deck_cards.remove(card)








