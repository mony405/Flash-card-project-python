from distutils.dep_util import newer

BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
import random
random_word={}
list={}
try:
    new_data=pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data=pd.read_csv("data/french_words.csv")
    list=data.to_dict(orient="records")
else:
    list=new_data.to_dict(orient="records")

#TODO 4: remove the known card and make file to The rest of the words
def known():
    list.remove(random_word)
    df = pd.DataFrame(list)
    df.to_csv("data/words_to_learn.csv", index=False)

    next_card()
#TODO 3:timer and flip card

def flip_card():
    canvas.itemconfig(background_img,image=back_img)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=random_word["English"], fill="white")

#TODO 2:next card with random word
def next_card():
    global random_word,flip_timer
    win.after_cancel(flip_timer)
    random_word=random.choice(list)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=random_word["French"], fill="black")
    canvas.itemconfig(background_img,image=front_img)
    flip_timer=win.after(3000, func=flip_card)


#TODO 1:create user interface
win=Tk()
win.title("FLASH CARD")
win.config(bg=BACKGROUND_COLOR,pady=50,padx=50)
flip_timer=win.after(3000, func=flip_card)

canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
front_img=PhotoImage(file="images/card_front.png")
back_img=PhotoImage(file="images/card_back.png")
background_img=canvas.create_image(400,263,image=front_img)
canvas.grid(column=0,row=0,columnspan=2)

# buttons
my = PhotoImage(file="images/right.png")
right_button= Button(image=my, highlightthickness=0, command=known)
right_button.grid(column=1,row=1)

my_image = PhotoImage(file="images/wrong.png")
wrong_button= Button(image=my_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0,row=1)
#text on card
title=canvas.create_text(400,150,text="title",font=("Ariel",40,"italic"))
word=canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
next_card()

win.mainloop()
