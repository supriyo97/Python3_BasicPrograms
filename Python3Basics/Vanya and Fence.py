n,h = map(int,input().split())

a = list(map(int, input().split(' ')))
w = []
for j in a:
    if j > h:
        width = 2
    else:
        width = 1
    w.append(width)

print(sum(w))
