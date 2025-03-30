import pygame
from deck import Deck
from hand import Hand

pygame.init()

# Ekranı oluştur
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

deck = Deck()
deck.shuffle_cards()

hand = Hand()

max_hand = 2
hand_size = 0

print(deck.cards)

hand.draw_hand(deck, max_hand)

print(deck.cards)

running = True
while running:
    screen.fill((0, 0, 0))  # Arka planı siyah yap

    mouse_pos = mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    for i, card in enumerate(hand.cards):
        screen.blit(card.image, (250 + i * 150, 550))



    pygame.display.flip()
    clock.tick(60)

pygame.quit()
