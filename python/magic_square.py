def msquare(m):
    if (m%2!=0):
        k=[[0 for r in range(m)]for c in range(m)]
        r=0
        c=m//2
        for n in range(1,(m**2)+1):
            k[r][c]= n
            n=n+1
            br = (r-1)%m
            bc = (c+1)%m
            if k[br][bc]!=0:
                br=br-1
            else:
                r=br
                c=bc
    for row in k:
        print(row)
msquare(5)
