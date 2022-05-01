divida = int(input())
maximo = int(input())
contador = 0
while divida > 0:
    contador += 1
    print ("pagamento: {}".format(contador))
    print("antes = {}".format(divida))
    if divida <= maximo:
        divida = 0
    else:
        divida -= maximo
    print("depois = {}".format(divida))
    print('-----')
