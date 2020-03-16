def sub_seq(X, Y):
    tamX = len(X)+2
    tamY = len(Y)+2
    
    matriz = [[0 for x in range(tamX)] for j in range(tamY)]
    
    for i in range(tamX-2):
         matriz[0][i+2] = X[i]
         
    for i in range(tamY-2):
         matriz[i+2][0] = Y[i] 
        
    for i in range(tamX):
        for j in range(tamY):
            print(matriz[i][j], end='')
        print()


X = input()
Y = input()

print()
subMAX = sub_seq(X, Y)