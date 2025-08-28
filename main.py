import tkinter as tk

root = tk.Tk()

# Setting some window properties
root.title("BMO")
root.configure(background="#49bc9f")
root.minsize(200, 200)
root.maxsize(500, 500)
root.geometry("300x300+50+50")


image = tk.PhotoImage(file="025.gif")
tk.Label(root, image=image).pack()

root.mainloop()