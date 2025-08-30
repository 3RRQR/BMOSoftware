import tkinter as tk
from PIL import Image, ImageTk
import random


def load_frames(path, count):
    frames = []
    for i in range(1, count + 1):
        img = Image.open(f'{path}/{i}.png')
        img = img.resize((640, 360), Image.Resampling.LANCZOS)
        frames.append(ImageTk.PhotoImage(img))
    return frames


emotions = {
    "happy": {
        "frames": load_frames("assets/happy", 5),
        "weights": {0: 3, 1: 1, 2: 2, 3: 3, 4: 3},
        "playlist": []
    },

    "sad": {
        "frames": load_frames("assets/sad", 3),
        "weights": {0: 1, 1: 2, 2: 3, 3: 4},
        "playlist": []
    },
    
    "bored": {
        "frames": load_frames("assets/bored", 5),
        "weights": {0: 3, 1: 3, 2: 4, 3: 1, 4: 5, 5: 6},
        "playlist": []
    },

    "angry": {
        "frames": load_frames("assets/angry", 4),
        "weights": {0: 1, 1: 3, 2: 2, 3: 4, 4: 5},
        "playlist": []
    },
    
    "idle": {
<<<<<<< HEAD
        "frames": [tk.PhotoImage(file=f'assets/idle/{i}.png') for i in range(1, 3)],
=======
        "frames": load_frames("assets/idle", 2),
>>>>>>> 24e3da9 (edited animations.py)
        "weights": {0: 3, 1: 3, 2: 0},
        "playlist": []
    },

    "shockedsad": {
        "frames": load_frames("assets/shocked", 3),
        "weights": {0: 1, 1: 1, 2: 1, 3: 1},
        "playlist": []
    },

    "shockedhappy": {
        "frames": load_frames("assets/shocked", 2),
        "weights": {0: 1, 1: 1, 2: 1},
        "playlist": []
    },

    "roboto": {
        "frames": load_frames("assets/roboto", 5),
        "weights": {0: 1, 1: 1, 2: 1, 3: 1, 4: 3, 5: 3},
        "playlist": []
    },
}

def generate_playlist(emotion):
    emo = emotions[emotion]
    playlist = []
    for frame_id, weight in emo["weights"].items():
        playlist.extend([frame_id] * weight)
    random.shuffle(playlist)
    emo["playlist"] = playlist

def animate(emotion, label, root):
    emo = emotions[emotion]
    if not emo["playlist"]:
        generate_playlist(emotion)
    
    frame_id = emo["playlist"].pop(0)
    frame = emo["frames"][frame_id - 1]
    label.config(image=frame)

    delay = random.randint(100, 1000)
    root.after(delay, animate, emotion, label, root)
    print("next")

