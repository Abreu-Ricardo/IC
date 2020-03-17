# colocar a maior string primeiro

def sub_seq(X, Y):
    tamX = len(X)+2
    tamY = len(Y)+2
    cont = 0
    palavra = None

    print(tamX-2, tamY-2, "tamhos sem alteracao")
    
    matriz = [[0 for x in range(tamX)] for j in range(tamY)]
    
    for i in range(2,tamX):
         matriz[0][i] = X[i-2]
         
    for i in range(2,tamY):
         matriz[i][0] = Y[i-2] 

    print("X->", tamX, "Y->", tamY)

    for i in range(2,tamX-1):
        print("i=",i)
        for j in range(2,tamY+1):
            print("j=",j)
            if X[i-3] == Y[j-3] and X[i-3] != palavra: # Pq comeca com 2, e nas palavras precisam ser reduzidas em 2
                palavra = X[i-2]
                cont = cont + 1
            matriz[i][j] = cont

    # Imprimir Matriz

    for i in range(tamX-1):
        #print("i=",i)
        for j in range(tamY+1):
            #print("j=",j)
            print(matriz[i][j], end=' ')
        print()


X = input()
Y = input()

print()
subMAX = sub_seq(X, Y)