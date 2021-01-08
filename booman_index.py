# Ricardo Abreu de Oliveira

aminos = {
      'L' : 4.92,
      'I' : 4.92,
      'V' : 4.04,
      'F' : 2.98,
      'M' : 2.35,
      'W' : 2.33,
      'A' : 1.81,
      'C' : 1.28,
      'G' : 0.94,
      'Y' : -0.14,
      'T' : -2.57,
      'S' : -3.40,
      'H' : -4.66,
      'Q' : -5.54,
      'K' : -5.55,
      'N' : -6.64,
      'E' : -6.81,
      'D' : -8.72,
      'R' : -14.92
    }

print("Digite a sua sequência...")
seq = input()
tam = len(seq)
index = 0.0

for i in seq:
    #print(i)
    index += aminos[i]

index =  -1.0 * (index / float(tam))
print(f"Índice de Booman: {index:2.2f}",)
