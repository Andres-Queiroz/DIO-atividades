a = ['b','x','d','v','e','r','e','p',]

def misterio(x,v,n):
    i=0
    while i < n and v[i] != x:
        i += 1
    if i < n:
        return i
    else:
        return -1
    return
