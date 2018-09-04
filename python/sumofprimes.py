def sumprimes(x):
    def prime(n):
        f = 0
        for i in range(1,n+1):
            if n%i == 0:
                f+=1
        return(f==2)
    plist = []
    for j in range(0,x):
        if prime(j):
            plist = plist + [j]
    return(sum(plist))

sumprimes(100)
