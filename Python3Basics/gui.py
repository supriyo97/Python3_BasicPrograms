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
