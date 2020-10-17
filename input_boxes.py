from tkinter import *

root = Tk()

e = Entry(root, width=50, bg="green", borderwidth=10)
e.pack()
e.insert(0,"Enter your name")

def myClick():
    myLabel = Label(root, text="Dayum!!!" + e.get())
    myLabel.pack()

myButton = Button(root, text="Enter your name", command=myClick)
myButton.pack()

root.mainloop()