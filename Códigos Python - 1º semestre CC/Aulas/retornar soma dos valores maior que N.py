def maiores(M, N):
    maiores = []
    for x in range(len(M)):
        if M[x] > N:
            maiores.append(M[x])
    return maiores

M = [1,2,5,7,4,8,1,9]
N = int(input())
print('Soma dos elementos da Matriz:', sum(M))
print('Soma dos elementos Maiores que',N,':',sum(maiores(M,5)))
