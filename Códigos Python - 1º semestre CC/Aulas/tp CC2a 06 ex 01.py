import math
import cmath
A = dir(math)
B = dir (cmath)
C = []
#A sin, cos, tan
#B tan, thip

for func1 in A:
    if func1 in B:
        C.append(func1) #adicionar em C, o que tiver em func1
print(C)


#outra solução
A = set(dir(math))
B = set(dir(cmath))
C = A.intersection(B)
print(sorted(C))  #sorted é para ordenar a lista

