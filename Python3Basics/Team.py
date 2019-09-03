n = int(input())
l = []
coun = 0
for i in range(n):
    a = list(map(int,input().split()))
    l.append(a)

for k in l:
    if k.count(1) >= 2:
        coun +=1
        
print(coun)
