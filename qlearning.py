import numpy as np
import random

# ========== Game  ========== # 
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
        reward1 = reward[0]
        reward2 = reward[1]
        self.players[0].update_reward(actions[0], reward1)
        self.players[1].update_reward(actions[1], reward2)

        print("Reward: ", reward)

    def play_matches(self, n):
        for i in range(n):
            self.play_match()

# ========== Player ========== # 
class Player(): 
    def __init__(self,id, actions):
        self.id = id
        self.actions = actions
        self.rewards = {action: 0 for action in actions}
        self.qTable = QTable(0.1, actions)

    def choose_action(self) -> str:
        action = actions[0] if random.random() <= 0.5 else actions[1]
        return action
    
    def update_reward(self,action, reward):
        self.rewards[action] = self.rewards[action] + 1 
        self.qTable.update_q(action,reward)

    def print_rewards(self):
        print("Player {} rewards:".format(self.id))
        for action in self.rewards:
            print("\t{}: {}".format(action, self.rewards[action]))
        self.qTable.print()
    

# ========== QTable ========== # 
class QTable(): 
    def __init__(self, alpha,actions):
        self.alpha = alpha
        self.values = {action: 0 for action in actions}
    

    def update_q(self, action, reward ):
        self.values[action] = self.values[action]+ self.alpha * (reward - self.values[action])

    def print(self):
        print("\tQTable:")
        for action in self.values:
            print("\t==> {:10}: {}".format(action, self.values[action]))

# ========== MAIN ========== # 
if __name__ == '__main__':
    # Prisoner's Dilemma Game
    actions = ['Cooperate', 'Defect']
    rewards = [[[3, 3], [0, 5]], [[5, 0], [1, 1]]]

    player1 = Player(1, actions)
    player2 = Player(2, actions)
    players = [player1, player2]




    # Start the game
    game = Game(players, actions, rewards)

    # === Play n Games === # 
    print(player1.choose_action())
    game.play_matches(40000)

    # === Print results === #
    for i in range(2):
        print("================ Player {} Results ================".format(i+1))
        players[i].print_rewards()
  
  



