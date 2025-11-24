from typing import Dict, List, Tuple, Optional, Any
import numpy as np
import gym
import random
from utils.decorators import optimality

# Тип для переходной модели MDP: P[state][action] = [(prob, next_state, reward, done), ...]
MDPTransitionModel = Dict[int, Dict[int, List[Tuple[float, int, float, bool]]]]
Policy = List[int]  # Политика: список действий для каждого состояния


class PolicyIterationSolver:
    """
    Реализация алгоритма итерации политик (Policy Iteration) для решения MDP.
    
    Алгоритм состоит из двух этапов:
    1. Policy Evaluation - оценка текущей политики
    2. Policy Improvement - улучшение политики на основе Q-функции
    """
    
    def __init__(
        self,
        P: MDPTransitionModel,
        gamma: Optional[float] = None,
        theta: float = 1e-10
    ) -> None:
        """
        Инициализация решателя MDP.
        
        Args:
            P: Переходная модель MDP. Словарь вида P[state][action] = [(prob, next_state, reward, done), ...]
            gamma: Коэффициент дисконтирования. Если None, используется недисконтированная награда.
            theta: Порог сходимости для алгоритма оценки политики.
        """
        self.P = P
        self.gamma = gamma
        self.theta = theta

    def get_available_actions(self, state: int) -> List[int]:
        """
        Получить список доступных действий для заданного состояния.
        
        Args:
            state: Номер состояния.
            
        Returns:
            Список доступных действий для состояния.
        """
        return list(self.P[state].keys())

    def transition_func(self, state: int, action: int) -> int:
        """
        Функция перехода в следующее состояние.
        
        Случайным образом выбирает следующее состояние согласно вероятностям переходов.
        
        Args:
            state: Текущее состояние.
            action: Выбранное действие.
            
        Returns:
            Номер следующего состояния.
        """
        available_transitions = self.P[state][action]
        probs = [trans[0] for trans in available_transitions]
        
        next_state = random.choices(available_transitions, weights=probs, k=1)[0][1]
        return next_state

    def _reward_function(
        self,
        prev_V: np.ndarray,
        prob: float,
        next_state: int,
        reward: float,
        done: bool
    ) -> float:
        """
        Вычисляет взвешенную награду для перехода.
        
        Args:
            prev_V: Вектор значений V-функции на предыдущей итерации.
            prob: Вероятность перехода.
            next_state: Следующее состояние.
            reward: Награда за переход.
            done: Флаг завершения эпизода.
            
        Returns:
            Взвешенная награда с учетом дисконтирования.
        """
        if self.gamma is not None:
            return prob * (reward + self.gamma * prev_V[next_state] * (not done))
        else:
            return prob * (reward + prev_V[next_state] * (not done))

    def get_random_policy(self) -> Policy:
        """
        Генерирует случайную политику.
        
        Возвращает список со случайными действиями для каждого возможного состояния MDP.
        Используется для инициализации алгоритма итерации политик.
        
        Returns:
            Список действий для каждого состояния.
        """
        pi = [
            random.randint(0, len(self.P[s].keys()) - 1)
            for s in range(len(self.P))
        ]
        return pi

    def v_function(self, pi: Policy, prev_V: np.ndarray) -> np.ndarray:
        """
        Вычисляет функцию ценности состояний V^π.
        
        Args:
            pi: Политика (список действий для каждого состояния).
            prev_V: Вектор значений V-функции на предыдущей итерации.
            
        Returns:
            Вектор значений V-функции для всех состояний.
        """
        V = np.zeros(len(self.P))

        for s in range(len(self.P)):
            for prob, next_state, reward, done in self.P[s][pi[s]]:
                V[s] += self._reward_function(prev_V, prob, next_state, reward, done)

        return V

    @optimality
    def q_function(self, V: np.ndarray) -> np.ndarray:
        """
        Вычисляет функцию ценности действий Q.
        
        Args:
            V: Вектор значений V-функции.
            
        Returns:
            Матрица Q[s][a] - ценность действия a в состоянии s.
            Примечание: декоратор @optimality преобразует результат в политику (argmax по действиям).
        """
        num_states = len(self.P)
        num_actions = len(self.P[0]) if num_states > 0 else 0
        Q = np.zeros((num_states, num_actions))

        for s in range(num_states):
            for a in range(len(self.P[s])):
                for prob, next_state, reward, done in self.P[s][a]:
                    if self.gamma is not None:
                        Q[s][a] += prob * (reward + self.gamma * V[next_state] * (not done))
                    else:
                        Q[s][a] += prob * (reward + V[next_state] * (not done))

        return Q

    def policy_evaluation(self, pi: Policy) -> np.ndarray:
        """
        Алгоритм оценки политики (Policy Evaluation).
        
        Итеративно вычисляет V^π до сходимости.
        
        Args:
            pi: Политика для оценки.
            
        Returns:
            Вектор значений V-функции для политики π.
        """
        prev_V = np.zeros(len(self.P))

        while True:
            V = self.v_function(pi, prev_V)

            if np.max(np.abs(V - prev_V)) < self.theta:
                break

            prev_V = V.copy()

        return V

    def policy_improvement(self, V: np.ndarray) -> Policy:
        """
        Алгоритм улучшения политики (Policy Improvement).
        
        Находит жадную политику относительно текущей V-функции.
        
        Args:
            V: Вектор значений V-функции.
            
        Returns:
            Улучшенная политика (список действий для каждого состояния).
        """
        new_pi = self.q_function(V)
        return new_pi

    def policy_iteration(self) -> Tuple[np.ndarray, Policy]:
        """
        Алгоритм итерации политик (Policy Iteration).
        
        Чередует оценку и улучшение политики до сходимости.
        
        Returns:
            Кортеж (V, pi), где:
            - V: Оптимальная V-функция.
            - pi: Оптимальная политика.
        """
        pi = self.get_random_policy()

        while True:
            old_pi = pi.copy()
            V = self.policy_evaluation(pi)
            pi = self.policy_improvement(V)

            if old_pi == pi:
                break

        return V, pi

if __name__ == "__main__":
    # Пример использования
    P = gym.make('FrozenLake-v1').env.P
    
    # Создаём решатель с коэффициентом дисконтирования 1.0
    solver = PolicyIterationSolver(P, gamma=1.0)
    
    # Находим оптимальную политику
    V, pi = solver.policy_iteration()
    
    def print_array(arr: List[Any], width: int = 4) -> None:
        """Выводит массив в виде сетки заданной ширины."""
        for i in range(0, len(arr), width):
            print(arr[i:i + width])
    
    print('Оптимальная V-функция:')
    print_array(V.tolist())
    
    print('\nОптимальная политика:')
    print_array(pi)

    from pprint import pprint

    pprint(P)