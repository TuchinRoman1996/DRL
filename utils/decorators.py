from typing import Callable

def optimality(func: Callable):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return  res
    return wrapper