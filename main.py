import pygame
from deck import Deck
from hand import Hand

class Game:
    
    def __init__(self):
        pygame.init()

        SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (1280, 720)
        hand_size = 5

        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()

        self.deck = Deck()
        self.deck.shuffle_deck()

        self.hand = Hand()
        self.hand.draw_hand(self.deck, hand_size)
        self.hand.update_positions(SCREEN_WIDTH)

    def quit(self):
        pygame.quit()


    def draw(self):
        for i, card in enumerate(self.hand.cards):      
            self.screen.blit(card.image, card.rect)

    def run(self):
        running = True
        while running:

            # Pool Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.draw()

            pygame.display.flip()
            self.clock.tick(60)



game = Game()
if __name__ == "__main__":
    game.run()