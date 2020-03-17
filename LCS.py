# Programador: Ricardo Abreu
# Descricao: Calcula a maior subseq entre duas strings.
# Sendo a primeira String a maior

# OBS:colocar a maior string primeiro

def sub_seq(X, Y):
    tamX = len(X)+2
    tamY = len(Y)+2
    cont = 0               # Preenche Matriz
    palavra = None         # Salva o caractere da sequencia

    #print(tamX-2, tamY-2, "tamahos sem alteracao")
    
    matriz = [[0 for x in range(tamX)] for j in range(tamY)]
    
    for i in range(2,tamX):
         matriz[0][i] = X[i-2]
         
    for i in range(2,tamY):
         matriz[i][0] = Y[i-2] 


    for i in range(2,tamY): # Laco ta certo
        for j in range(2,tamX):
                                                                                      # DIMINUINDO APENAS DAS CADEIAS X E Y
            if matriz[i][0] == matriz[0][j] and matriz[0][j] != palavra:              # Diminuir 3 devido comecar 2 casas para frente,
                palavra = matriz[0][j]                                                # e diminuir mais 1, devido comecar do 0 o vetor
                cont = cont + 1                                                 
            
            elif j == 2 and i != 2:
                cont = matriz[i-1][j-1] + 1 # Recebe da diagonal mais 1
            
            elif matriz[i][j-1] >= matriz[i-1][j]:
                cont = matriz[i][j-1]
            
            elif matriz[i][j-1] <= matriz[i-1][j]:
                cont = matriz[i-1][j]

            matriz[i][j] = cont
    
    
    # Imprimir Matriz
    for i in range(tamX-1):
        for j in range(tamY+1):
            print(matriz[i][j], end=' ')
        print()


X = input()
Y = input()

print()
subMAX = sub_seq(X, Y)