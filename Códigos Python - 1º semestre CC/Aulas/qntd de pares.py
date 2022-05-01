a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())

if a % 2 == 0:
    a = 1
else:
    a=0

if b % 2 == 0:
    b = 1
else:
    b=0

if c % 2 == 0:
    c = 1
else:
    c=0

if d % 2 == 0:
    d = 1
else:
    d=0

if e % 2 == 0:
    e = 1
else:
    e=0
    
x=a+b+c+d+e
print(f'{x} valores pares')
