import pygame
from deck import Deck
from hand import Hand
from enemy import Enemy
from player import Player
from button import Button
from card import Cards

class Game:

    def __init__(self):
        pygame.init()
        self.SCREEN_SIZE = self.SCREEN_WIDTH, self.SCREEN_HEIGHT = (1280, 720)
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        self.clock = pygame.time.Clock()

        # Initialize all cards
        self.cards = Cards()

        # Initialize player
        self.player = Player()

        # Initialize enemy
        self.enemy = Enemy()

        # Initialize deck
        self.deck = Deck(self.cards.cards)
        self.deck.shuffle_deck()

        # Initialize buttons
        self.button = Button(1100, 600)

        # Initialize hand
        self.hand = Hand()
        self.hand.draw_hand(self.deck)

    def draw(self):
        if self.enemy.live:
            self.screen.blit(self.enemy.image, self.enemy.rect)
        
        if self.player.live:
            self.screen.blit(self.player.image, self.player.rect)

        if self.player.turn:
            self.hand.draw(self.screen, self.SCREEN_WIDTH)

            
        self.screen.blit(self.button.image, self.button.rect)

    def handle_button_events(self, event):
        clicked = self.button.click(event)

        if clicked and self.player.turn == True:
            self.hand.draw_hand(self.deck)
            self.player.turn = not self.player.turn
            self.enemy.turn = not self.enemy.turn

    def handle_card_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.player.turn == True:
            if self.hand.select_card():
                released_card = self.hand.release_card()
                if released_card:
                    if released_card.rect.colliderect(self.player.rect) and self.player.live:
                        self.apply_card_effects(released_card, self.player)
                    elif released_card.rect.colliderect(self.enemy.rect) and self.enemy.live:
                        self.apply_card_effects(released_card, self.enemy)


    def apply_card_effects(self, card, target):
        if card.type == "attack":
            target.hp -= 5
        
        elif card.type == "defense":
            target.armor += 5

        self.hand.hand_cards.remove(card)
        self.hand.hand_copy.remove(card)

    def enemy_logic(self):
        if self.enemy.turn and self.enemy.live:
            self.enemy.attack(self.player)
            self.enemy.turn = not self.enemy.turn
            self.player.turn = not self.player.turn

        else:
            self.player.turn = True


    def run(self):
        running = True
        while running:
            self.screen.fill((0, 0, 0))

            # Pool Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                self.handle_card_events(event)
                self.handle_button_events(event)


            self.enemy_logic()
            self.draw()

            pygame.display.flip()
            self.clock.tick(60)


        pygame.quit()



game = Game()
if __name__ == "__main__":
    game.run()