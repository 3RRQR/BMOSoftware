import tkinter as tk
import random

emotions = {
    "happy": {
        "frames": [tk.PhotoImage(file=f'assets/happy/{i}.png') for i in range(1, 5)],
        "weights": {0: 3, 1: 1, 2: 2, 3: 3, 4: 3},
        "playlist": []
    },

    "sad": {
        "frames": [tk.PhotoImage(file=f'assets/sad/{i}.png') for i in range(1, 4)],
        "weights": {0: 1, 1: 2, 2: 3, 3: 4},
        "playlist": []
    },
    
    "bored": {
        "frames": [tk.PhotoImage(file=f'assets/bored/{i}.png') for i in range(1, 6)],
        "weights": {0: 3, 1: 3, 2: 4, 3: 1, 4: 5, 5: 6},
        "playlist": []
    },

    "angry": {
        "frames": [tk.PhotoImage(file=f'assets/angry/{i}.png') for i in range(1, 5)],
        "weights": {0: 1, 1: 3, 2: 2, 3: 4, 4: 5},
        "playlist": []
    },
    
    "idle": {
        "frames": [tk.PhotoImage(file=f'assets/idle/{i}.png') for i in range(1, 3)],
        "weights": {0: 3, 1: 3, 2: 1},
        "playlist": []
    },

    "shockedsad": {
        "frames": [tk.PhotoImage(file=f'assets/shocked/{i}.png') for i in range(1, 4)],
        "weights": {0: 1, 1: 1, 2: 1, 3: 1},
        "playlist": []
    },

    "shockedhappy": {
        "frames": [tk.PhotoImage(file=f'assets/shocked/{i}.png') for i in range(1, 3)],
        "weights": {0: 1, 1: 1, 2: 1},
        "playlist": []
    },

    "roboto": {
        "frames": [tk.PhotoImage(file=f'assets/shocked/{i}.png') for i in range(1, 6)],
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

    delay = random.randint(100, 5000)
    root.after(delay, animate, emotion, label, root)
    print("next")

