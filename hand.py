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
                    card.rect.top -= 100
                

        #if not self.__is_any_card_selected():
        mouse_pos = mouse_x, mouse_y = pygame.mouse.get_pos()

        # If the card is not selected give some enlarging when you hovering the mouse on the cards if the card is selected move the card with the mouse.
        # Kart secili değilken üstüne geldiğinde kartı y ekseninde biraz büyüt eğer kart secili ise mousela birlikte kartı hareket ettir.

        """selected_card = self.__is_any_card_selected()
        if selected_card == None:
            if card.rect.collidepoint(mouse_pos):
                card.rect.top -= 100"""
        


        for card in self.cards:
            if not card.selected:
                if card.rect.collidepoint(mouse_pos):
                    card.rect.top -= 100
            else:
                card.rect.left = mouse_x - (card.rect.width / 2)
                card.rect.top = mouse_y - (card.rect.height / 2)

        
        # Draw

        self.cards.draw(surface)

    def select_card(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            
            is_any_card_selected = self.__is_any_card_selected()
            for card in self.cards:
                if card.rect.collidepoint(mouse_pos) and is_any_card_selected != None:
                    card.selected = True
                    card.image.fill("red")
                    is_any_card_selected.selected = False
                    is_any_card_selected.image = is_any_card_selected.original_image.copy()
            
                elif card.rect.collidepoint(mouse_pos) and is_any_card_selected == None:
                    card.selected = True
                    card.image.fill("red")

    
    def __is_any_card_selected(self):
        for card in self.cards:
            if card.selected:
                return card
        else:
            return None
        







