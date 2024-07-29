
class PrisonersDilemmaEnv:
    def __init__(self):
        self.states = {'s0': 0}  # Definindo o único estado como 's0'
        self.state = self.states['s0']  # O jogo começa no estado 's0'
        self.actions = {0: 'cooperate', 1: 'defect'}  # Definindo as ações
        self.rewards = {
            (0, 0): (-1, -1),  # Ambos cooperam
            (0, 1): (-3, 0),   # Agente 1 coopera, Agente 2 trai
            (1, 0): (0, -3),   # Agente 1 trai, Agente 2 coopera
            (1, 1): (-2, -2)   # Ambos traem
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
