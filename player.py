import pygame
from setting import *



class Player(pygame.sprite.Sprite):
    def __init__(self,groups):
        super().__init__(groups)

        self.image = pygame.Surface(PLAYER_SIZE)
        self.image.fill('white')
        self.rect = self.image.get_rect(center =(PLAYER_STARTING_POINT))
        self.direction = pygame.Vector2()
        self.speed = 400


        
    def input(self):
        self.keys = pygame.key.get_pressed()

        if self.keys[pygame.K_d]:
            self.direction.x = 1
            self.direction.y = 0
        elif  self.keys[pygame.K_a]:
            self.direction.x = -1
            self.direction.y = 0
        elif self.keys[pygame.K_w]:
                self.direction.y = -1
                self.direction.x = 0
        elif  self.keys[pygame.K_s]:
                self.direction.y = 1
                self.direction.x = 0


            
    def move(self, dt):
        self.rect.x += self.speed *self.direction.x * dt
        self.rect.y += self.speed *self.direction.y * dt

 

    def update(self, dt):
        self.input()
        self.move(dt)


        
    