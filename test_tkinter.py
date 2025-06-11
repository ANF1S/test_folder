import tkinter as tk

root = tk.Tk()
root.title("Tinter Test")
root.geometry("200x100")

label = tk.Label(root, text="hallo")
label.pack(pady=20)

root.mainloop()
