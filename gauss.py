def eliminacao_gauss():
    # Obter o número de linhas e colunas da matriz
    num_linhas = int(input("Digite o número de linhas da matriz: "))
    num_colunas = int(input("Digite o número de colunas da matriz: "))
    matriz_aumentada = []  # Inicializar a matriz aumentada
    vetor_b = []  # Inicializar o vetor B
    
    # Preencher a matriz aumentada e o vetor B com valores informados pelo usuário
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = float(input(f"Digite o valor da posição ({i+1}, {j+1}): "))
            linha.append(valor)
        matriz_aumentada.append(linha)
        b = float(input(f"Digite o valor de B da linha {i+1}: "))
        vetor_b.append(b)
    
    # Mostrar a matriz aumentada inicial
    print("\nMatriz aumentada inicial:")
    for i in range(num_linhas):
        for j in range(num_colunas):
            print(f"{matriz_aumentada[i][j]:.2f}", end=" ")
        print(f"| {vetor_b[i]:.2f}")
    
    # Realizar a eliminação de Gauss
    for k in range(num_linhas - 1):
        print(f"\nIteração {k+1}:")
        pivo = matriz_aumentada[k][k]

        # Aplicar pivoteamento se o pivô for igual a zero
        if pivo == 0:
            for i in range(k+1, num_linhas):
                if matriz_aumentada[i][k] != 0:
                    matriz_aumentada[k], matriz_aumentada[i] = matriz_aumentada[i], matriz_aumentada[k]
                    vetor_b[k], vetor_b[i] = vetor_b[i], vetor_b[k]
                    pivo = matriz_aumentada[k][k]
                    break

        for i in range(k+1, num_linhas):
            multiplicador = matriz_aumentada[i][k] / pivo
            vetor_b[i] -= multiplicador * vetor_b[k]
            for j in range(num_colunas):
                matriz_aumentada[i][j] -= multiplicador * matriz_aumentada[k][j]

            # Mostrar as alterações feitas
            print(f"L{i+1} <= L{i+1} - {multiplicador:.2f} * L{k+1}")

        # Mostrar o valor do multiplicador e do pivô
        print(f"Multiplicador L{k+1} = {1/pivo:.2f}")
        print(f"Pivô = {pivo:.2f}")

        # Mostrar a matriz aumentada após as alterações
        print("Matriz aumentada:")
        for i in range(num_linhas):
            for j in range(num_colunas):
                print(f"{matriz_aumentada[i][j]:.2f}", end=" ")
            print(f"| {vetor_b[i]:.2f}")

    # Mostrar a matriz escalonada triangular superior
    print("\nMatriz escalonada triangular superior:")
    for i in range(num_linhas):
        for j in range(num_colunas):
            print(f"{matriz_aumentada[i][j]:.2f}", end=" ")
        print(f"| {vetor_b[i]:.2f}")


# Executar a função
eliminacao_gauss()
