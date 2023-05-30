import numpy as np

import numpy as np


def create_matrix():
    rows = int(input("Informe o número de linhas da matriz: "))
    cols = int(input("Informe o número de colunas da matriz: "))
    matrix = np.zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):
            value = float(input(f"Informe o valor para a posição [{i},{j}]: "))
            matrix[i][j] = value

    return matrix


def n(matrix):
    return matrix.shape[1]


def set_matrix():
    matrix = create_matrix()
    return matrix


def pivo(matrix, value):
    return matrix[value]


def k(matrix):
    for i in range(n(matrix) - 1):
        for j in range(i + 1, n(matrix)):
            ratio = matrix[j][i] / matrix[i][i]
            matrix[j] -= ratio * matrix[i]
            print("Matriz após a alteração:")
            print(matrix)

    return matrix


def start():
    matrix = set_matrix()
    matrix = k(matrix)

    print("Matriz após a eliminação de Gauss:")
    print(matrix)


start()






'''import numpy as np


def create_matrix():
    rows = int(input("Informe o número de linhas da matriz: "))
    cols = int(input("Informe o número de colunas da matriz: "))
    matrix = np.zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):
            value = float(input(f"Informe o valor para a posição [{i},{j}]: "))
            matrix[i][j] = value

    return matrix


def n(matrix):
    return matrix.shape[1]


def set_matrix():
    matrix = create_matrix()
    return matrix


def pivo(matrix, value):
    return matrix[value]


def k(matrix):
    for i in range(n(matrix) - 1):
        for j in range(i + 1, n(matrix)):
            ratio = matrix[j][i] / matrix[i][i]
            matrix[j] -= ratio * matrix[i]

    return matrix


def start():
    matrix = set_matrix()
    matrix = k(matrix)

    print("Matriz após a eliminação de Gauss:")
    print(matrix)


start()
'''







'''
matrix1 = []


#function to know the number of variables
def n(value):
    return matrix1.shape[value]


def set_matrix(matrix):
    matrix1 = matrix

#function to know the current line in the matrix
def pivo(value):
    return matrix1


#function to know the current step in the matrix
def k():
    ...



# start the program
def start():



def l1():
    ...


def gaussian_elimination(matrix):
    n = len(matrix)

    for i in range(n):
        # Pivô atual
        pivot = matrix[i][i]

        # Reduzir os elementos abaixo do pivô para zero
        for j in range(i + 1, n):
            factor = matrix[j][i] / pivot

            # Atualizar os valores das linhas abaixo do pivô
            for k in range(i, n + 1):
                matrix[j][k] -= factor * matrix[i][k]

    # Fase de substituição inversa
    solution = [0] * n
    for i in range(n - 1, -1, -1):
        solution[i] = matrix[i][n] / matrix[i][i]
        for j in range(i - 1, -1, -1):
            matrix[j][n] -= matrix[j][i] * solution[i]

    return solution


# Exemplo de uso
matrix = np.array([[2, 1, -1, 8], [-3, -1, 2, -11], [-2, 1, 2, -3]], dtype=float)

solution = gaussian_elimination(matrix)
print("Solução:", solution)
'''