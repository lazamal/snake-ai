import pygame
from setting import *



class Player_trail(pygame.sprite.Sprite):
    def __init__(self,groups, position, index):
        super().__init__(groups)

        self.image = pygame.Surface(PLAYER_SIZE)
        self.image.fill('white')
        self.rect = self.image.get_rect(center =(position))
        self.index = index
