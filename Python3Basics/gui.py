from tkinter import *


win = Tk()
def km_mile():
    conv = float(entry.get())*1.6
    t1.insert(END,conv)
win.title("Converter km to miles")
b1 = Button(win,text = "Convert",command =km_mile)
b1.grid(row=0,column=0)

entry = StringVar()
e1 = Entry(win,textvariable = entry)
e1.grid(row=0,column=1)

t1 = Text(win,height=1,width=20)
t1.grid(row=0,column=2)

win.mainloop()

from tkinter import *

win = Tk()

def Convert():
    g = float(entry.get())*1000
    pounds = float(entry.get())*2.20462
    ounces = float(entry.get())*35.274
    tg.insert(END,g)
    tp.insert(END,pounds)
    tou.insert(END,ounces)


win.title("Weight Converter")

l = Label(win,text = "KG")
l.grid(row=0,column=0)

entry = StringVar()
e1 = Entry(win,textvariable = entry)
e1.grid(row=0,column=1)

b1 = Button(win,text = "Convert", command = Convert)
b1.grid(row=0,column=2)

tg = Text(win,height = 1,width= 10)
tg.grid(row=1,column=0)

tp = Text(win,height = 1,width= 10)
tp.grid(row=1,column=1)

tou = Text(win,height = 1,width= 10)
tou.grid(row=1,column=2)

win.mainloop()


#sorting using selection sort with a GUI

from tkinter import *

win = Tk()

def selection_sort():
    arr=list()
    list = (envalue.get())
    arr.append(list.split(","))
    for i in range(len(arr)-1):
        minindex = i
        for j in range(i+1,len(arr)):
            if a[j] < a[minindex]:
                minindex = j
        arr[i],arr[minindex] = arr[minindex],arr[i]

    return arr

win.title("Selection sorting")
envalue = StringVar()
e1 = Entry(win,textvariable = envalue)
e1.grid(row = 0,column = 0)

b1 = Button(win,text = "Sort It",command = selection_sort)
b1.grid(row = 0, column = 1)

t1 = Text(win,height=1,width=40)
t1.grid(row= 1,column = 0)

win.mainloop()


l = []
a = "123,44,423"
l.append(a.split(","))
for i in l:
    for j in i:
        print(j)
