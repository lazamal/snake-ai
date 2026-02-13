from random import randint
import pygame
from setting import *
from player import Player
from candy import Candy









class Game():
    def __init__(self):

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0 
        self.spawn_candy = pygame.event.custom_type()
        self.spawn_candy_event = pygame.event.Event(self.spawn_candy)


        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.player = Player(self.all_sprites, self.collision_sprites, self.spawn_candy_event)
        self.candy = Candy((self.all_sprites, self.collision_sprites), (30,30))
  




    def run(self):
     
            while self.running:
                self.dt = self.clock.tick(60) / 1000
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    if event.type == self.spawn_candy:
                        random_x = randint(0, SCREEN_WIDTH - 20)
                        random_y = randint(0, SCREEN_HEIGHT - 20)
                        Candy((self.all_sprites, self.collision_sprites), (random_x, random_y))

                
                self.screen.fill("black")
                self.all_sprites.update(self.dt)
                self.all_sprites.draw(self.screen)



                pygame.display.update()

             

            pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()
