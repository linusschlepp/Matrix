from matrix_calculations import solve_matrix, print_list, generate_random_vector, generate_random_matrix
from operations import add_matrices, multiply_matrices, print_list_operations


def define_matrix(size):
    matrix = [[0 for x in range(size)] for y in range(size)]

    print("Please enter the matrix you have in mind")
    for x in range(size):
        for y in range(size):
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
            proportions = int(input())
        except ValueError:
            print("Wrong input"+"\n")
            continue

        print ("Enter the operations, you want to execute")
        input_user = input()

        if input_user == 'random':
            solve_matrix(generate_random_matrix(proportions, proportions), generate_random_vector(proportions))
            print_list()
        elif input_user == 'solve':
            solve_matrix(define_matrix(proportions), define_vector(proportions))
            print_list()
        elif input_user == 'multiply':
            multiply_matrices(define_matrix(proportions), define_matrix(proportions))
            print_list_operations()
        elif input_user == 'add':
            add_matrices(define_matrix(proportions), define_matrix(proportions))
            print_list_operations()
