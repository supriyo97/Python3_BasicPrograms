def LSearch(elements,key): #Linear Search function
    if key in elements:
        return (f"Element found in {elements.index(key)+1} positon" )
    else:
        return ("Element not found!!!")

a = []
n = int(input("Enter the no of element: "))
for i in range(n):
    k = int(input("Enter the element: "))
    a.append(k)
key = int(input("Enter the element to be found: "))
print(a)
LSearch(a,key)
