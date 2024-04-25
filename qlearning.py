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
        for i in range(2):  # Update rewards for both players
            self.players[i].update_reward(actions[i], reward[i])

        print("Reward: ", reward)

    def play_matches(self, n):
        for i in range(n):
            self.play_match()

# ========== Player ========== # 
class Player(): 
    def __init__(self,id, actions):
        self.id = id
        self.actions = actions
        self.choice = {action: 0 for action in actions}
        alpha = 0.1 
        self.qTable = QTable(alpha, actions)

    def choose_action(self) -> str:
        #starts with random action
        if self.choice[actions[0]] + self.choice[actions[1]] < 500:
            action = actions[0] if random.random() <= 0.5 else actions[1]
        else: 
            if random.random() <= 0.95: # ==== epsilon greedy === #
                action = max(self.qTable.values, key=self.qTable.values.get)
            else: 
                action = self.actions[random.randint(0,1)]
        return action
    
    def update_reward(self,action, reward):
        self.choice[action] = self.choice[action] + 1 
        self.qTable.update_q(action,reward)

    def print_choices(self):
        print("Player {} rewards:".format(self.id))
        for action in self.choice:
            print("\t{}: {}".format(action, self.choice[action]))
        self.qTable.print()
    

# ========== QTable ========== # 
class QTable(): 
    # constructor 
    def __init__(self, alpha,actions):
        self.alpha = alpha
        # self.values = {action: 0 for action in actions}
        self.values = {action: random.randint(0, 20) for action in actions}
    
    # method -> update Q-Value
    def update_q(self, action, reward):
        self.values[action] = self.values[action]+ self.alpha * (reward - self.values[action])

    # method -> print Q-Table
    def print(self):
        print("\tQTable:")
        for action in self.values:
            print("\t==> {:10}: {}".format(action, self.values[action]))

# ========== MAIN ========== # 
if __name__ == '__main__':
    # Prisoner's Dilemma Game
    actions = ['Cooperate', 'Defect']
    rewards = [[[-1, -1], [-20, 0]], [[0, -20], [-10, -10]]]

    player1 = Player(1, actions)
    player2 = Player(2, actions)
    players = [player1, player2]




    # Start the game
    game = Game(players, actions, rewards)

    # === Play n Games === # 
    print(player1.choose_action())
    game.play_matches(600000)

    # === Print results === #
    for i in range(2):
        print("================ Player {} Results ================".format(i+1))
        players[i].print_choices()
  
  



