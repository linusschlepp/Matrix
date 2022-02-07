from matrix_calculations import solve_matrix, print_list, generate_random_vector, generate_random_matrix
from matrix_operations import add_matrices, multiply_matrices, print_list_operations


def define_matrix(am_rows, am_col):
    matrix = [[0 for x in range(am_rows)] for y in range(am_col)]

    print("Please enter the matrix you have in mind")
    for x in range(am_rows):
        for y in range(am_col):
            matrix[x][y] = float(input(str(x)+"/"+str(y)+": "))

    return matrix


def define_vector(size):
    vector = []

    print("Please enter the vector you have in mind")
    for x in range(size):
        vector.append(float(input(str(x)+": ")))

    return vector


if __name__ == '__main__':

    while True:
        print("Enter the proportions of your vector and matrix")
        try:
            size_rows = int(input("Enter the amount of rows"))
            size_cols = int(input("Enter the amount of columns"))
        except ValueError:
            print("Wrong input"+"\n")
            continue

        print ("Enter the operations, you want to execute")
        input_user = input()

        if input_user == 'random':
            solve_matrix(generate_random_matrix(size_rows, size_cols), generate_random_vector(size_cols))
            print_list()
        elif input_user == 'solve':
            solve_matrix(define_matrix(size_rows, size_cols), define_vector(size_rows))
            print_list()
        elif input_user == 'multiply':
            multiply_matrices(define_matrix(size_rows, size_cols), define_matrix(size_rows))
            print_list_operations()
        elif input_user == 'add':
            add_matrices(define_matrix(size_rows, size_cols), define_matrix(size_rows))
            print_list_operations()
