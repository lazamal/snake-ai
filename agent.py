import torch
import random
import numpy as np
from collections import deque, namedtuple
from main import Game

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001
point = namedtuple('point', 'x,y')


class Agent:
    def __init__(self):
        self.number_of_games = 0
        self.epsilon = 0 #control randomness
        self.gamma = 0 #discount rate
        self.memory  = deque(maxlen=MAX_MEMORY) # popleft()
        # todo model, trainer


def get_state(self, game):
    # head is (x, y)
    head = game.player.rect.center 
    
    # 1. Define points relative to the head
    # Assuming your grid/player size is 20
    p_left  = point(head[0] - 20, head[1])
    p_right = point(head[0] + 20, head[1])
    p_up    = point(head[0], head[1] - 20)
    p_down  = point(head[0], head[1] + 20)

    # 2. Check current direction (using your Player's direction attribute)
    dir_l = game.player.direction.x == -1
    dir_r = game.player.direction.x == 1
    dir_u = game.player.direction.y == -1
    dir_d = game.player.direction.y == 1

    state = [
        # Danger Straight
        (dir_r and game.is_collision(p_right)) or 
        (dir_l and game.is_collision(p_left)) or 
        (dir_u and game.is_collision(p_up)) or 
        (dir_d and game.is_collision(p_down)),

        # Danger Right (relative to current head direction)
        (dir_u and game.is_collision(p_right)) or 
        (dir_d and game.is_collision(p_left)) or 
        (dir_l and game.is_collision(p_up)) or 
        (dir_r and game.is_collision(p_down)),

        # Danger Left
        (dir_d and game.is_collision(p_right)) or 
        (dir_u and game.is_collision(p_left)) or 
        (dir_r and game.is_collision(p_up)) or 
        (dir_l and game.is_collision(p_down)),

        # Current Direction
        dir_l, dir_r, dir_u, dir_d,

        # Food Location
        game.candy.rect.centerx < head[0], # food left
        game.candy.rect.centerx > head[0], # food right
        game.candy.rect.centery < head[1], # food up
        game.candy.rect.centery > head[1]  # food down
    ]

    return np.array(state, dtype=int)

    def remember(self,state,action,reward, next_state, game_over):
        pass

    def train_short_memory(self, state,action,reward, next_state, game_over):
        pass

    def train_long_memory(self):
        pass

    def get_action(self,state):
        pass

def train():
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 0
    agent=Agent()
    game = Game()
    while True:
        # get the old state
        state_old = agent.get_state()
        # get move
        final_move = agent.get_action(state_old)
        # perform move and get new state
        reward, done, score = game.run(final_move)
        state_new = agent.get_state(game)

        #train short memory
        agent.train_short_memory(state_old, final_move, reward, state_new, done)

        # remember
        agent.remember(state_old, final_move, reward, state_new, done)

        if game_over:
            # train long memory
            game.reset()
            agent.number_of_games +=1
            agent.train_long_memory()
            if score > record:
                record = score
                # agent.model.save()
            print('Game', agent.number_of_games, 'Score', score, 'Record', record)

            



if __name__ == '__main__':
    train()


