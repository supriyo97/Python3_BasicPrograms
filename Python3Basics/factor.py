def factor(n):
    f = []
    for i  in range(1,n+1):
        if n%i == 0:
            f = f + [i]
    return(f)
factor(44)
