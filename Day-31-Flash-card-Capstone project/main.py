import tkinter as tk
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"
data = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
finally:
    to_learn = data.to_dict(orient="records")  # change orientation of DataFrame to list of dict
    current_card_list = []
    current_card = {}


def known_card():
    # find and remove current_card from to_learn
    to_learn.remove(current_card)
    #print(to_learn)
    # save to_learn to words_to_learn.csv
    new_data = pd.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)  # index=False will remove index number from dict
    # call next_card()
    next_card()


def next_card():
    global current_card_list
    global current_card
    global flip_timer
    windows.after_cancel(flip_timer)  # will cause reset timer
    current_card = random.choice(to_learn)
    current_card_list = [(key, value) for key, value in current_card.items()]
    canvas.itemconfig(canv_img, image=front_image)
    canvas.itemconfig(title, text=current_card_list[0][0], fill="black")
    canvas.itemconfig(word, text=current_card_list[0][1], fill="black")
    flip_timer = windows.after(3000, flip_card)  # will back set timer to 3000ms


def flip_card():
    canvas.itemconfig(canv_img, image=back_image)
    canvas.itemconfig(title, text=current_card_list[1][0], fill="white")
    canvas.itemconfig(word, text=current_card_list[1][1], fill="white")


windows = tk.Tk()
windows.title("Flash Cards")
windows.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

flip_timer = windows.after(3000, flip_card)

canvas = tk.Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
front_image = tk.PhotoImage(file="images/card_front.png")
back_image = tk.PhotoImage(file="images/card_back.png")
canv_img = canvas.create_image(400, 263, image=front_image)
title = canvas.create_text(400, 150, text="Title", fill="black", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", fill="black", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = tk.PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(image=wrong_image, highlightthickness=0, borderwidth=0, padx=50, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = tk.PhotoImage(file="images/right.png")
right_button = tk.Button(image=right_image, highlightthickness=0, borderwidth=0, padx=50, command=known_card)
right_button.grid(row=1, column=1)

next_card()

windows.mainloop()
