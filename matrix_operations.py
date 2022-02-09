string_list = []
import numpy as np


# np.set_printoptions(suppress=True, formatter={'float_kind': '{:20.2f}'.format}, linewidth=130)
# TODO: Remove unnecessary print statements

# TODO: Make it all printable

def add_matrices(matrix_1, matrix_2):
    string_list.clear()
    if check(matrix_1, matrix_2):
        string_list.append('Solution of addition')
        string_list.append("\n")
        for x in range(len(matrix_1)):
            sb = []
            for y in range(len(matrix_2)):
                sb.append(str(matrix_1[x][y] + matrix_2[x][y]) + " ")
            string_list.append(str(sb))
            string_list.append("\n")


def subtract_matrices(matrix_1, matrix_2):
    string_list.clear()
    if check(matrix_1, matrix_2):
        string_list.append('Solution of addition')
        string_list.append("\n")
        for x in range(len(matrix_1)):
            sb = []
            for y in range(len(matrix_2)):
                sb.append(str(matrix_1[x][y] - matrix_2[x][y]) + " ")
            string_list.append(str(sb))
            string_list.append("\n")

# TODO: This looks horrible, try to fix it
def multiply_matrices(matrix_1, matrix_2):
    string_list.clear()
    if check(matrix_1, matrix_2):
        string_list.append('Solution of the multiplication')
        string_list.append("\n")
        for x in range(len(matrix_1)):
            sb = []
            for y in range(len(matrix_1[0])):
                for t in range(len(matrix_1[0])):
                    sb.append(str(matrix_1[x][y] * matrix_2[t][y]) + " ")

                string_list.append(str(sb))
                string_list.append("\n")

            print(string_list)


def check(matrix_1, matrix_2):
    if len(matrix_1) == len(matrix_2) and len(matrix_1[0]) == len(matrix_2[0]):
        return True
    elif len(matrix_1) == len(matrix_2) and len(matrix_1[0]) == len(matrix_1):
        return True

    return False


def print_list_operations():
    for x in string_list:
        print(x)
    string_list.clear()
