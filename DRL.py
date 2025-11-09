import numpy as np
import gym
import math
import random

class Reconstruction:
    def __init__(self, P, state, y=1, theta=1e-10):
        self.P = P                                  # Среда MDP
        self.state = state                          # Текущее состояние
        self.action = None                          # Действие
        self.reward = 0                             # Награда
        self.y = y                                  # Коэфициент дисконтирования
        self.theta = theta                          # Порог сходимости

    def get_action(self):
        return [a for a in P[self.state]]

    def transition_func(self):
        """
        Функция перехода.

        Выполняет переход в следующее состояние среды на основе текущего состояния и действия (пока что рандомного)
        случайным образом выбирает следующее состояние согласно вероятностям переходов.
        """
        available_states = [i for i in self.P[self.state][random.choice(self.get_action())]] # TO-DO: получать action из политики
        probs = [i[0] for i in available_states]

        self.state = random.choices(available_states, weights=probs, k=1)[0][1]

        return self.state

    def reward_func(self):
        if self.y:
            self.y = math.exp(-0.1 * self.y)
            self.reward = self.reward + self.P[self.state][self.action][0][2] * self.y
        else:
            self.reward = self.reward + self.P[self.state][self.action][0][2]
        return self.reward

    def get_random_policy(self):
        """
        Функция генерации случайной политики.

        Нужна для валидации функции оценки политик. Возвращает список с доступными рандомными
        действиями для каждого возможного состояния MDP.

        TO-DO: исключить терминальные состояния
        """
        pi = []
        for s in self.P:
            actions = list(P[s].keys())
            pi.append(random.choice(actions))
        return pi

    def policy_evaluation(self):
        """
        Функция оценки политик.

        TO-DO: Исключить оценку для терминальных состояний
        """
        prev_V = np.zeros(len(self.P))
        pi = self.get_random_policy()  # Генерация случайной политики

        print(pi)

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

from pprint import  pprint

pprint(
    model.P
)