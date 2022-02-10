

from asyncore import read
import matplotlib.pyplot as plt
import numpy as np

def func():
    # Carrega arquivo na memoria RAM para uso
    arquivo = open("density.xvg", "r")


    colunas = []

    # Pega todas as linhas e poe num vetor(teste) de linhas
    teste = arquivo.readlines()
    

    # for i in range(24, len(teste)):
    #     print(teste[i])

    for i in teste:
        if i[0] == '#' or i[0] == '@':
            continue

        else:
            # Cria uma matriz com duas colunas
            # a segunda coluna sao os resultados, a primeira
            # indica o numero da linha

            
            colunas.append(i.split())
            #print(f" {i.split()[1]}")
            
            

    return colunas



if __name__ == "__main__":
    print("Comecou...")
    
    r = func()

    print("TERMINOU !!! \n")
    
    #for i in r:
        #print(f"{i}")
    
    

    x = []
    y = []

    
    for i in range(len(r)):
        x.append(r[i][0])
        y.append(r[i][1])
        #print(r[i][1])
    
    #print(x)

    # x = [1,2,3]
    # y = [2,4,1]

    t = [0, 20, 40, 60, 80, 100]
    
    plt.plot(x, y, c='r')
    #plt.plot(y)
    #plt.plot(t)
    #plt.axis(x)
    plt.ylabel('density')
    plt.show()