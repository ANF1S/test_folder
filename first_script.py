#!/usr/bin/env python3
from tkinter import * 
from names import nameit

root = Tk()
root.title('Code Pablo')
root.title('version 3')
root.geometry("500x350")
#testing ssh key
greet = nameit("LoL")

my_label = Label(root, text=greet, font=("Helvetica",18))
my_label.pack(pady=20)
#label = Label(root,text="hallo world")
#label.pack()
root.mainloop()