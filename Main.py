import time
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from game import Hangman

#logs user input
def log(mylog,event):
    with open('mylogs.txt', 'a') as the_file:
        the_file.write(str(mylog) + event +'\n')

# Function for selecting the difficulty of the game
level="HARD"
def select(value):
    global level
    level = value

#initialise the game
def start():
    root.destroy()
    log(level, "Was the level selected")
    window = Tk()
    game = Hangman(window, level)
    game.play()
    window.mainloop()



# Main menu buttons
root = Tk()
root.title("Main menu")
root.iconbitmap("icon.ico")
root.geometry("400x200")
welcome = Label(root, text="Welcome To hangman, Please select the difficulty and click start ")
welcome.pack()

easy1 = Button(root, text="Easy", bg="Blue", fg="Black", width=7, height=1, font=('sans', '15'), command=lambda *args: select("EASY"))
easy1.pack()

medium1 = Button(root, text="Medium", bg="Blue", fg="Black", width=7, height=1, font=('sans', '15') ,command=lambda *args: select("MEDIUM"))
medium1.pack()

hard1 = Button(root, text="Hard", bg="Blue", fg="Black", width=7, height=1, font=('sans', '15'), command=lambda *args: select("HARD"))
hard1.pack()

begin = Button(root, text="Start", bg="Red", fg="Black", width=7, height=1, font=('sans', '15'), command=lambda: start())
begin.pack()

root.mainloop()



