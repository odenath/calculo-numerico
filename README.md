# Algoritmos de Gauss e Gauss-Seidel

Este repositório contém implementações dos algoritmos de Gauss e Gauss-Seidel para resolver sistemas de equações lineares.

## Gauss

O algoritmo de eliminação de Gauss é um método direto para resolver sistemas de equações lineares. Ele utiliza a eliminação de variáveis para transformar o sistema em uma forma escalonada triangular superior, permitindo então obter a solução de forma direta.

O código `gauss.py` implementa o algoritmo de eliminação de Gauss. Ele solicita ao usuário o número de linhas e colunas da matriz, bem como os valores da matriz de coeficientes e do vetor B. Em seguida, realiza a eliminação de Gauss para obter a solução do sistema. A solução é exibida na saída padrão.

## Gauss-Seidel

O método de Gauss-Seidel é um método iterativo para resolver sistemas de equações lineares. Ele utiliza uma abordagem de aproximações sucessivas, atualizando iterativamente as incógnitas até atingir uma solução convergente.

O código `gauss_seidel.py` implementa o algoritmo de Gauss-Seidel. Ele solicita ao usuário o número de linhas e colunas da matriz, bem como os valores da matriz de coeficientes e do vetor B. Além disso, é necessário fornecer uma aproximação inicial `X0`, o número máximo de iterações e uma tolerância para o critério de parada. O algoritmo então realiza as iterações do método de

## ---------------------------------------------------------------------------------------------------------------------------

Feito sob a supervisão da professora Tânia da Universidade Unifil
