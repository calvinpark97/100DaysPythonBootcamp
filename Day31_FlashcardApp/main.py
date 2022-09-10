from tkinter import *
import random

import pandas
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"
wordlist_dict = {}
selected_words = {}

#testing the pandas dataframe function
try:
    wordlist_df = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    wordlist_df = pd.read_csv("data/french_words.csv")
    wordlist_dict =wordlist_df.to_dict(orient="records")
else:
    wordlist_dict = wordlist_df.to_dict(orient="records")

#showing random word and showing the next random word
def next_word():
    global selected_words, flip_timer
    window.after_cancel(flip_timer)
    selected_words = random.choice(wordlist_dict)
    canvas.itemconfig(canvas_card_image, image=front_card)
    canvas.itemconfig(top_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=selected_words["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(canvas_card_image, image=back_card)
    canvas.itemconfig(top_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=selected_words["English"], fill="white")

def is_known():
    wordlist_dict.remove(selected_words)
    data = pandas.DataFrame(wordlist_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_word()


window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

#Creating the checkmark and exmark buttons
check_mark = PhotoImage(file="images/right.png")
ex_mark = PhotoImage(file="images/wrong.png")

check_mark_button = Button(image=check_mark, highlightthickness=0, borderwidth=0, bd=0, command=is_known)
check_mark_button.grid(row=1, column=2)
ex_mark_button = Button(image=ex_mark, highlightthickness=0, borderwidth=0, bd=0, command=next_word)
ex_mark_button.grid(row=1, column=1)

#Creating the Canvas for language and the word
front_card = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_card_image = canvas.create_image(400,263, image=front_card)
back_card = PhotoImage(file="images/card_back.png")

#Language card text
card_language = "French"
top_text = canvas.create_text(400,150, fill="black", font=("Ariel", 40, "italic"))

#Language_word_
word_text = canvas.create_text(400, 253, fill="black", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=1, columnspan=2)

next_word()

window.mainloop()