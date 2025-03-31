import pygame
from deck import Deck
from hand import Hand
from card import Card

class Game:

    def __init__(self):
        pygame.init()
        SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (1280, 720)
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()

        # Initialize deck
        self.deck = Deck()
        self.deck.build_deck()
        self.deck.shuffle_deck()

        # Initialize hand
        self.hand_size = 5
        self.hand = Hand()
        self.hand.draw_hand(self.deck, self.hand_size)
        self.hand.adjust_card_position(SCREEN_WIDTH)


    def quit(self):
        pygame.quit()

    def draw(self):
        self.hand.cards.draw(self.screen)

    def enlarge_card(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        card_top = 600
        for i, card in enumerate(self.hand.cards):
            if (card.rect.left < mouse_x < card.rect.left + card.rect.width and card.rect.top < mouse_y < card.rect.top + card.rect.height):
                if card.rect.top < 601 and card.rect.top > 500:
                    card.rect.top -= 100
            else:
                if i % 2 == 0:
                    card.rect.top = card_top - 5
                else:
                    card.rect.top = card_top

    def run(self):
        running = True
        while running:

            self.screen.fill((0, 0, 0))

            # Pool Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.enlarge_card()
            self.draw()

            pygame.display.flip()
            self.clock.tick(60)



game = Game()
if __name__ == "__main__":
    game.run()