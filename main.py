import pygame
from deck import Deck
from hand import Hand
from enemy import Enemy
from character import Character

class Game:

    def __init__(self):
        pygame.init()
        self.SCREEN_SIZE = self.SCREEN_WIDTH, self.SCREEN_HEIGHT = (1280, 720)
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        self.clock = pygame.time.Clock()

        # Initialize character
        self.player = Character()
        self.player.adjust_player_position(self.SCREEN_HEIGHT)

        # Initialize enemy
        self.enemy = Enemy()
        self.enemy.adjust_enemy_position(self.SCREEN_HEIGHT)

        # Initialize deck
        self.deck = Deck()
        self.deck.build_deck()
        self.deck.shuffle_deck()

        # Initialize hand
        self.hand_size = 5
        self.hand = Hand()
        self.hand.draw_hand(self.deck, self.hand_size)

    def quit(self):
        pygame.quit()

    def draw(self):
        self.screen.blit(self.player.image, self.player.rect)
        self.screen.blit(self.enemy.image, self.enemy.rect)
        self.hand.draw(self.screen, self.SCREEN_WIDTH)

    def run(self):
        running = True
        while running:
            self.screen.fill((0, 0, 0))

            # Pool Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                self.hand.select_card(event)


            self.draw()

            pygame.display.flip()
            self.clock.tick(60)



game = Game()
if __name__ == "__main__":
    game.run()