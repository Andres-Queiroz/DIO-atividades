def maiores(M, N):
    maiores = []
    for x in range(len(M)):
        if M[x] > N:
            maiores.append(M[x])
    return maiores

M = [1,2,5,7,4,8,1,9]
N = int(input())
print('Matriz:', M)
print('Maiores que',N,':',maiores(M,5))
