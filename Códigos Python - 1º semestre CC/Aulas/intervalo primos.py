a = int(input())
b = int(input())
tot = 1

for c in range (a, b+1):
    if c > 1:
        for d in range (2, c):
            if (c % d == 0):
                break
        else:
            print(c)
            tot += 1
print('primos:', tot)
