from tkinter import *

root = Tk()

#Create a fucntion to do somrthign
def myClick():
    myLabel = Label(root, text="A button was pressed!!!")
    myLabel.pack()

#Creating a button widget
#myButton = Button(root, text="Click Me!!!", state=DISABLED)
#myButton = Button(root, text="Click Me!!!", padx=50)
myButton = Button(root, text="Click Me!!!", command=myClick, fg="blue", bg="yellow")

#Shoving it onto the screen
myButton.pack()

#Create the loop to update the GUI
root.mainloop()