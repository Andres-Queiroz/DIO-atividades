def rec(n):
    if n ==3:
        print('3')
        return rec(n-1)
    elif n==2:
        print('2')
        return rec(n-1)
    elif n==1:
        return 1
print(rec(3))
