import pprint
import numpy as np
import gym
import math
import random

class Reconstruction:
    def __init__(self, P, S_0, y=0.99, theta=1e-10):
        self.P = P                                  # Словарь со значениями
        self.S = [s for s in P]                     # Простраснтво состояний
        self.S_0 = S_0                              # Начальное состояние
        self.state = S_0                            # Текущее состояние
        self.action = None                          # Действие
        self.reward = 0                             # Награда
        self.y = y                                  # Коэфициент дисконтирования
        self.theta = theta                          # Порог сходимости

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

    def generate_random_policy(self):
        pi = []
        for s in P:
            actions = list(P[s].keys())
            pi.append(random.choice(actions))
        return pi


    def policy_evaluation(self):
        prev_V = np.zeros(len(self.P))
        pi = self.generate_random_policy()  # Генерация случайной политики
        
        while True:
            V = np.zeros(len(self.P))

            for s in range(len(self.P)):
                for prob, next_state, reward, done in self.P[s][pi[s]]:
                    V[s] += prob * (reward + self.y * prev_V[next_state] * (not done)) 

            if np.max(np.abs(prev_V - V)) < self.theta:  # Проверка сходимости
                break

            prev_V = V.copy()

        return V

    
P = gym.make('FrozenLake-v1').env.P

model = Reconstruction(P, 0)
print(model.policy_evaluation())