import pygame

class Hand:

    def __init__(self):
        self.cards = pygame.sprite.Group()

    def draw_hand(self, deck, hand_size):
        if (len(deck.cards) > hand_size):
            while len(self.cards) < hand_size and deck.cards:
                card = deck.draw_card_from_deck()
                self.cards.add(card)
        else:
            self.cards.add(deck.cards) # If the hand_size bigger than the deck we simply add all deck to hand   
          

    def draw(self, surface, screen_width):
        num_cards = len(self.cards)
        
        # Calculate the initial left position relative to the center of the screen
        total_width = (num_cards * 150) + (num_cards - 1)
        start_x = (screen_width - total_width) // 2

        # Adjust the position of the cards
        card_top = 600
        current_x = start_x
        for card in self.cards:
            card.rect.left = current_x
            current_x += card.rect.width
            card.rect.top = card_top
                
        # Kart secili değilken üstüne geldiğinde kartı y ekseninde biraz büyüt eğer kart secili ise mousela birlikte kartı hareket ettir.
        # If the card is not selected give some enlarging when you hovering the mouse on the cards if the card is selected move the card with the mouse.
        mouse_pos = mouse_x, mouse_y = pygame.mouse.get_pos()
        get_selected_card = self.__get_selected_card()

        if get_selected_card == None:
            for card in self.cards:
                if card.selected == False:
                    if card.rect.collidepoint(mouse_pos): 
                        card.rect.top -= 100
        else:
            get_selected_card.rect.left = mouse_x - (get_selected_card.rect.width / 2)
            get_selected_card.rect.top = mouse_y - (get_selected_card.rect.height / 2)

        
        self.cards.draw(surface)

    def select_card(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            
            get_selected_card = self.__get_selected_card()
            if get_selected_card == None:
                for card in self.cards:
                    if card.rect.collidepoint(mouse_pos):
                        card.selected = True
                        card.image.fill("red")
            else:
                get_selected_card.selected = False
                get_selected_card.image = get_selected_card.original_image.copy()

    
    def __get_selected_card(self):
        for card in self.cards:
            if card.selected:
                return card
        else:
            return None
    







