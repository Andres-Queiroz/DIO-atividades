a_b = input()
a,b = a_b.split()
a=int(a)
b=int(b)

if a > b:
    if a % b == 0:
        print ("Sao Multiplos")
    else:
        print ("Nao sao Multiplos")
if a < b:
    if b % a == 0:
        print ("Sao Multiplos")
    else:
        print ("Sao Multiplos")

if a == b:
   print ("Sao Multiplos") 
