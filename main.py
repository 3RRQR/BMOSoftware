import tkinter as tk
import random
import time

root = tk.Tk()



import animations 

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

def animation(frame=0, mood=animations.blinking, dur=animations.blinkdur):
    label.config(image=mood[frame])
    root.after(random.randint(dur[0], dur[1]), animation, (frame+1) % len(mood))

animation()
 
root.mainloop()

