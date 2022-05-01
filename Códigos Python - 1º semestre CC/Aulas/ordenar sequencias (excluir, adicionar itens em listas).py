Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:04:37) [MSC v.1929 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 1. Converta a Tupla criada para Lista
2. Insira o valor 733 no index 11 da lista
3. Remova todos os valores 3 da lista
4. Qual elemento que mais aparece na lista?
5. Quantas vezes esse elemento aparece?
SyntaxError: invalid syntax
>>> tupla = (10,30,40,20,40,30,33,55,66,33,2,1,4,5,6,7,66,77,121,23,43,65,7,8,10,21,34,54,66,447,86,432,65,45,23,12,32,456,65,3,12)
>>> lista = list(tupla)
>>> lista
[10, 30, 40, 20, 40, 30, 33, 55, 66, 33, 2, 1, 4, 5, 6, 7, 66, 77, 121, 23, 43, 65, 7, 8, 10, 21, 34, 54, 66, 447, 86, 432, 65, 45, 23, 12, 32, 456, 65, 3, 12]
>>> lista.insert(10,733) #posição, numero
>>> lista
[10, 30, 40, 20, 40, 30, 33, 55, 66, 33, 733, 2, 1, 4, 5, 6, 7, 66, 77, 121, 23, 43, 65, 7, 8, 10, 21, 34, 54, 66, 447, 86, 432, 65, 45, 23, 12, 32, 456, 65, 3, 12]
>>> lista.remove(3)
>>> lista
[10, 30, 40, 20, 40, 30, 33, 55, 66, 33, 733, 2, 1, 4, 5, 6, 7, 66, 77, 121, 23, 43, 65, 7, 8, 10, 21, 34, 54, 66, 447, 86, 432, 65, 45, 23, 12, 32, 456, 65, 12]
>>> maximo = 0
max = 0
valor = False
for a in tupla:
  maximo = tupla.count(a)
  if maximo > max:
    max = maximo
    valor = a
print('valor',valor, 'qtd:',max)
SyntaxError: multiple statements found while compiling a single statement
>>> 