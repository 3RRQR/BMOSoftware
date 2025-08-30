import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
emotion = "happy"

from animations import generate_playlist, animate

# Setting some window properties
root.title("BMO")
root.geometry("640x480")#window size
root.configure(bg="#c9e4c3")
root.overrideredirect(True)#no window bar

label = tk.Label(root, bg="#c9e4c3")
label.pack(expand=True)#expand true centers label
generate_playlist(emotion)
animate(emotion, label, root)

root.mainloop()