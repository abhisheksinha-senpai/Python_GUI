from tkinter import *

root = Tk()

#Creating a label widget
myLabel = Label(root, text = "Hello World")

#Shoving it onto the screen
myLabel.pack()

#Create the loop to update the GUI
root.mainloop()