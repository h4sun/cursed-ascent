import pygame

class Hand:

    def __init__(self,):
        self.hand_cards = pygame.sprite.Group()
        self.hand_size = 5
        self.hand_copy = []

        self.selected_card = None
        self.released_card = False 

    def draw_hand(self, deck):
        while len(self.hand_cards) < self.hand_size and deck.deck_cards:
            card = deck.draw_card()
            self.hand_cards.add(card)
            deck.remove_card(card) # Remove the card we draw from the deck

        self.hand_copy = []
        for card in self.hand_cards:
            self.hand_copy.append(card) # Copy hand it is solve the topmost card when the select
          
    def draw(self, surface, screen_width):
        num_cards = len(self.hand_cards)
        
        # Calculate the initial left position relative to the center of the screen
        total_width = (num_cards * 150) + (num_cards - 1)
        start_x = (screen_width - total_width) // 2

        # Adjust the position of the cards
        if self.selected_card == None:
            card_top = 600
            current_x = start_x
            for card in self.hand_cards:
                card.rect.left = current_x
                current_x += card.rect.width
                card.rect.top = card_top
                
        # Kart secili değilken üstüne geldiğinde kartı y ekseninde biraz büyüt eğer kart secili ise mousela birlikte kartı hareket ettir.
        # If the card is not selected give some enlarging when you hovering the mouse on the cards if the card is selected move the card with the mouse.
        mouse_pos = mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.selected_card == None:
            for card in self.hand_cards:
                if card.rect.collidepoint(mouse_pos): 
                    card.rect.top -= 100
        else:
            self.selected_card.rect.left = mouse_x - (self.selected_card.rect.width / 2)
            self.selected_card.rect.top = mouse_y - (self.selected_card.rect.height / 2)

        self.hand_cards.draw(surface)

    def select_card(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.selected_card == None:
            for card in self.hand_cards:
                if card.rect.collidepoint(mouse_pos):
                    self.selected_card = card
                    #card.image.fill("red")
                    self.hand_cards.remove(card)
                    self.hand_cards.add(card)
                    return False # We still holding the card
           
        else:
            #self.selected_card.image = self.selected_card.original_image.copy()
            #print(self.selected_card.rect)
            return True # We releasing the card

    # Realease the card and return the realesed card
    def release_card(self):
        if self.selected_card == None:
            return None

        released_card = self.selected_card   
        self.selected_card = None
        self.hand_cards = pygame.sprite.Group(self.hand_copy)

        return released_card


