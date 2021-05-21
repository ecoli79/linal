import numpy as np

A = np.array([[4, 5, 6], [4, 8, 0], [2, 5, 1], [5, 4, 7], [3, 2, 1]])
B = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [6, 7, 8, 9, 0]])
C = np.array([[1, 2, 4, 5], [1, 3, 4, 5]])
D = np.array([[1, 1], [2, 3], [4, 4], [5, 5]])
print(A.shape[0], A.shape[1])
print(B.shape[0], B.shape[1])


def matrix_multy(A, B):
    result = []
    if A.shape[1] == B.shape[0]:

        for row in range(A.shape[0]):

            colsum = []

            for col in range(B.shape[1]):

                temp_result = int()

                for rowB in range(B.shape[0]):

                    temp_result = temp_result + A[row][rowB] * B[rowB][col]

                colsum.append(temp_result)

            result.append(colsum)

        return result

    else:
        print("The matrix shape not allow multiply. It can be same rows in A and cols in B matrix.")


print(matrix_multy(C, D))
