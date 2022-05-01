import random
v = [0]*11 #cria vetor com 10 posições iniciados com ZEROS
#sorteiode 10000 numeros de 0 a 10 e contagem de numero
for i in range(10000):
  n = random.randint(0,10)
  v[n] = v[n] + 1
#exibe o numero e a quantidade de vezes que foi executado
for i in range(len(v)):
  print(i, "foi sorteado ", v[i], 'vezes')
