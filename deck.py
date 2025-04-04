import pygame
import random
from card import Cards

class Deck:
    
    def __init__(self, cards):
        self.deck_cards = cards
        self.card_graveyard = []

    def build_deck(self):
        self.deck_cards.add()

    def shuffle_deck(self):
        shuffled_cards = list(self.deck_cards)
        random.shuffle(shuffled_cards)
        self.deck_cards = pygame.sprite.Group(shuffled_cards)

    def draw_card(self):
        if len(self.deck_cards) > 0:
            card = self.deck_cards.sprites()[0]
            return card
        else:
            self.deck_cards = pygame.sprite.Group(self.card_graveyard) # Hangi kart en üste geliyor bak ilk giren mi yoksa son giren mi
            self.card_graveyard = []
            card = self.deck_cards.sprites()[0]
            return card

    def remove_card(self, card):
        self.card_graveyard.append(card)
        self.deck_cards.remove(card)








