# Programador: Ricardo Abreu
# Inicio da clivagem de algoritmos
from LCS import LCS

arquivo = open("entrada.txt", "r")

# Criando objetos
pept1 = LCS()
pept2 = LCS()
resultado = None

for aux in arquivo:
    try:
        if aux[0] == '>':
            continue
        else:
            pept1.string = aux
            if pept2.string == None:    # Primeiro linha do arquivo
                pept2.string = pept1.string
            
            elif pept1.string != pept2.string:
                resultado = LCS.sub_seq(pept1, pept2)

                if len(pept2.string) < len(resultado):
                    pept2.string = resultado

    except EOFError:        ### FIM DO ARQUIVO
        break   

resultado.reverse() #Inverter o vetor

print(resultado)
print("Tamanho da seq:", len(resultado))
print()

arquivo.close()