from typing import Callable, TypeVar, List
import numpy as np

T = TypeVar('T')

def optimality(func: Callable[..., np.ndarray]) -> Callable[..., List[int]]:
    """
    Декоратор для преобразования Q-функции в жадную политику.
    
    Применяет argmax по действиям для каждого состояния, возвращая оптимальную политику.
    
    Args:
        func: Функция, возвращающая матрицу Q[s][a].
        
    Returns:
        Обёрнутая функция, возвращающая список действий (политику).
    """
    def wrapper(*args, **kwargs) -> List[int]:
        res = func(*args, **kwargs)
        return np.argmax(res, axis=1).tolist()
    return wrapper