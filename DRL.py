import numpy as np
import gym
import math
import random

class Reconstruction:
    def __init__(self, P, state, gamma=1, theta=1e-10):
        self.P = P                                  # Среда MDP
        self.state = state                          # Текущее состояние
        self.action = None                          # Действие
        self.reward = 0                             # Награда
        self.gamma = gamma                          # Коэфициент дисконтирования
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

    def reward_funcion(self, prev_V, prob, next_state, reward, done):
        if self.gamma:
            self.gamma = math.exp(-0.1 * self.gamma)
            reward = prob * (reward + self.gamma * prev_V[next_state] * (not done))
        else:
            reward = prob * (reward + prev_V[next_state] * (not done))

        return reward

    def get_random_policy(self):
        """
        Функция генерации случайной политики.

        Нужна для валидации функции оценки политик. Возвращает список с доступными рандомными
        действиями для каждого возможного состояния MDP.
        """
        pi = []
        for s in self.P:
            actions = list(self.P[s].keys())
            pi.append(random.choice(actions))
        return pi

    def v_function(self, prev_V):
        """
        Функция ценности состояний V

        :param prev_V:
        :return:
        """
        V = np.zeros(len(self.P))

        for s in range(len(self.P)):
            for prob, next_state, reward, done in self.P[s][pi[s]]:
                # Суммируем взвешенную ценность перехода в сосотояние s
                V[s] += self.reward_funcion(prev_V, prob, next_state, reward, done)

        return V

    def policy_evaluation(self, pi):
        """
        Алгоритм оценки политик
        """
        # Инициализируем значения V-функции нулями для первой итерации
        prev_V = np.zeros(len(self.P))

        while True:
            V = self.v_function(prev_V)

            if np.max(np.abs(V - prev_V)) < self.theta:
                break

            prev_V = V.copy()

        return V

P = gym.make('FrozenLake-v1').env.P
model = Reconstruction(P, 0)

from pprint import  pprint

# pprint(P)

pi = model.get_random_policy()
print(pi)
pprint(model.policy_evaluation(pi))
