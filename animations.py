from PIL import Image, ImageTk


def display(piece, canvas):
    img = Image.open('').convert("RGBA")
    img = img.resize((100,100), Image.LANCZOS)
    frames = ImageTk.PhotoImage(img)
    canvas.itemconfig(1, image=frames)