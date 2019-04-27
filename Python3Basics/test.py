# def Prime(n):
#     m = 0
#     for i in range(1,n+1):
#         if n%i == 0:
#             m += 1
#     return(m==2)
#
# Prime(4)

# def LeapyYear(n):
#     year = False
#     if n%4 == 0:
#         if n%100 != 0 or n%400 == 0:
#             year = True
#     return year
#
# LeapyYear(1992)

def LSearch(array,key):
    array=[]
    for i in array:
        if array[i] == key:
            return(print(f"Element found in {array.index(i+1)} positon"))
        else:
            return(print("Element not found"))

a=[]
n = int(input("Enter no of element: "))
for k in range(n):
    k = int(input("Enter elements: "))
    a.append(k)
key = int(input("Enter KEY: "))
LSearch(a,key)

import tkinter as tk

win = Tk()
# ch1 = tk.Checkbutton(win, text="Music", value=1, variable = var1)
# ch1 = tk.Checkbutton(win, text="Playing", value=2, variable = var2)
b1 = tk.Button(win,Text = "Submit")
b1.pack()

win.mainloop()

print(2+3




for i in range(1,31):
    if i%3 == 0 and i%5 == 0:
        print(f"{i} = FizzBuzz")
    else:
        if i%3==0:
            print(f"{i} = Fizz")
        if i%5==0:
            print(f"{i} = Buzz")
        else:
            print(i)




plt.xlabel("X")
plt.ylabel("Y")
plt.plot([1,5,9,12],[1,5,9,16],"ro")

import matplotlib.pyplot as plt
from scipy import stats
l = [143,242,1243,12456,7654,432,675,970,4543,34]
l.sort()
plt.plot()
plt.plot((stats.trim_mean(l,.1),)



import tkinter as t

win = t.Tk()
r = t.Checkbutton
can = t.Canvas(win,bg="red",width=300,height=350)
coord = 50,50,300,250
arc = can.create_oval(coord,start=0,extent=130,fill="blue")
can.pack()
win.mainloop()

en,ep,ee=input("Enter").split(",")


# Function to print
# the required traversal
def counterClockspiralPrint(n,arr) :
    k = 0; l = 0

    # k - starting row index
    # m - ending row index
    # l - starting column index
    # n - ending column index
    # i - iterator

    # initialize the count
    cnt = 0

    # total number of
    # elements in matrix
    total = n * n

    while (k < n and l < n) :
        if (cnt == total) :
            break

        # Print the first column
        # from the remaining columns
        for i in range(k, n) :
            print(arr[i][l], end = " ")
            cnt += 1

        l += 1

        if (cnt == total) :
            break

        # Print the last row from
        # the remaining rows
        for i in range (l, n) :
            print( arr[n - 1][i], end = " ")
            cnt += 1

        n -= 1

        if (cnt == total) :
            break

        # Print the last column
        # from the remaining columns
        if (k < n) :
            for i in range(n - 1, k - 1, -1) :
                print(arr[i][n - 1], end = " ")
                cnt += 1
            n -= 1

        if (cnt == total) :
            break

        # Print the first row
        # from the remaining rows
        if (l < n) :
            for i in range(n - 1, l - 1, -1) :
                print( arr[k][i], end = " ")
                cnt += 1

            k += 1


# Driver Code
R = input()
a = []
for i in range(n*n):

    arr = input()
    a.append(arr)
counterClockspiralPrint(R, arr)



l = [12,35,456,234,23]
l.sort()
print("Second largest no of the list: ",l[-2])


s = "Sathya @k19"
alpha = digit = lower = upper = spec = 0
s = s.replace(" ",'')
for i in s:
    if i.isalpha():
        alpha += 1
        if i.islower():
            lower += 1
        if i.isupper():
            upper += 1

    elif i.isdigit():
        digit += 1
    else:
        spec += 1

print(f"No of Alphabets: {alpha}\nNo of Lowercase: {lower}\nNo of Uppercase: {upper}\nNo of Digits: {digit}\nNo of Special Character: {spec}")


s = input("Enter a Stirng: ")
w = int(input("Enter the width of the string: "))
t = 0
for i in s:
    print(i,end = "")
    t+=1
    if t%w == 0:
        print()

l = [12,242,121,43]
print(sorted(l,reverse = True))

n = int(input())
m = n*3
pattern = [('.|.'*(2*i+1)).center(m,'-') for i in range(n//2)]
for i in pattern:
    print(i)
print('WELCOME'.center(m,'_'))
pattern.reverse()
for i in pattern:
    print(i)


import re
def isvalid(num):

    pattern = r"^(?!.*([0-9])(?:-?\1){3})[456][0-9]{3}(-?)[0-9]{4}(-?)[0-9]{4}(-?)[0-9]{4}$"
    match = re.match(pattern,num)
    if  match == None:
        return False
    return True

isvalid("4341-2341-2232-2211")

def evendigit(l,u):
    item = []
    for i in range(2000,4000):
        s = str(i)
        if (int(s[0])%2==0) and  (int(s[1])%2==0) and  (int(s[2])%2==0) and  (int(s[3])%2==0):
            item.append(s)
            print(",".join(item))
l = input("l: ")
u = input("u: ")
evendigit(l,u)

from collections import Counter
with open(f) as file:
    retunr Counter(f.read().split())


import pytube
pytube.YouTube("https://www.youtube.com/watch?v=8367ETnagHo").streams.get_
