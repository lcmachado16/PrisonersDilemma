from Player import Player
import numpy as np 
# ========== Game ============================================== #  
# Class Game
class Game: 
    def __init__(self, gameRules):
        self.name    = gameRules['name']
        self.actions = gameRules['actions']
        self.rewards = gameRules['rewards']
        self.players = self.__create_players()




    def __create_players(self):
        min_reward = np.array(self.rewards).min()
        max_reward = np.array(self.rewards).max()
        player1 = Player(1, self.actions, min_reward, max_reward)
        player2 = Player(2, self.actions, min_reward, max_reward)
        return [player1, player2]