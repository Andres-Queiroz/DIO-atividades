n = int(input())
a = n
f = 1

while a > 0:
    print('{}' .format(a), end = '')
    print(' x ' if a > 1 else ' = ', end ='')
    f = f * a
    a -= 1
print('{}'.format(f))

