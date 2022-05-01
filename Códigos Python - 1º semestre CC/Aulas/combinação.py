n = int(input())
m = int(input())
a = n
b = m
f = 1
g = 1
n_m = n - m
z = 1
while a > 0  :
    f = f * a
    a -= 1
while b > 0:
    g = g * b
    b -= 1
while n_m > 0:
    z = z * n_m
    n_m -= 1
            
x = f/(z*g)
print('{}'.format(x))

