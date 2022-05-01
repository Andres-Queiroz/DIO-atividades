a = int(input())
b = int(input())

if a <= b:
    for z in range(a,b+1):
        while a <= b:
            for x in range(1,10+2):
                tab = a * x
                if x == 11:
                    print('----------')

                else:
                    print(f'{a} x {x} = {tab}')
                
            a += 1

else:
    print('Nenhuma tabuada no intervalo!')


