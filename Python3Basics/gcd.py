def gcd(m,n):
    if m<n:
        (m,n) = (n,m)
    while m%n != 0:
        (m,n) = (n,m%n)
    return(print("GCD/HCF of the two number: ",n))
gcd(222,3)
