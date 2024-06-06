import sys

num_arquivo = 0

# Ler soh os 2 primeiros valores da linha
def busca_valor(i, menor_valor):
	valor_linha  = ""

	valor_linha +=  i[11]
	valor_linha +=  i[12]
	valor_linha +=  i[13]
	valor_linha +=  i[14]
	valor_linha +=  i[15]
	valor_linha +=  i[16]
	valor_linha +=  i[17]

	print( float(valor_linha) )

	return float(valor_linha)
	# if float(valor_linha) < menor_valor:
	# 	menor_valor = float(valor_linha)



if __name__ == "__main__":
	arquivo = open(sys.argv[1], "r")
	linhas = arquivo.readlines()

	flag = 0
	menor_valor_total = -1000.00
	cont_num_arquivo = 0
	
	
	for i in range(0, len(linhas)):
		#print(linhas[i])
		
		if linhas[i][0] == "-":
			cont_num_arquivo += 1
			print(linhas[i][0])
		
			for j in range(0,9):
				i += 1

				valor_da_func = busca_valor(linhas[i], menor_valor_total)

				if menor_valor_total < valor_da_func:
					menor_valor_total = valor_da_func
					num_arquivo = cont_num_arquivo
	
	print(f"Maior valor entre os arquivos: {menor_valor_total}, numero do arquivo:{num_arquivo}")
	arquivo.close()

	arquivo = open("MELHOR_RESULADO.txt", "w+")
	arquivo.write(f"Maior valor entre os arquivos: {menor_valor_total}, numero do arquivo:{num_arquivo}")