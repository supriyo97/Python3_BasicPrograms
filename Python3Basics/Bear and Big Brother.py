a,b = map(int,input().split())
if(a>b):
    print("Bob's weight can not be less")
while(a<=b):
    for i in range(1,200):
        a *= 3
        b *= 2
        if a>b:
            print(i)
            break
