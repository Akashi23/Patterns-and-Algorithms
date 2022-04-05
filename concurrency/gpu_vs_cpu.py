import numba
from numba import cuda
import numpy as np
from time import time

def timer(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func


@timer
@numba.jit
def sum_with_booster(x):
    total = 0
    for i in range(x.shape[0]):
        total += x[i]
    return total

@timer
def sum_without_booster(x):
    total = 0
    for i in range(x.shape[0]):
        total += x[i]
    return total


sums = sum_with_booster(np.random.rand(100000000))
sums_without = sum_without_booster(np.random.rand(100000000))
