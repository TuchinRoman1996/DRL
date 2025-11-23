import numpy as np
import gym
import random

class Evaluation:
    def __init__(self, P, state, gamma=None, theta=1e-10):
        self.P = P                                  # Среда MDP
        self.state = state                          # Текущее состояние
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
            reward = prob * (reward + self.gamma * prev_V[next_state] * (not done))
        else:
            reward = prob * (reward + prev_V[next_state] * (not done))

        return reward

    def get_random_policy(self) -> list[int]:
        """
        Функция генерации случайной политики.

        Нужна для валидации функции оценки политик. Возвращает список с доступными рандомными
        действиями для каждого возможного состояния MDP.
        """
        pi = [random.randint(0, len(self.P[s].keys()) - 1) for s in range(len(self.P))]

        return pi

    def v_function(self, pi, prev_V):
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
            V = self.v_function(pi, prev_V)

            if np.max(np.abs(V - prev_V)) < self.theta:
                break

            prev_V = V.copy()

        return V

    def policy_improvement(self, V):
        """
        Алгоритм оптимизации политик
        """
        Q = np.zeros((len(self.P), len(self.P[0])))

        for s in range(len(self.P)):
            for a in range(len(P[s])):
                for prob, next_state, reward, done in self.P[s][a]:
                    Q[s][a] += prob * (reward + self.gamma * V[next_state] * (not done))

        # new_pi = lambda s: {s: a for s, a in enumerate(np.argmax(Q, axis=1))}[s]
        new_pi = np.argmax(Q, axis=1)

        return new_pi.tolist()

    def policy_iteration(self):
        """
        Алгоритм итерации политик
        """
        pi = self.get_random_policy()

        while True:
            old_pi = pi
            V = self.policy_evaluation(pi)
            pi = self.policy_improvement(V)

            if old_pi == pi:
                break

        return V, pi


P = gym.make('FrozenLake-v1').env.P
model = Evaluation(P, state=0, gamma=1)

def print_array(arr):
    for i in range(0, len(arr), 4):
        print(arr[i:i + 4])

V, pi = model.policy_iteration()

print('Лучшая политика:')
print_array(pi)

