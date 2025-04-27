import pygame
import os

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__
        self.image = pygame.image.load("assets/characters/mage.png").convert()
        self.rect = self.image.get_rect()
        self.live = True
        self.turn = True
        self.adjust_player_position(720)

        # Player Stats
        self.hp = 100
        self.current_hp = 100
        self.armor = 0

    def adjust_player_position(self, screen_height):
        self.rect.top = (screen_height - self.rect.height) // 2
        self.rect.left += 100




"""class Characters:

    def __init__(self):
        self.characters = pygame.sprite.Group()
        self.load_characters()

    def load_characters(self):
        character_images = os.listdir(path="assets/characters")

        for image in character_images:
            image = Character(f"assets/cards/{image}")
            self.characters.add(image)

    def select_character(self, character):
        pass"""