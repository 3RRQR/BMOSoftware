import tkinter as tk
import random

root = tk.Tk()

import animations as anim

# Setting some window properties
root.title("BMO")
root.configure(background="#c9e4c3")
root.geometry("1280x720+50+50")

label = tk.Label(root, image=anim.talking[0])
label.pack()

def animation(mood, dur, frame=0):
    label.config(image=mood[frame])
    if frame==0:
        root.after(random.randint(dur[0], dur[1]), animation, mood, dur, (frame+1) % len(mood))
    else:
        root.after(dur[frame], animation, mood, dur, (frame+1) % len(mood))

animation(anim.blinking, anim.blinkdur)


root.mainloop()