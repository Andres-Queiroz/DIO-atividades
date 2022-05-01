import string

def contar(a):
    palavra = a
    l = list(string.ascii_lowercase)
    j = 0
    for l[j] in palavra:
        print(l[j])
        j += 1
a = str(input())
print(contar(a))
        

