def prime(n):
    f = 0
    for i in range(1,n+1):
        if n%i == 0:
            f+=1
    return(f==2)


def sumprimes(l):
    return sum(n for n in l if prime(n))
