from typing import Callable
import numpy as np

def optimality(func: Callable):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return  np.argmax(res, axis=1)
    return wrapper