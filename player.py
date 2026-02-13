import pygame
from setting import *



class Player(pygame.sprite.Sprite):
    def __init__(self,groups, collision_sprite, spawn_candy_event):
        super().__init__(groups)
        self.spawn_candy_event = spawn_candy_event
        self.image = pygame.Surface(PLAYER_SIZE)
        self.image.fill('white')
        self.rect = self.image.get_rect(center =(PLAYER_STARTING_POINT))
        self.direction = pygame.Vector2()
        self.speed = 400
        self.collision_sprite = collision_sprite
        self.score = 0

        
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

    def collisions(self):
        collided_sprites = pygame.sprite.spritecollide(self, self.collision_sprite, True)
        
        if collided_sprites:
       
            pygame.event.post(self.spawn_candy_event)
            self.score += 1
            print('score is', self.score)
 

    def update(self, dt):
        self.input()
        self.move(dt)
        self.collisions()

        
    