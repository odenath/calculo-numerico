import numpy as np


def pivo():
    ...


def k():
    ...

def hola():
    ...


# def main():
#   ...


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
