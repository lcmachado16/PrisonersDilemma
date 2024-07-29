
import random 
from old.qtable import QTable
# ========== Player ============================================== # 
# Class Player 
class Player(): 
    def __init__(self,id, actions, min_reward, max_reward):
        self.id = id
        self.actions = actions
        self.choice = {action: 0 for action in self.actions}
        alpha = 0.1 
        
        self.qTable = QTable(alpha, self.actions,min_reward, max_reward)

    def choose_action(self) -> str:
        #starts with random action
        epsilon = 0.95  
        if random.uniform(0,1) <= epsilon:
            action = min(self.qTable.values, key=self.qTable.values.get)
        else: 
            action = self.actions[random.randint(0, len(self.actions)-1)]
        return action
    
    def update_reward(self,action, reward):
        self.choice[action] = self.choice[action] + 1 
        self.qTable.update_q(action,reward)

    def print_choices(self):
        print("Player {} rewards:".format(self.id))
        for action in self.choice:
            print("\t{}: {}".format(action, self.choice[action]))
        self.qTable.print()