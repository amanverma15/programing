from tkinter import *
master = Tk()
e = Entry(master)
e.pack()
e.insert(0,"Enter a number between 1 and 20: ")
ea = Entry(master)
ea.pack()
b = Button(master,text = "check")
b.pack()
mainloop()
