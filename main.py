import sys
import pygame
from deck import Deck
from hand import Hand
from enemy import Enemy
from player import Player
from button import Button
from card import Cards

pygame.init()
pygame.display.set_caption("Cursed Ascent")

class Game:

    def __init__(self):

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
        self.button = Button("assets/buttons/end_turn.png", 1100, 600)

        # Initialize hand
        self.hand = Hand()
        self.hand.draw_hand(self.deck)

        self.font = pygame.font.SysFont(None, 20)

    # Drawing
    def draw(self):
        if self.enemy.hp > 0:
            self.screen.blit(self.enemy.image, self.enemy.rect)

        if self.player.hp > 0:
            self.screen.blit(self.player.image, self.player.rect)

        if self.player.turn:
            self.hand.draw(self.screen, self.SCREEN_WIDTH)

            
        self.screen.blit(self.button.image, self.button.rect)

    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    # Events
    def handle_button_events(self, event):
        clicked = self.button.is_clicked(event)

        if clicked and self.player.turn == True:
            self.hand.draw_hand(self.deck)
            self.player.turn = not self.player.turn
            self.enemy.turn = not self.enemy.turn

    def handle_card_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.player.turn == True:
            if self.hand.select_card():
                released_card = self.hand.release_card()
                if released_card:
                    if released_card.rect.colliderect(self.player.rect) and self.player.hp > 0:
                        self.apply_card_effects(released_card, self.player)
                    elif released_card.rect.colliderect(self.enemy.rect) and self.enemy.hp > 0:
                        self.apply_card_effects(released_card, self.enemy)


    # Game logic
    def apply_buff_effects(self, buff):
        pass

    def apply_card_effects(self, card, target):
        if card.type == "attack":
            target.hp -= 5
        
        elif card.type == "defense":
            target.armor += 5

        self.hand.hand_cards.remove(card)
        self.deck.card_graveyard.append(card)
        self.hand.hand_copy.remove(card)

    def enemy_logic(self):

        if self.enemy.turn and self.enemy.hp > 0:
            self.enemy.attack(self.player)
            self.enemy.turn = not self.enemy.turn
            self.player.turn = not self.player.turn

        else:
            self.player.turn = True


    # Menu

    def quit(self):
        pygame.quit()
        sys.exit()

    def main_menu(self):
        while True:

            self.screen.fill((0, 0, 0))

            self.play_button = Button("assets/buttons/play.png", self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 2)
            self.quit_button = Button("assets/buttons/quit.png", self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 2 + 200)

            self.screen.blit(self.play_button.image, self.play_button.rect)
            self.screen.blit(self.quit_button.image, self.quit_button.rect)

            # Pool Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                
                if self.play_button.is_clicked(event):
                    self.game()

                if self.quit_button.is_clicked(event):
                    self.quit()

            pygame.display.flip()
            self.clock.tick(60)

        
    def game(self):
        while True:
            self.screen.fill((0, 0, 0))

            # Pool Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

                self.handle_card_events(event)
                self.handle_button_events(event)


            self.enemy_logic()
            self.draw()

            pygame.display.flip()
            self.clock.tick(60)


game = Game()
if __name__ == "__main__":
    game.main_menu()
    pygame.quit()