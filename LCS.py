# Programador: Ricardo Abreu
# Descricao: Computa a maior subseq entre duas strings.
# e imprime a maior cadeia comum


def sub_seq(X, Y):
    tamX = len(X)+2
    tamY = len(Y)+2
    cont = 0               # Preenche Matriz
    palavra = None         # Salva o ultimo igual caractere da sequencia

    
    matriz = [[0 for x in range(tamX)] for j in range(tamY)]       # Declaracao da matriz
    
    for i in range(2,tamX):     # Preenchendo a primeira linha da matriz
         matriz[0][i] = X[i-2]
         
    for i in range(2,tamY):     # Preenchendo a primeira coluna da matriz
         matriz[i][0] = Y[i-2] 


    for i in range(2,tamY):     # Comeca a partir do 2, pq tam +2 da matriz
        for j in range(2,tamX):
            
            if  matriz[i][0] == matriz[0][j]:                               #### Caso a primeira coluna for igual a um item da linha

                    cont = matriz[i-1][j-1] + 1                 # Recebe a diagonal mais 1
            
            elif matriz[i][0] == matriz[0][j] and matriz[0][j] != palavra:  #### Se liha e coluna forem iguais, mas tem que ser diferente do ultimo caratere igual(palavra)
                
                    palavra = matriz[0][j]                      # Recebe o caratere da linha 0 com a coluna j
                    cont = cont + 1
            
            elif matriz[i][j-1] >= matriz[i-1][j]:                          #### Compara uma posicao anterior eh maior que a posicao de cima 

                    cont = matriz[i][j-1]

            elif matriz[i][j-1] <= matriz[i-1][j]:                          #### Compara uma posicao anterior eh menor que a posicao de cima

                    cont = matriz[i-1][j]

            matriz[i][j] = cont                                 # matriz sempre recebe cont(que varia com os condicionais) 

    return matriz

def maior_seq(matriz, tamX, tamY):      #### Percorre a matriz e guarda no array vetor
    vetor = []

    for i in range(tamY):
        for j in range(tamX):
            print(matriz[i][j], end=' ')
        print()

    while i >= 0 and j >= 0:
        if matriz[i][j-1] == matriz[i][j]:
            j = j - 1
        
        elif matriz[i-1][j] == matriz[i][j]:
            i = i - 1

        else:
            if matriz[i][0] != 0:
                vetor.append(cadeia_max[i][0])
                i = i - 1

    return vetor
    
### Main ###
X = input()
Y = input()
cadeia_max = sub_seq(X, Y)

resposta = maior_seq(cadeia_max, len(X)+2, len(Y)+2)

resposta.reverse()
print(resposta)