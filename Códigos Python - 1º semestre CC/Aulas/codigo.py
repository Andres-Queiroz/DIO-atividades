# coding=utf-8
while True:
    try:
        x = input()
        print(x)
    except(EOFError): #Executado quando chega EOFError erro de linhas
        break
