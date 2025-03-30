import pygame
import random


class Hand:

    def __init__(self):
        self.cards = pygame.sprite.Group()

    def draw_hand(self, deck, max_hand):
        while len(self.cards) < max_hand and deck.cards:
            self.cards.add(deck.cards)
            deck.remove_card(self.cards)




            





        







