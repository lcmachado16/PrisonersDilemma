import numpy as np
import random

class QLearningAgent:
    def __init__(self, state_size, action_size, alpha=0.1, gamma=0.99, epsilon=0.1):
        self.state_size = state_size
        self.action_size = action_size
        self.alpha  = alpha  # Taxa de aprendizagem
        self.gamma = gamma  # Fator de desconto
        self.epsilon = epsilon  # Probabilidade de escolher uma ação aleatória
        self.q_table = np.zeros((state_size, action_size))  # Inicializando a Q-table com zeros

    def choose_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            return random.randint(0, self.action_size - 1)  # Ação aleatória
        else:
            return np.argmax(self.q_table[state])  # Ação com maior valor Q

    def update_q_table(self, state, action, reward, next_state):
        best_next_action = np.argmax(self.q_table[next_state])
        td_target = reward + self.gamma * self.q_table[next_state][best_next_action]
        td_error = td_target - self.q_table[state][action]
        self.q_table[state][action] += self.alpha * td_error

    def train(self, env, episodes):
        actions_count = np.zeros(self.action_size)  # Contador de ações tomadas
        for episode in range(episodes):
            state = env.reset()
            done = False
            while not done:
                action = self.choose_action(state)
                actions_count[action] += 1  # Contabilizando a ação tomada
                next_state, reward, done, _ = env.step(action)
                self.update_q_table(state, action, reward, next_state)
                state = next_state
        return actions_count
    


class PrisonersDilemmaEnv:
    def __init__(self):
        self.states = {'s0': 0}  # Definindo o único estado como 's0'
        self.state = self.states['s0']  # O jogo começa no estado 's0'
        self.actions = {0: 'cooperate', 1: 'defect'}  # Definindo as ações
        self.rewards = {
            # general matrix of game,
            #  where C means cooperate (remain silent)
            #  and D means defect (implicate the other):
            (0, 0): (-1, -1),       #(c,c) (remain silent, remain silent)
            (0, 1): (-20, 0),        #(c,d) Agent 1 remain silent, Agent2 implicate other
            (1, 0): (0, -20),        #(d,c) Agent1 implicate other, Agent2 remain silent
            (1, 1): (-10, -10)      #(d,d) both implicate other
        }

    def reset(self):
        return self.state

    def step(self, action):
        # Ação do segundo jogador é escolhida aleatoriamente (pode ser ajustada)
        opponent_action = random.randint(0, 1)
        reward = self.rewards[(action, opponent_action)][0]
        next_state = self.state  # O único estado é 's0'
        done = True  # Um único estado, o jogo termina após uma ação
        return next_state, reward, done, opponent_action

class BatlleOfSexesEnv:
    def __init__(self):
        self.states = {'s0': 0}  # Definindo o único estado como 's0'
        self.state = self.states['s0']  # O jogo começa no estado 's0'
        self.actions = {0: 'Ballet', 1: 'Footbal'}  # Definindo as ações
        self.rewards = {
            # general matrix of game,
            #  where C means cooperate (remain silent)
            #  and D means defect (implicate the other):
            (0, 0): (1, 4),       #(c,c) (remain silent, remain silent)
            (0, 1): (0, 0),        #(c,d) Agent 1 remain silent, Agent2 implicate other
            (1, 0): (0, 0),        #(d,c) Agent1 implicate other, Agent2 remain silent
            (1, 1): (4, 1)      #(d,d) both implicate other
        }

    def reset(self):
        return self.state

    def step(self, action):
        # Ação do segundo jogador é escolhida aleatoriamente (pode ser ajustada)
        opponent_action = random.randint(0, 1)
        reward = self.rewards[(action, opponent_action)][0]
        next_state = self.state  # O único estado é 's0'
        done = True  # Um único estado, o jogo termina após uma ação
        return next_state, reward, done, opponent_action


if __name__ == "__main__":
    # env = PrisonersDilemmaEnv()
    env = BatlleOfSexesEnv()
    agent = QLearningAgent(state_size=1, action_size=2)
    agent = QLearningAgent(state_size=1, action_size=2)
    
    episodes = 10000
    actions_count = agent.train(env, episodes)
    print("Q-table após treinamento:")
    print(agent.q_table)
    print(f"Contagem de ações após {episodes} episódios:")
    print(f"Cooperate (0): {actions_count[0]}")
    print(f"Defect (1): {actions_count[1]}")
    # Verificar convergência para o equilíbrio
    if actions_count[1] > actions_count[0]:
        # print("O agente convergiu para o equilíbrio de Nash (defect).")
        print(f'O agente convergiu para {env.actions[1]}') 
    else:
        # print("O agente não convergiu para o equilíbrio de Nash.")
        print(f"O agente não convergiu para o equilíbrio de Nash.")
