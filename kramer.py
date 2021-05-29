import numpy as np
from numpy import linalg as linalg

a = np.array([[2, -1, 5], [1, 1, -3], [2, 4, 1]])
b = np.array([10, -2, 1])


def kramer_solve(a, b):

    kramer_solve = []

    if a.shape[1] == len(b):
        for col in range(a.shape[1]):
            c = a.copy()
            c[:, col] = b.T
            kramer_solve.append(linalg.det(c) / linalg.det(a))

        print(kramer_solve)

    else:
        print("Wrong size matrix!")
