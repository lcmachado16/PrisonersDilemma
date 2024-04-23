import numpy as np
import random

class Game: 
    # Constructor
    def __init__(self, players, actions, rewards):
        self.players = players
        self.actions = actions
        self.rewards = rewards 
        print("Game created")

    def play_match(self):
        actions = []
        for player in self.players:
            action = player.choose_action()
            print("Player {} chooses action {}".format(player.id, action))
            actions.append(action) 

        reward = self.rewards[self.actions.index(actions[0])][self.actions.index(actions[1])]
        # reward1 = reward[0]
        # reward2 = reward[1]
        # self.players[0].update_reward(actions[0], reward1)
        # self.players[1].update_reward(actions[1], reward2)

        print("Reward: ", reward)

    def play_matches(self, n):
        for i in range(n):
            self.play_match()

      
class Player(): 
    def __init__(self,id, actions):
        self.id = id
        self.actions = actions
        self.rewards = {action: 0 for action in actions}

    def choose_action(self) -> str:
        action = actions[0] if random.random() <= 0.50000 else actions[1]
        return action
    
    def update_reward(self,action, reward):
        self.rewards[action] = reward

    def print_rewards(self):
        print("Player {} rewards:".format(self.id))
        for action in self.rewards:
            print("\t{}: {}".format(action, self.rewards[action]))
    



if __name__ == '__main__':
    # Prisoner's Dilemma Game
    actions = ['Cooperate', 'Defect']
    rewards = [[[3, 3], [0, 5]], [[5, 0], [1, 1]]]

    gamma = 0.8     #discount factor
    alpha = 0.1     #learning rate

    player1 = Player(1, actions)
    player2 = Player(2, actions)
    players = [player1, player2]




    # Start the game
    game = Game(players, actions, rewards)
    # print(player1.choose_action())
    game.play_matches(2)

    player1.print_rewards()
  


