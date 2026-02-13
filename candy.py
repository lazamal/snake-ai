import pygame

class Candy(pygame.sprite.Sprite):
    def __init__(self, groups,spawn_location):
        super().__init__(groups)

        self.spawn_location = spawn_location
        self.image = pygame.Surface([20,20])
        self.image.fill('orange')
        self.rect = self.image.get_rect(center = (spawn_location))
    