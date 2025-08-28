import tkinter as tk
import random
import sleep

root = tk.Tk()
face = random.randint(1, 30)

# Setting some window properties
root.title("BMO")
root.configure(background="#c9e4c3")
root.geometry("1280x720+50+50")


image = tk.PhotoImage(file=f'assets/Rosto-{face}.png')
tk.Label(root, image=image).pack()

root.mainloop()

