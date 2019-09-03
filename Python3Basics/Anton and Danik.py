ng = int(input())
l = list(map(str,input().split()))
for i in l:
    if i.count('A') > i.count('D'):
        print("Anton")
    elif i.count('A') < i.count('D'):
        print("Danik")
    else:
        print("Friendship")
