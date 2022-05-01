ch=1
vl=10
def blevers(N1):
    S=10
    for i in range(3):
        S=S+1
        
    chave = valor=0
    print("Variaveis locais de f:")
    for chave, valor in locals().items():
        print(chave,":", valor)

    return ch
z=1
w=blevers(5)

        
chave = valor=0
print("Variaveis globais:")
for chave, valor in globals().items():
    print(chave,":", valor)

    
