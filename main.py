from random import randint
import pygame
from player_trail import Player_trail
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
        self.score = 0
        self.game_iteration = 0 
        self.frame_iteration = 0 

        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.trails = pygame.sprite.Group()

        self.player = Player(self.all_sprites)
        self.candy = Candy((self.all_sprites, self.collision_sprites), (30,30))

        self.player_path = []

    def reset(self):
        self.score = 0
        for trail in self.trails:
            trail.kill()
        self.player.rect.center = PLAYER_STARTING_POINT
        self.player_path =[]
        self.game_iteration+=1
        self.frame_iteration = 0

  
    def play_step(self, action):
    # 1. Update frame iteration (to prevent infinite loops)
        self.frame_iteration += 1
        
        # 2. Handle Action [Straight, Right, Left]
        # You'll need logic here to update self.player.direction based on the action
        
        # 3. Move and Check Collisions
        reward = 0
        game_over = False
        
        # Example Reward logic
        # If hit wall/trail: reward = -10, game_over = True
        # If eat candy: reward = +10
        
        # 4. Update UI and Clock
        self.all_sprites.update(self.dt)
        self.screen.fill("black")
        self.all_sprites.draw(self.screen)
        pygame.display.update()
        self.clock.tick(60)

        return reward, game_over, self.score
        

    def collisions(self):


        collided_sprites = pygame.sprite.spritecollide(self.player, self.collision_sprites, True)

        if collided_sprites:
            pygame.event.post(self.spawn_candy_event)
            self.score += 1
            print('score is', self.score)
            starting_trail_pos, starting_trail_direction = self.get_trail_at_location()
            Player_trail((self.all_sprites,self.trails), starting_trail_pos, starting_trail_direction)

        if self.player.rect.x > SCREEN_WIDTH or self.player.rect.x < 0:
            self.reset()
        if self.player.rect.y > SCREEN_HEIGHT or self.player.rect.y < 0:
            self.reset()

      
        if len(self.trails) >= 5:
        
            trail_list  = self.trails.sprites()

            body_to_check = trail_list[5:]

            for trail in body_to_check:
                if self.player.rect.colliderect(trail.rect):
                    self.reset()
                    # self.running=False


    def get_trail_at_location(self):
            offset_x = PLAYER_SIZE[0]
            offset_y = PLAYER_SIZE[1]
            if len(self.trails) == 0: 
                x_pos = self.player.rect.centerx
                y_pos = self.player.rect.centery
                direction_x = self.player.direction.x
                direction_y = self.player.direction.y

                if self.player.direction.x !=0 :
                    x_pos -= self.player.direction.x * offset_x 
                
                if self.player.direction.y !=0 :
                    y_pos -= self.player.direction.y * offset_y

           
            else:
                trail_list = self.trails.sprites()
                last_trail = trail_list[-1]
                x_pos = last_trail.rect.centerx
                y_pos = last_trail.rect.centery
                direction_x = last_trail.direction.x
                direction_y = last_trail.direction.y
           
                if last_trail.direction.x !=0 :
                    x_pos -= last_trail.direction.x * offset_x 
                
                if last_trail.direction.y !=0 :
                    y_pos -= last_trail.direction.y * offset_y

            return (x_pos,y_pos), (direction_x,direction_y)

    def trail_position(self):
        current_pos = (self.player.rect.centerx, self.player.rect.centery)
        self.player_path.insert(0,current_pos)
        if len(self.player_path) > 500:
            self.player_path.pop()


        spacing = 3

        for i, trail in enumerate(self.trails):
            index = (i + 1)  * spacing
            if index < len(self.player_path):
                trail.rect.center = self.player_path[index]

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
                self.trail_position()  
                self.collisions()
                


                pygame.display.update()

             

            pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()
