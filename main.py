import tkinter as tk
import random

root = tk.Tk()
talk = 1

frames = [
tk.PhotoImage(file=f'assets/Rosto-1.png'),
tk.PhotoImage(file=f'assets/Rosto-2.png')
]

# Setting some window properties
root.title("BMO")
root.configure(background="#c9e4c3")
root.geometry("1280x720+50+50")


label = tk.Label(root, image=frames[0])
label.pack()

def talking(frame=0):
    label.config(image=frames[frame])
    root.after(random.randint(100, 500), talking, (frame+1) % len(frames))

talking()


root.mainloop()