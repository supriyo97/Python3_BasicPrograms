def g(x):
    (q,d) = (1,0)
    while (q < x):
      (q,d) = (q*10,d+1)
    return(d)
x=input("enter ur no: ")
g(x)
