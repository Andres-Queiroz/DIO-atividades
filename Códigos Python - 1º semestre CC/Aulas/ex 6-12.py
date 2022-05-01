a = int(input())
x=1
while x<= a:
    w,y = input().split()
    if w == 'tesoura' and (y == 'papel' or y == 'lagarto'):
        print(f'Caso #{x}: Bazinga!')
    elif w == 'papel' and (y == 'pedra' or y == 'Spock'):
        print(f'Caso #{x}: Bazinga!')
    elif w == 'pedra' and (y == 'lagarto' or y == 'tesoura'):
        print(f'Caso #{x}: Bazinga!')
    elif w == 'lagarto' and (y == 'Spock' or y ==  'papel'):
        print(f'Caso #{x}: Bazinga!')
    elif w == 'Spock' and (y == 'tesoura' or 'pedra'):
        print(f'Caso #{x}: Bazinga!')
    elif w == 'tesoura' and y == 'tesoura':
        print(f'Caso #{x}: De novo!')
    elif w == 'papel' and y == 'papel':
        print(f'Caso #{x}: De novo!')
    elif w == 'pedra' and y == 'pedra':
        print(f'Caso #{x}: De novo!')
    elif w == 'lagarto' and y == 'lagarto':
        print(f'Caso #{x}: De novo!')
    elif w == 'Spock' and y == 'Spock':
        print(f'Caso #{x}: De novo!')
    elif w == 'tesoura' and (y == 'pedra' or y == 'Spock'):
        print(f'Caso #{x}: Raj trapaceou!')
    elif w == 'papel' and (y == 'lagarto' or y == 'tesoura'):
        print(f'Caso #{x}: Raj trapaceou!')
    elif w == 'pedra' and (y == 'papel' or y == 'Spock'):
        print(f'Caso #{x}: Raj trapaceou!')
    elif w == 'lagarto' and (y == 'tesoura' or y == 'pedra'):
        print(f'Caso #{x}: Raj trapaceou!')
    elif w == 'Spock' and (y == 'papel' or y == 'lagarto'):
        print(f'Caso #{x}: Raj trapaceou!')
    x += 1
