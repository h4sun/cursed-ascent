import pygame
from character import Character
from enemy import Enemy

class Hand:

    def __init__(self):
        self.hand_cards = pygame.sprite.Group()
        self.hand_copy = []

        self.player = Character()
        self.enemy = Enemy()


    def draw_hand(self, deck, hand_size):
        if (len(deck.deck_cards) >= hand_size):
            while len(self.hand_cards) < hand_size and deck.deck_cards:
                card = deck.draw_card()
                self.hand_cards.add(card)
                deck.remove_card(card) # Remove the card we draw from the deck
        else:
            self.hand_cards.add(deck.deck_cards) # If the hand_size bigger than the deck we simply add all deck to hand 
            deck.remove_card(self.hand_cards) # Remove the all cards we draw

        for card in self.hand_cards:
            self.hand_copy.append(card) # Copy hand it is solve the topmost card when the select
          

    def draw(self, surface, screen_width):
        num_cards = len(self.hand_cards)
        
        # Calculate the initial left position relative to the center of the screen
        total_width = (num_cards * 150) + (num_cards - 1)
        start_x = (screen_width - total_width) // 2

        # Adjust the position of the cards
        get_selected_card = self.__get_selected_card()
        if get_selected_card == None:
            card_top = 600
            current_x = start_x
            for card in self.hand_cards:
                card.rect.left = current_x
                current_x += card.rect.width
                card.rect.top = card_top
                

        # Kart secili değilken üstüne geldiğinde kartı y ekseninde biraz büyüt eğer kart secili ise mousela birlikte kartı hareket ettir.
        # If the card is not selected give some enlarging when you hovering the mouse on the cards if the card is selected move the card with the mouse.
        mouse_pos = mouse_x, mouse_y = pygame.mouse.get_pos()
        if get_selected_card == None:
            for card in self.hand_cards:
                if card.rect.collidepoint(mouse_pos): 
                    card.rect.top -= 100
        else:
            get_selected_card.rect.left = mouse_x - (get_selected_card.rect.width / 2)
            get_selected_card.rect.top = mouse_y - (get_selected_card.rect.height / 2)

        self.hand_cards.draw(surface)

    def select_card(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            
            get_selected_card = self.__get_selected_card()
            if get_selected_card == None:
                for card in self.hand_cards:
                    if card.rect.collidepoint(mouse_pos):
                        self.hand_cards.remove(card)
                        self.hand_cards.add(card)
                        card.selected = True
                        card.image.fill("red")
            else:
                self.hand_cards.empty()
                self.hand_cards = pygame.sprite.Group(self.hand_copy)
                self.check_card_collide(get_selected_card, self.player, self.enemy)
                get_selected_card.selected = False
                get_selected_card.image = get_selected_card.original_image.copy()


    def check_card_collide(self, card, player, enemy):
        if card.type == "attack":
            if card.rect.colliderect(enemy.rect):
                self.hand_cards.remove(card)
                self.hand_copy.remove(card)
        elif card.type == "defense":
            if card.rect.colliderect(player.rect):
                self.hand_cards.remove(card)
                self.hand_copy.remove(card)



    def __get_selected_card(self):
        for card in self.hand_cards:
            if card.selected:
                return card
        else:
            return None
    







