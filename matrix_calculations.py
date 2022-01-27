import random
import numpy as np

string_list = []

np.set_printoptions(suppress=True, formatter={'float_kind': '{:20.2f}'.format}, linewidth=130)


# Fix error: for some error it adds 0 at the pivots and stuff
def generate_random_vector(size_rows):
    vector = [size_rows - 1]
    for x in range(size_rows - 1):
        vector.append(float(random.randint(0, 50)))

    return vector


def generate_random_matrix(size_rows, size_col):
    matrix = [[0 for x in range(size_rows)] for y in range(size_col)]

    for x in range(size_rows):
        for y in range(size_col):
            matrix[x][y] = float(random.randint(0, 50))

    return matrix


def find_solutions(matrix, vector):
    solutions = []
    for x in range(len(matrix)):
        rowSum = 0
        for y in range(len(matrix)):
            rowSum += matrix[x][y]
        temp = vector[x] = vector[x] / rowSum
        solutions.append(temp)
        string_list.append('x' + str(x) + ': ' + str(round(solutions[x], 2)))


def check_matrix(matrix, vector):
    for x in range(len(matrix)):
        zero_counter = 0
        for y in range(len(matrix[x])):
            if matrix[x][y] == 0:
                zero_counter = zero_counter + 1
            if zero_counter == len(matrix) and vector[x] == 0:
                string_list.append('The matrix has infinite solutions!')
                return False
            if zero_counter == len(matrix):
                string_list.append('The matrix has no solution')
                return False
    return True


def show_operations(colIndex1, colIndex2, num1, num2):
    print("Row " + str(colIndex2) + " * " + str(num2) + " - " + "Row " + str(colIndex1)
          + " * " + str(num1) + "\n")


def solve_matrix(matrix, vector):
    for x in range(len(matrix)):
        if x == 0:
            print(np.matrix(print_matrix_and_vector(matrix, vector)).round())
            print()
        for y in range(len(matrix) - 1, -1, -1):
            try:
                pivot_element1 = float(get_kgv(matrix[x][x], matrix[y][x]) / matrix[y][x])
                pivot_element2 = float(get_kgv(matrix[x][x], matrix[y][x]) / matrix[x][x])
            except ZeroDivisionError:
                print('Matrix can not be solved')
                return
            if x == y:
                continue
            else:
                for t in range(len(matrix)):
                    # matrix[y][t] = round(pivot_element1 * matrix[y][t] - pivot_element2 * matrix[x][t], 2)
                    matrix[y][t] = round(pivot_element1 * matrix[y][t] - pivot_element2 * matrix[x][t], 2)
            show_operations((x + 1), (y + 1), pivot_element2, pivot_element1)
            vector[y] = round(pivot_element1 * vector[y] - pivot_element2 * vector[x], 2)
            print(np.matrix(print_matrix_and_vector(matrix, vector)))
            print()
            if not check_matrix(matrix, vector):
                return
    find_solutions(matrix, vector)


def print_matrix_and_vector(matrix, vector):
    matrix_1 = [[0 for x in range(len(matrix) + 1)] for y in range(len(matrix))]

    for x in range(len(matrix_1)):
        for y in range(len(matrix_1[0])):
            if y < len(matrix_1):
                matrix_1[x][y] = round(matrix[x][y], 2)
            else:
                matrix_1[x][y] = round(vector[x], 2)

    return matrix_1


def print_list():
    for x in string_list:
        print(x)


def get_kgv(pivot_element1, pivot_element2):
    if pivot_element1 == pivot_element2:
        return pivot_element1
    if pivot_element1 < 0:
        pivot_element1 *= -1
    if pivot_element2 < 0:
        pivot_element2 *= -1

    ret_value1 = pivot_element1
    ret_value2 = pivot_element2

    while ret_value1 != ret_value2:
        if ret_value1 < ret_value2:
            ret_value1 += pivot_element1
        else:
            ret_value2 += pivot_element2

    return ret_value1
    # Error occurs when one of the pivots is zero
