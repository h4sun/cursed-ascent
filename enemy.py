import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__
        self.image = pygame.image.load("assets/enemies/angry_man.png").convert()
        self.rect = self.image.get_rect()
        self.turn = False
        self.live = True
        self.adjust_enemy_position(720)

        # Enemy Stats
        self.hp = 10
        self.current_hp = 10
        self.armor = 0
        self.damage = 5

    def adjust_enemy_position(self, screen_height):
        self.rect.top = (screen_height - self.rect.height) // 2
        self.rect.left = 1050

    def enemy_intend():
        pass

    def attack(self, target):
        waiting_for_enemy_attack = True
        attack_start_time = 0
        attack_delay = 5000 
        if waiting_for_enemy_attack:
            current_time = pygame.time.get_ticks()
            if current_time - attack_start_time >= attack_delay:
                # Burada animasyon da başlatabilirsin
                target.current_hp -= 5
                waiting_for_enemy_attack = False

