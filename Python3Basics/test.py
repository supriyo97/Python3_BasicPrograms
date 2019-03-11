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
b1 = tk.Button(win,Text = "Submit", command = show())
b1.pack()

win.mainloop()

print(2+3)


