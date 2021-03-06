import numpy as np


string_list = []
np.set_printoptions(suppress=True, formatter={'float_kind': '{:20.2f}'.format}, linewidth=130)


# adds two matrices
def add_matrices(matrix_1, matrix_2):
    matrix_sol = [[0 for x in range(len(matrix_1))] for y in range(len(matrix_2))]
    string_list.clear()
    if check(matrix_1, matrix_2):
        string_list.append('Solution of addition')
        string_list.append("\n")
        for x in range(len(matrix_1)):
            for y in range(len(matrix_2)):
                matrix_sol[x][y] = matrix_1[x][y] + matrix_2[x][y]
        string_list.append(np.matrix(matrix_sol))


# subtracts two matrices
def subtract_matrices(matrix_1, matrix_2):
    matrix_sol = [[0 for x in range(len(matrix_1))] for y in range(len(matrix_2))]
    string_list.clear()
    if check(matrix_1, matrix_2):
        string_list.append('Solution of the subtraction')
        string_list.append("\n")
        for x in range(len(matrix_1)):
            for y in range(len(matrix_2)):
                matrix_sol[x][y] = matrix_1[x][y] - matrix_2[x][y]
        string_list.append(np.matrix(matrix_sol))


# multiplies two matrices
def multiply_matrices(matrix_1, matrix_2):
    matrix_sol = [[0 for x in range(len(matrix_1))] for y in range(len(matrix_2[0]))]
    string_list.clear()
    if check(matrix_1, matrix_2):
        string_list.append('Solution of the multiplication')
        string_list.append("\n")
        for x in range(len(matrix_1)):
            for y in range(len(matrix_2[0])):
                for t in range(len(matrix_2)):
                    matrix_sol[x][y] += (matrix_1[x][t] * matrix_2[t][y])
        string_list.append(np.matrix(matrix_sol))


def check(matrix_1, matrix_2):
    if len(matrix_1) == len(matrix_2) and len(matrix_1[0]) == len(matrix_2[0]):
        return True
    elif len(matrix_1) == len(matrix_2) and len(matrix_1[0]) == len(matrix_1):
        return True
    return False