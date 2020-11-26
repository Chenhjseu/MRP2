import pandas as pd
import numpy as np
from tkinter import *
import load_songs


def get_ratings():
    root = Tk()
    root.title('Pick your favourite songs!')

    # load_songs = load_songs.songs_mysql()
    # sql = ''
    # song_df = load_songs.Read_database()
    # song_list = song_df['SongName']

    song_list = ['THE TWIST', 'SMOOTH', 'MACK THE KNIFE', 'UPTOWN FUNK!', 'HOW DO I LIVE',
         'PARTY ROCK ANTHEM', 'I GOTTA FEELING', 'SHAPE OF YOU', 'PHYSICAL']
    v = []  # save the
    choice = []

    for song in song_list:
        v.append(IntVar(value='0'))
        # print(IntVar())
        b = Checkbutton(root, text=song, variable=v[-1], padx=80, font=('Times', 22))
        b.pack(anchor=W)

    def done_click (event=None):
        for x in v:
            choice.append(x.get())
        root.quit()

    theButton = Button(root, text='Done', command=done_click)
    theButton.pack(pady=20)
    mainloop()
    my_ratings = [x * 3 for x in choice]

    return my_ratings

# pass my_ratings back to rating table
