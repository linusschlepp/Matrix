string_list = []


def add_matrices(matrix_1, matrix_2):
    if check(matrix_1, matrix_2):
        string_list.append('Solution of addition')
        for x in range(len(matrix_1)):
            sb = []
            for y in range(len(matrix_2)):
                sb.append(str(matrix_1[x][y] + matrix_2[x][y]) + " ")
            string_list.append(str(sb))


def multiply_matrices(matrix_1, matrix_2):
    if check(matrix_1, matrix_2):
        string_list.append('Solution of the multiplication')
        for x in range(len(matrix_1)):
            sb = []
            for y in range(len(matrix_1[0])):
                for t in range(len(matrix_1[0])):
                    sb.append(str(matrix_1[x][y] * matrix_2[t][y]) + " ")

                string_list.append(str(sb))


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
