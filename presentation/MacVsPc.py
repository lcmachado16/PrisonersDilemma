import numpy as np
import random

class QLearningAgent:
    def __init__(self, state_size, action_size, rewards, alpha=0.1, gamma=0.99, epsilon=0.5, epsilon_decay=0.999, epsilon_min=0.01):
        self.state_size     = state_size
        self.action_size    = action_size
        self.alpha          = alpha  # Learning Rate 
        self.gamma          = gamma  # Fator de desconto
        self.epsilon        = epsilon  # Probabilidade de escolher uma ação aleatória
        self.epsilon_decay  = epsilon_decay  # Fator de decaimento do epsilon
        self.epsilon_min    = epsilon_min  # Valor mínimo para o epsilon

        # Inicializando a Q-table com valores aleatórios entre o mínimo e o máximo das recompensas para cada estado
        self.q_table = np.zeros((state_size, action_size))
        for state in range(state_size):
            min_reward = min(min(rewards[state].values(), key=lambda x: x[0])[0], min(rewards[state].values(), key=lambda x: x[1])[1])
            max_reward = max(max(rewards[state].values(), key=lambda x: x[0])[0], max(rewards[state].values(), key=lambda x: x[1])[1])
            self.q_table[state] = np.random.uniform(min_reward, max_reward, action_size)
            # self.q_table = np.zeros((state_size, action_size)) # Inicializando a Q-table com zeros


    def choose_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            return random.randint(0, self.action_size - 1)  # Ação aleatória
        else:
            return np.argmax(self.q_table[state])  # Ação com maior valor Q

    def update_q_table(self, state, action, reward, next_state):
        old_value   = self.q_table[state][action]
        next_max    = np.max(self.q_table[next_state])
        # new_value   = (1 - self.alpha) * old_value + self.alpha * (reward + self.gamma * next_max)
        new_value   = (1 - self.alpha) * old_value + self.alpha * (reward + self.gamma * next_max  - old_value)
        self.q_table[state][action] = new_value


class PrisonersDilemmaEnv:
    def __init__(self):
        # Stochastic ----------------------------------------------------------
        # self.states = {'s0': 0, 's1': 1} #__STOCHASTIC_GAME_VERSION___
        self.states = {'s0': 0}        #__SINGLE_STATE_VERSION___
        self.state = self.states['s0']  # O jogo começa no estado 's0'
        self.actions = {
            0: 'Mac', 1: 'Pc'}  # Definindo as ações
            # 0: 'Ballet', 1: 'Football'}  # Definindo as ações
        
        self.rewards = {
        # ==== PRISONER'S DILEMMA ===================================
            0: {  # Recompensas para o estado 's0'
                (0, 0): [2, 2],  
                (0, 1): [0, 0], 
                (1, 0): [0, 0],  
                (1, 1): [1, 1]   
            }

        #==========================================================

        }
        self.exploration_proba              = 1  # Fator de decaimento do epsilon
        self.min_exploration_proba          = 0.01
        self.exploration_decreasing_decay   = 0.001
       

    def reset(self):
        # self.state = random.choice(list(self.states.values()))  # Reset para um estado aleatório
        return self.state
        # return self.states['s0']  ##__SINGLE_STATE_VERSION___

    def step(self, state, action1, action2):
        reward1, reward2 = self.rewards[state][(action1, action2)]
        next_state = state          ##__SINGLE_STATE_VERSION___
        next_state = self.reset()   ##__STOCHASTIC_GAME_VERSION___
        done = True  # O jogo termina após uma ação
        return next_state, (reward1, reward2), done

    def train(self, agent1, agent2, episodes):
        joint_action_count = np.zeros((agent1.action_size, agent2.action_size))  # Contador de ações conjuntas

        for episode in range(episodes):
            state = self.reset()
            done = False
            while not done:
                action1 = agent1.choose_action(state)
                action2 = agent2.choose_action(state)
                joint_action_count[action1][action2] += 1  # Contabilizando a ação conjunta
                next_state, (reward1, reward2), done = self.step(state, action1, action2)

                agent1.update_q_table(next_state, action1, reward1, state)
                agent2.update_q_table(next_state, action2, reward2, state)

            self.exploration_proba = max(self.min_exploration_proba, np.exp(-self.exploration_decreasing_decay*episode))
            agent1.epsilon = self.exploration_proba
            agent2.epsilon = agent1.epsilon  # Garantir que o epsilon seja o mesmo para ambos os agentes
    
        return joint_action_count

if __name__ == "__main__":

    env = PrisonersDilemmaEnv()
    actions = env.actions
    print(actions[0], actions[1])
    state_size = len(env.states)

    agent1 = QLearningAgent(state_size=state_size, action_size=2, rewards=env.rewards)
    agent2 = QLearningAgent(state_size=state_size, action_size=2, rewards=env.rewards)
    
    
    episodes = 10000
    joint_action_count = env.train(agent1, agent2, episodes)
    print("Q-table do Agente 1 após treinamento:")
    print(agent1.q_table)
    print("Q-table do Agente 2 após treinamento:")
    print(agent2.q_table)
    print("=============================================================")
    print(f"Contagem de ações conjuntas após {episodes} episódios:")
    print(f"[{actions[0]:3} , {actions[0]:3}]: (0, 0): {joint_action_count[0][0]}")
    print(f"[{actions[0]:3} , {actions[1]:3}]: (0, 1): {joint_action_count[0][1]}")
    print(f"[{actions[1]:3} , {actions[0]:3}]: (1, 0): {joint_action_count[1][0]}")
    print(f"[{actions[1]:3} , {actions[1]:3}]: (1, 1): {joint_action_count[1][1]}")
    print("=============================================================")


    print(f"Exploração do Agente 1 após {episodes} episódios: {agent1.epsilon}")

