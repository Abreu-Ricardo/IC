# Programador: Ricardo Abreu
# Descricao: Calcula a maior subseq entre duas strings.
# Sendo a primeira String a maior

# OBS:colocar a maior string primeiro

def verifica_ordem(matriz, tamX, tamY, verificar, a, b):    # Verifica se na colina tem o caractere "verificar", pois se nao tiver nao pode incrementar na matriz
    flag = 0
    print(verificar)

    for i in range(2,a):
        for j in range(2,b):
            if matriz[a][0] == verificar:               # Se for vdd entao pode incrementar na matriz
                flag += 1
                print("SOU IGUAL")
                return flag
                
            else:
                print("N SOU IGUAL")
                flag += -1
    return flag


def imprime_lcs(matriz, tamX, tamY):
    vetor = []

    for i in range(tamY):
        for j in range(tamX):
            print(matriz[i][j], end=' ')
        print()
    
    # for i in range(tamY-1, -1, -1):
    #     for j in range(tamX-1, -1, -1):

    #         #print("Comeco do fim", i,j)
    #         if matriz[i][j-1] == matriz[i][j]:
    #             j = j - 1
            
    #         elif matriz[i-1][j] == matriz[i][j]:
    #             i = i - 1

    #         else:
    #             if matriz[i][0] != 0:
    #                 vetor.append(matriz[i][0])
    #                 i = i - 1
    #                 #print(vetor)

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
    
    
    
    
def sub_seq(X, Y):
    tamX = len(X)+2
    tamY = len(Y)+2
    cont = 0               # Preenche Matriz
    palavra = None         # Salva o caractere da sequencia
    flag = 1

    
    matriz = [[0 for x in range(tamX)] for j in range(tamY)]
    
    for i in range(2,tamX):
         matriz[0][i] = X[i-2]
         
    for i in range(2,tamY):
         matriz[i][0] = Y[i-2] 


    for i in range(2,tamY): # Laco ta certo
        for j in range(2,tamX):
                                                                                      # DIMINUINDO APENAS DAS CADEIAS X E Y
            if matriz[i][0] == matriz[0][j] and matriz[0][j] != palavra:              # Diminuir 3 devido comecar 2 casas para frente,
                
                flag = verifica_ordem(matriz, tamX, tamY, matriz[i][0], i ,j)
                if flag >= 0:
                    palavra = matriz[0][j]                                            # e diminuir mais 1, devido comecar do 0 o vetor
                    cont = cont + 1
                
                else:                                                                 # Caso o caractere de matriz[i][j] nao estiver na sequencia
                    cont = 0                                                 
            
            elif j == 2:
                
                flag = verifica_ordem(matriz, tamX, tamY, matriz[i][0], i ,j)
                if flag >= 0:
                    cont = matriz[i-1][j-1] + 1                 # Recebe da diagonal mais 1

                else:
                    cont = 0                                    # Se n estiver na ordem correta
            
            elif matriz[i][j-1] >= matriz[i-1][j]:
                
                flag = verifica_ordem(matriz, tamX, tamY, matriz[i][0], i ,j)
                if flag >= 0:
                    cont = matriz[i][j-1]

                else:
                    cont = 0                                    # Se n estiver na ordem correta
            
            elif matriz[i][j-1] <= matriz[i-1][j]:
                
                flag = verifica_ordem(matriz, tamX, tamY, matriz[i][0], i ,j)
                if flag >= 0:
                    cont = matriz[i-1][j]
                
                else:
                    cont = 0                                    # Se n estiver na ordem correta

            matriz[i][j] = cont

    return matriz

### Main ###
X = input()
Y = input()
cadeia_max = sub_seq(X, Y)

resposta = imprime_lcs(cadeia_max, len(X)+2, len(Y)+2)

resposta.reverse()
print(resposta)