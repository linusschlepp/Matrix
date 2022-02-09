import math
import random
import numpy as np

string_list = []

np.set_printoptions(suppress=True, formatter={'float_kind': '{:20.2f}'.format}, linewidth=130)
# TODO: Remove unnecessary print statements

def generate_random_vector(size_rows):
    vector = [size_rows - 1]
    for x in range(size_rows - 1):
        vector.append(float(random.randint(5, 50)))

    return vector


def generate_random_matrix(size_rows, size_col):
    matrix = [[0 for x in range(size_rows)] for y in range(size_col)]

    for x in range(size_rows):
        for y in range(size_col):
            matrix[x][y] = float(random.randint(5, 50))

    return matrix


def find_solutions(matrix, vector):
    solutions = []
    for x in range(len(matrix)):
        row_sum = 0
        for y in range(len(matrix)):
            row_sum += matrix[x][y]
        temp = vector[x] = vector[x] / row_sum
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


def show_operations(col_index1, col_index2, num1, num2):
    print("Row " + str(col_index2) + " * " + str(num2) + " - " + "Row " + str(col_index1)
          + " * " + str(num1) + "\n")
    string_list.append("\n")
    string_list.append("Row " + str(col_index2) + " * " + str(num2) + " - " + "Row " + str(col_index1)
          + " * " + str(num1) + "\n")
    string_list.append("\n")


def solve_matrix(matrix, vector):
    for x in range(len(matrix)):
        if x == 0:
            print(np.matrix(print_matrix_and_vector(matrix, vector)).round())
            string_list.append(np.matrix(print_matrix_and_vector(matrix, vector)).round())
            string_list.append("\n")
            print()
        for y in range(len(matrix) - 1, -1, -1):
            try:
                pivot_element1 = float(math.lcm(abs(int(matrix[x][x])), abs(int(matrix[y][x])))) / matrix[y][x]
                pivot_element2 = float(math.lcm(abs(int(matrix[x][x])), abs(int(matrix[y][x])))) / matrix[x][x]
            except ZeroDivisionError:
                print('Matrix can not be solved')
                string_list.append("Matrix can not be solved")
                return
            if x == y:
                continue
            else:
                for t in range(len(matrix)):
                    matrix[y][t] = round(pivot_element1 * matrix[y][t] - pivot_element2 * matrix[x][t], 2)
            show_operations((x + 1), (y + 1), pivot_element2, pivot_element1)
            vector[y] = round(pivot_element1 * vector[y] - pivot_element2 * vector[x], 2)
            print(np.matrix(print_matrix_and_vector(matrix, vector)))
            print()
            string_list.append(np.matrix(print_matrix_and_vector(matrix, vector)))
            string_list.append("\n")
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
    string_list.clear()
