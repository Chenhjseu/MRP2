# This is a sample Python script.
import Initialize
from update_rating import *
import load_data
# import prediction
import pandas as pd
import numpy as np
from tkinter import *
import time

if __name__ == '__main__':

    my_db = my_mysql()
    user_df = my_db.Read_database('')

    name_list = user_df['User Name']

    window = Tk()
    window.title("Login")
    window.geometry("350x200")
    lbl = Label(window, text="User Name:")
    lbl.grid(column=0, row=0)
    txt = Entry(window, width=10)
    txt.grid(column=1, row=0)


    def clicked ():
        lbl.configure(text="Successfully Login!")
        window.quit()


    btn = Button(window, text="Enter", command=clicked)
    btn.grid(column=2, row=0)
    window.mainloop()

    user_name = txt.get()

    if user_name not in name_list:
        Initialize.get_ratings()

    while 1:
        emotion_state = get_emotion()

        recommend_song_id = prediction(user_name, emotion_state)

        feedback = get_feedback()

        current_emotion_state = get_emotion()

        update_rating(feedback, current_emotion_state)
