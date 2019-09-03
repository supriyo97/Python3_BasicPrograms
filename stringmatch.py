x = input().lower()
y = input().lower()
sumx = 0
sumy = 0
if(len(x)== len(y)):
    for i in x:
        sumx+=ord(i)
    for j in y:
        sumy+=ord(j)
if(sumx==sumy):
    print("0")
elif(sumx<sumy):
    print("-1")
else:
    print("1")
