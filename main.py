import tkinter as tk
import animations

root = tk.Tk()
emotion = "idle"


root.title("BMO")
root.geometry("640x480")    #window size
root.configure(bg="#c9e4c3")
#root.overrideredirect(True)    #no window bar

canvas = tk.Canvas(root, width=640, height=480, bg="#c9e4c3")
canvas.pack()

animations.display('eyebrows',9,canvas)


root.mainloop()