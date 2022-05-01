s = 0
num = int(input())
for c in range(1,num):
    num = int(input())
    if num%2 == 0:
        s = s + num
print(s)
