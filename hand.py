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
          

    def draw(self, surface, screen_width):
        num_cards = len(self.cards)
        
        # Calculate the initial left position relative to the center of the screen
        total_width = (num_cards * 150) + (num_cards - 1)
        start_x = (screen_width - total_width) // 2

        card_top = 600
        current_x = start_x
        for card in self.cards:
            card.rect.left = current_x
            current_x += card.rect.width
            if not card.selected:
                card.rect.top = card_top
            else:
                if card.rect.top > 500:
                    print(card.rect.top)
                    card.rect.top -= 100
                

        # Enlarge the card when the mouse on the card
        mouse_pos = pygame.mouse.get_pos()
        for card in self.cards:
            if not card.selected:
                if card.rect.collidepoint(mouse_pos):
                    card.rect.top -= 100


        # Draw
        self.cards.draw(surface)

    def select_card(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()

            for card in self.cards:
                if card.rect.collidepoint(mouse_pos):
                    card.selected = not card.selected
                    if card.selected:
                        card.image.fill("red")
                    else:
                        card.image = card.original_image.copy()
                    print(f"Card selected: {card.selected}")



        







