
import numpy as np


def square(n, fn = lambda x: x**2):
    """lambda function is power of 2"""
    return[fn(i) for i in range(n)]


def sigmoid(x,a=1):
    return 1/(1+np.exp(-a*x))

print(square(10))
print(sigmoid(0.0))