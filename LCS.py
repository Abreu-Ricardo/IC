# Programador: Ricardo Abreu
# Descricao: Calcula a maior subseq entre duas strings.
# Sendo a primeira String a maior

# OBS: COLOCAR A MAIOR STRING PRIMEIRO

def verifica_ordem(matriz, tamX, tamY, verificar, a, b):    # Verifica se na colina tem o caractere "verificar", pois se nao tiver nao pode incrementar na matriz
    flag = 0

    for i in range(2,a):
        for j in range(2,b):
            if matriz[a][0] == verificar:               # Se for vdd entao pode incrementar na matriz
                flag = 1
                return flag                             # O caractere existe entao pode voltar
                
            else:
                flag = -1
    return flag

    
def sub_seq(X, Y):
    tamX = len(X)+2
    tamY = len(Y)+2
    cont = 0               # Preenche Matriz
    palavra = None         # Salva o ultimo igual caractere da sequencia
    flag = 1

    
    matriz = [[0 for x in range(tamX)] for j in range(tamY)]       # Declaracao da matriz
    
    for i in range(2,tamX):     # Preenchendo a primeira linha da matriz
         matriz[0][i] = X[i-2]
         
    for i in range(2,tamY):     # Preenchendo a primeira coluna da matriz
         matriz[i][0] = Y[i-2] 


    for i in range(2,tamY):     # Comeca a partir do 2, pq tam +2 da matriz
        for j in range(2,tamX):
            
            if j == 2 and matriz[i][0] == matriz[0][j]:         #### Caso a primeira coluna for igual a um item da linha

                flag = verifica_ordem(matriz, tamX, tamY, matriz[i][0], i ,j)
                
                if flag >= 0:
                    cont = matriz[i-1][j-1] + 1                 # Recebe a diagonal mais 1

                else:
                    cont = 0                                    # Se n estiver na ordem correta
            
            elif matriz[i][0] == matriz[0][j] and matriz[0][j] != palavra:  ### Se liha e coluna forem iguais, mas tem que ser diferente do ultimo caratere igual(palavra)

                flag = verifica_ordem(matriz, tamX, tamY, matriz[i][0], i ,j)
                
                if flag >= 0:
                    palavra = matriz[0][j]                      # Recebe o caratere da linha 0 com a coluna j
                    cont = cont + 1
                
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

            matriz[i][j] = cont                                 # matriz sempre recebe cont(que varia com os condicionais) 

    return matriz

def maior_seq(matriz, tamX, tamY):
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