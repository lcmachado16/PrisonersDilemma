
import random 
# ========== QTable ============================================== # 
# QTable Class
class QTable: 
    # constructor  
    def __init__(self, alpha,actions,min_reward, max_reward):
        self.alpha = alpha
        # self.values = {action: 0 for action in actions}
             # self.values = {action: 0 for action in actions}
        self.values = {action: random.randint(min_reward, max_reward) for action in actions}
    
    # method -> update Q-Value
    def update_q(self, action, reward):
        self.values[action] = self.values[action]+ self.alpha * (reward - self.values[action])

    # method -> print Q-Table
    def print(self):
        print("\tQTable:")
        for action in self.values:
            print("\t==> {:10}: {}".format(action, self.values[action]))
