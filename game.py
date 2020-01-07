# importing GUI Library and Imgae handling library
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from play2 import *
from play2 import charposition
from play2 import *
# import Main
#creating hangman class
class Hangman:
    def __init__(self, window, level):
        self.window = window
        self.window.title("Hangman")
        self.window.iconbitmap("icon.ico")
        self.window.geometry("1200x600")
        self.res = Image.open("restar.jpg")
        self.res = self.res.resize((50, 50), Image.ANTIALIAS)
        self.res = ImageTk.PhotoImage(self.res)

        self.qui = Image.open("quit.jpg")
        self.qui = self.qui.resize((50, 50), Image.ANTIALIAS)
        self.qui = ImageTk.PhotoImage(self.qui)

        # Quit button
        self.buttonq1 = Button(window, image=self.qui, command=window.quit)
        self.buttonq1.grid(row=4, column=7)
        self.buttonr1 = Button(window, image=self.res) #command=lambda: restart())
        self.buttonr1.grid(row=4, column=6)

        #number of lives
        self.lives = 4
        self.live = 5
        self.pos = 0

        self.label1 = Label(window, text="Lives remaining 5 ")
        self.label1.grid(row=5, column=0)

        # Change images everytime answer is wrong
        self.image_view = ['hang.jpg', 'img4.png', 'img2.jpg', 'img2.jpg', 'img1.png']
        self.img = Image.open(self.image_view[self.lives])
        self.img = self.img.resize((200, 200), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.panel = Label(window, image=self.img)
        self.panel.grid(column=0, row=0)
        self.grid = []
        self.answer_arr = []
        self.answer = None
        self.level = level

        # restart function
    # def restart(self):
    #     self.window.destroy
    #     self.Main.main()
    #set level function(Here we validate the difficulty of the game)
    def setlevel(self):
        if self.level == "EASY":
            self.answer = easy()
        elif self.level == "HARD":
            self.answer = hard()
        elif self.level == "MEDIUM":
            self.answer = medium()
    def log(self, mylog, event):
        with open('mylogs.txt', 'a') as the_file:
            the_file.write(str(mylog) + event +'\n')
    # Validate if selected letter is correct and making it appear if it is.
    def clicked(self, letters):
        global lives
        global live
        global pos
        self.log(letters, " (is the letter selected)") #log letter input
        print(letters)
        if letters in self.answer:
            postions = charposition(self.answer, letters)
            for char in postions:
                self.grid[char]["text"] = letters
                self.pos += 1

            pass
        # Change image when answer is wrong
        else:
            self.live -= 1
            self.wrtn = "Lives remaining " + str(self.live)
            self.label1.configure(text=self.wrtn)
            self.image = Image.open(self.image_view[self.lives])
            self.image = self.image.resize((200, 200), Image.ANTIALIAS)
            self.imgn = ImageTk.PhotoImage(self.image)
            self.panel.configure(image=self.imgn)
            self.panel.image = self.imgn
            self.lives -= 1
            self.log(self.live, " (lives left)")  # log lives left
            if self.live <= 0:
                messagebox.showinfo("Game Over!", "You Hung the man")
                self.window.destroy()
        # Message display if you win game
        if self.pos == len(self.answer):
            messagebox.showinfo("You Won", "not all heroes \n Wear capes")

        print(self.live)
        #dynamically create the grid for the answer depending on the number of letters in the word
    def answer_grid(self, word):
        column = 2
        for i in word:
            button = Button(self.window, text=" ", bg="white", fg="Black", width=3, height=1, font=('sans', '25'))
            button.grid(column=column, row=0)
            self.grid.append(button)
            column += 1
        #Dynamically creae a keyboard with  all the letters
    def generate_keyboard(self):
        # Alphabet
        keyboard = "QWERTYUIOPMNBVCXZASDFGHJKL"
        col = 1
        row = 1
        for i in keyboard:
            if col == 8:
                col = 1
                row += 1
            cmd = lambda key=i: self.clicked(key)
            button = Button(self.window, text=i, bg="Blue", fg="Black", width=3, height=1, font=('sans', '25'), command=cmd)
            button.grid(column=col, row=row)
            col += 1
        pass

    def play(self):
        self.setlevel()
        print(self.answer)
        self.answer_grid(self.answer)
        self.generate_keyboard()
        self.log(self.answer, " (Is the generated answer)") #log answer input

