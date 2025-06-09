import gym
import math
import random

class Reconstruction:
    def __init__(self, P, S_0, y=None):
        self.P = P                                  # Словарь со значениями
        self.S = [s for s in P]                     # Простраснтво состояний
        self.S_0 = S_0                              # Начальное состояние
        self.state = S_0                            # Текущее состояние
        self.action = None                          # Действие
        self.reward = 0                             # Награда
        self.y = y                                  # Коэфициент дисконтирования

    def get_state(self):
        return self.state

    def get_action(self):
        return [a for a in P[self.state]]

    def transition_func(self): # переход рандомный, поскольку еще нет оптимальных политик
        states_weights = [i for i in self.P[self.state][random.choice(self.get_action())]]
        weights = [i[0] for i in states_weights]

        next_state = random.choices(states_weights, weights=weights, k=1)[0]

        print('states_weights', states_weights)
        print('weights', weights)
        print('next_state', next_state[1])

        return next_state

    def reward_func(self):
        if self.y:
            self.reward = self.reward + self.P[self.state][self.action][0][2] * math.exp(-0.1 * self.y)
        else:
            self.reward = self.reward + self.P[self.state][self.action][0][2]
        return self.reward

    def v_function(self):
        pass


P = gym.make('FrozenLake-v1').env.P

model = Reconstruction(P, 0)
model.transition_func()