from tkinter import *
from tkinter import filedialog
from pytube import YouTube

import shutil


# Functions

def select_path():
    # allows user to select path from explorer
    path = filedialog.askdirectory()
    path_label.configure(text=path)


def download_movie():
    # get user path
    get_link = link_field.get()
    # get selected path
    user_path = path_label.cget("text")
    screen.title('Pobieranie...')
    # download video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()

    # move to selected directory
    shutil.move(mp4_video, user_path)
    screen.title('Pobieranie ukończone')


screen = Tk()
title = screen.title("YouTube Downloader")
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

# link field
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Podaj link do filmu:", font=('Arial', 15))

# select path for saving the file
path_label = Label(
    screen, text="Wybierz ścieżkę gdzie pobrać film:", font=('Arial', 15))
select_path_btn = Button(screen, text="Wybierz", command=select_path)

# add field to window
canvas.create_window(250, 160, window=path_label)
canvas.create_window(250, 210, window=select_path_btn)

# add field to window
canvas.create_window(250, 50, window=link_label)
canvas.create_window(250, 100, window=link_field)


# download button
download_btn = Button(screen, text="Pobierz film", command=download_movie)

# add field to window
canvas.create_window(250, 390, window=download_btn)


screen.mainloop()
