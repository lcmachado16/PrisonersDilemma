import random
import time
import numpy as np
import matplotlib.pyplot as plt

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

# ========== Match  ============================================== # 
# Class Match
class Match: 
    def __init__(self, game):
        self.players = game.players
        self.actions = game.actions
        self.rewards = game.rewards 
        print("Game created")
        self.lastAction = {'p1':None,'p2': None}

    # method -> play match
    def play_match(self, epsilon):
        actions = []
        for player in self.players:
            action = player.choose_action(epsilon)
            # print("Player {} chooses action {}".format(player.id, action))
            actions.append(action)

        reward = self.rewards[self.actions.index(actions[0])][self.actions.index(actions[1])]
        for i in range(len(self.players)):  # Update rewards for both players
            self.players[i].update_reward(actions[i], reward[i])

        # print("Reward: ", reward)

    # method -> play n matches
    def play_matches(self, n, epsilon_decay=0.9999):
        epsilon = 0.05  # Initial epsilon
        epsilon_values = []  # List to store epsilon values
        for i in range(n):
            self.play_match(epsilon)
            epsilon_values.append(epsilon)  # Store the current value of epsilon
            epsilon *= epsilon_decay  # Apply epsilon decay
        return epsilon_values

# ========== Player ============================================== # 
# Class Player 
class Player(): 
    def __init__(self, id, actions, min_reward, max_reward):
        self.id = id
        self.actions = actions
        self.choiceHistory = {action: 0 for action in self.actions}
        self.alpha = 0.1 
        self.qTable = QTable(self.alpha, self.actions, min_reward, max_reward)
        self.TesteStats = {'random': 0, 'else': 0}

    def choose_action(self, epsilon) -> str:
        if random.uniform(0, 1) <= epsilon:
            self.TesteStats['random'] += 1
            action = max(self.qTable.values, key=self.qTable.values.get)
        else: 
            self.TesteStats['else'] += 1    
            action = random.choice(self.actions)
        return action
    
    def update_reward(self, action, reward):
        self.choiceHistory[action] += 1
        self.qTable.update_q(action, reward)

    def print_choices(self):
        print("Player {} rewards:".format(self.id))
        for action in self.choiceHistory:
            print("\t{}: {}".format(action, self.choiceHistory[action]))
        self.qTable.print()

# ========== QTable ============================================== # 
# QTable Class
class QTable: 
    def __init__(self, alpha, actions, min_reward, max_reward):
        self.alpha = alpha
        self.values = {action: random.uniform(min_reward, max_reward) for action in actions}

    def update_q(self, action, reward):
        self.values[action] = self.values[action] + self.alpha * (reward - self.values[action])

    def print(self):
        print("\tQTable:")
        for action in self.values:
            print("\t\t{:10}: {:2.4f}".format(action, self.values[action]))

# ========== MAIN  ============================================== # 
if __name__ == '__main__':
    # Prisoner's Dilemma Game
    prisionersDilemmaRules = { 
        'name': 'Prisoners Dilemma Game',
        'actions': ['Cooperate', 'Defect'],
        'rewards': [[[1, 1], [20, 0]], [[0, 20], [10, 10]]]
    }

    battleOfSexesRules = { 
        'name': 'Battle Of Sexes',
        'actions': ['Ballet', 'Movie'],
        'rewards':  [[[1, 4], [0, 0]], [[0, 0], [4, 1]]]
    }

    rockScissorPaperRules = {
        'name': 'Rock Scissor Paper',
        'actions': ['Rock', 'Scissor', 'Paper'],
        'rewards': [
            [[0, -1, 1]], 
            [[1, 0, -1]],
            [[-1, 1, 0]]
        ]
    }

    paretoDominanceGameRules =  {
        'name': 'Pareto Dominance Game',
        'actions': ['L', 'R'],
        'rewards': [
            [[9, 9], [0, 8]], 
            [[8, 0], [7, 7]]
        ]
    }

    # Create Game
    newGame = Game(prisionersDilemmaRules)

    # Create Match
    match = Match(newGame)
    epsilon_values = match.play_matches(1)

    print(newGame.actions)

    players = {'p1': newGame.actions, 'p2': newGame.actions}  
    print('yahoo')
    print(players['p1'])

    # Plot epsilon values
    # plt.plot(epsilon_values)
    # plt.xlabel('Matches')
    # plt.ylabel('Epsilon')
    # plt.title('Epsilon Decay over Matches')
    # plt.show()

    # Print results
    # for player in match.players:
    #     player.print_choices()

    print("TesteStats: ", match.players[0].TesteStats)
    print("TesteStats: ", match.players[1].TesteStats)