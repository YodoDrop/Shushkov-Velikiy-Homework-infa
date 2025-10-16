from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("400x400")




mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))


ttk.Entry(mainframe).grid(row=0,column=0, columnspan=5,sticky="ew")

ttk.Button(mainframe, text='1').grid(column=0, row=1)


root.mainloop()
