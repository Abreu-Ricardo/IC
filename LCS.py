# Programador: Ricardo Abreu
# Descricao: Computa a maior subseq entre duas strings.
# e imprime a maior cadeia comum

### OBS: Este algoritimo eh utilizado em conjunto com outro
###      para tratar muitas entradas em um arquivo.
###      Caso nao for usar para muitas entradas tire o comentario 
###      no fim deste programa

class LCS:
    def __init__(self):
        self.string = None
        self.tamanho = None

    def sub_seq(X, Y):
        # Construcao da matriz do LCS, por isso mais 2 em cada coluna e linha

        X.tamanho = len(X.string) + 2
        Y.tamanho = len(Y.string) + 2
        cont = 0               # Preenche Matriz
        palavra = None         # Salva o ultimo igual caractere da sequencia

        
        matriz = [[0 for x in range(X.tamanho)] for j in range(Y.tamanho)]       # Declaracao da matriz
        
        for i in range(2,X.tamanho):     # Preenchendo a primeira linha da matriz
            matriz[0][i] = X.string[i-2]
            
        for i in range(2,Y.tamanho):     # Preenchendo a primeira coluna da matriz
            matriz[i][0] = Y.string[i-2] 


        for i in range(2,Y.tamanho):     # Comeca a partir do 2, pq tam +2 da matriz
            for j in range(2,X.tamanho):
                
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

        return LCS.maior_seq(matriz, X.tamanho, Y.tamanho)

    def maior_seq(matriz, tamX, tamY):      #### Percorre a matriz e guarda no array vetor
        vetor = []
        i = tamY-1
        j = tamX-1

        ### Impressao da matriz ###
        # for i in range(tamY):
        #     for j in range(tamX):
        #         print(matriz[i][j], end=' ')
        #     print()

        while i >= 0 and j >= 0:
            if matriz[i][j-1] == matriz[i][j]:
                j = j - 1
            
            elif matriz[i-1][j] == matriz[i][j]:
                i = i - 1

            else:
                if matriz[i][0] != 0:
                    vetor.append(matriz[i][0])
                    i = i - 1

        return vetor
    
### Main ### 
# X = LCS(None, None)
# Y = LCS(None, None)

# entrada = input()
# X.string = entrada
# X.tamanho = len(X.string) + 2

# entrada = input()
# Y.string = entrada
# Y.tamanho = len(Y.string) + 2


# resposta = LCS.sub_seq(X, Y)

# resposta.reverse()
# print(resposta)