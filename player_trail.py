import pygame
from setting import *





class Player_trail(pygame.sprite.Sprite):
    def __init__(self, groups, pos, direction):
        super().__init__(groups)

        self.image = pygame.Surface(PLAYER_SIZE)
        self.image.fill('white')
        self.rect = self.image.get_rect(center =pos)
        self.direction = pygame.math.Vector2(direction)
    
