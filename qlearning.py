#  
import random
import time

# To do 
## Implementar decaimento epsilon 
## Comecar slides
## Testar outro jogo 

# ========== Match  ============================================== # 
# Class Match
class Match: 
    # Constructor
    def __init__(self, game):
        self.players = game.players
        self.actions = game.actions
        self.rewards = game.rewards 
        print("Game created")



    #========== Methods ========== #
    # method -> play match
    def play_match(self):
        actions = []
        for player in self.players:
            action = player.choose_action()
            print("Player {} chooses action {}".format(player.id, action))
            actions.append(action) 

        reward = self.rewards[self.actions.index(actions[0])][self.actions.index(actions[1])]
        for i in range(len(self.players)):  # Update rewards for both players
            self.players[i].update_reward(actions[i], reward[i])
    
        print("Reward: ", reward)


    # method -> play n matches
    def play_matches(self, n):
        for i in range(n):
            self.play_match()

# ========== Player ============================================== # 
# Class Player 

class Player(): 
    def __init__(self,id, actions):
        self.id = id
        self.actions = actions
        self.choice = {action: 0 for action in actions}
        alpha = 0.1 
        self.qTable = QTable(alpha, actions)

    def choose_action(self) -> str:
        #starts with random action
        epsilon = 0.95  # Exploration rate @@TODO: Implement decay
        if random.random() <= epsilon:
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
    

# ========== QTable ============================================== # 
# QTable Class
class QTable(): 
    # constructor 
    def __init__(self, alpha,actions):
        self.alpha = alpha
        # self.values = {action: 0 for action in actions}
             # self.values = {action: 0 for action in actions}
        min_value = min([reward for reward in .])
        max_value = max([reward for reward in actions])
  
        while(True):
            print("Min value: ", min_value)
            print("Max value: ", max_value)
            time.sleep(10)
    
        self.values = {action: random.randint(0, 1) for action in actions}
    
    # method -> update Q-Value
    def update_q(self, action, reward):
        self.values[action] = self.values[action]+ self.alpha * (reward - self.values[action])

    # method -> print Q-Table
    def print(self):
        print("\tQTable:")
        for action in self.values:
            print("\t==> {:10}: {}".format(action, self.values[action]))


# ========== Game ============================================== #  
# Class Game
class Game: 
    def __init__(self, gameRules):
        self.name    = gameRules['name']
        self.actions = gameRules['actions']
        self.rewards = gameRules['rewards']
        self.players = self.__create_players()


    def __create_players(self):
        player1 = Player(1, self.actions)
        player2 = Player(2, self.actions)
        return [player1, player2]
    


# ========== MAIN  ============================================== # 
 # 
if __name__ == '__main__':
    # Prisoner's Dilemma Game

    prisionersDilemmaRules = { 
        'name': 'Prisioners Dilemma Game',
        'actions': ['Cooperate', 'Defect'],
        'rewards': [[[1, 1], [20, 0]], [[0, 20], [10, 10]]]
    }

    rockScissorPaperRules = {
        'name': 'Rock Scissor Paper',
        'actions': ['Rock', 'Scissor', 'Paper'],
        'rewards': 
            [[0, -1, 1], 
            [1, 0, -1],
            [-1, 1, 0]]

    }



    #Create Game
    #--- Priosoners Dilemma---------------
    newGame = Game(prisionersDilemmaRules)

    #--- Rock Scissor Paper ---------------
    # newGame = Game(rockScissorPaperRules)


    # === Create Match === #
    match = Match(newGame)
    match.play_matches(200)

    # === Print results === #
    # for player in match.players:
    #     player.print_choices()


    # for i in range(2):
    #     print("================ Player {} Results ================".format(i+1))
    #     players[i].print_choices()
  
  


