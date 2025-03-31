import pygame

class Hand:

    def __init__(self):
        self.cards = pygame.sprite.Group()

    def draw_hand(self, deck, hand_size):
        if (len(deck.cards) > hand_size):
            while len(self.cards) < hand_size and deck.cards:
                card = deck.draw_card()
                self.cards.add(card)
        else:
            self.cards.add(deck.cards)   
          
    def update_positions(self, screen_width):
        card_top = 550
        card_gap = 25
        num_cards = len(self.cards)
        
        # Calculate the initial left position relative to the center of the screen
        total_width = (num_cards * 150) + (num_cards - 1) * card_gap
        start_x = (screen_width - total_width) // 2

        current_x = start_x
        for card in self.cards:
            card.rect.left = current_x
            card.rect.top = card_top

            # Adding the gap between the cards
            current_x += card.rect.width + card_gap








        







