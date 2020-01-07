# importing GUI Library and Imgae handling library
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from play import *
from play import Level

class Game:


    def __init__(self, master, level):
        # Creating main window
        self.master = master
        self.master.title("Hang man")
        self.master.iconbitmap("icon.ico")
        self.master.geometry("1200x600")
        self.res = Image.open("restar.jpg")
        self.res = self.res.resize((50, 50), Image.ANTIALIAS)
        self.res = ImageTk.PhotoImage(self.res)

        self.qui = Image.open("quit.jpg")
        self.qui = self.qui.resize((50, 50), Image.ANTIALIAS)
        self.qui = ImageTk.PhotoImage(self.qui)

        self.lives = 4
        self.live = 5
        self.pos = 0

        # Change images everytime answer is wrong
        self.image_view = ['hang.jpg', 'img4.png', 'img2.jpg', 'img2.jpg', 'img1.png']
        self.img = Image.open(self.image_view[self.lives])
        self.img = self.img.resize((200, 200), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.panel = Label(self.master, image=self.img)
        self.panel.grid(column=0, row=0)
        self.grid = []
        self.answer_arr = []
        self.level = level

        # Input Buttons
        self.button1 = Button(self.master, text="R", bg="Blue", fg="Black", width=3, height=1, font=('sans', '25'),
                              command=lambda: self.clicked("R"))
        self.button1.grid(column=1, row=1)
        self.button2 = Button(self.master, text="A", bg="Blue", fg="Black", width=3, height=1, font=('sans', '25'),
                              command=lambda: self.clicked("A"))
        self.button2.grid(column=2, row=1)
        self.button3 = Button(self.master, text="B", bg="Blue", fg="Black", width=3, height=1, font=('sans', '25'),
                              command=lambda: self.clicked("B"))
        self.button3.grid(column=3, row=1)
        self.button4 = Button(self.master, text="X", bg="Blue", fg="Black", width=3, height=1, font=('sans', '25'),
                              command=lambda: self.clicked("X"))
        self.button4.grid(column=4, row=1)
        self.button5 = Button(self.master, text="T", bg="Blue", fg="Black", width=3, height=1, font=('sans', '25'),
                              command=lambda: self.clicked("T"))
        self.button5.grid(column=5, row=1)
        self.button6 = Button(self.master, text="I", bg="Blue", fg="Black", width=3, height=1, font=('sans', '25'),
                              command=lambda: self.clicked("I"))
        self.button6.grid(column=6, row=1)
        self.button7 = Button(self.master, text="C", bg="Blue", fg="Black", width=3, height=1, font=('sans', '25'),
                              command=lambda: self.clicked("C"))
        self.button7.grid(column=7, row=1)
        self.button8 = Button(self.master, text="Z", bg="Blue", fg="Black", width=3, height=1, font=('sans', '25'),
                              command=lambda: self.clicked("Z"))
        self.button8.grid(column=8, row=1)

        self.button9 = Button(self.master, text="D", bg="Blue", fg="Black", width=3, height=1, font=('sans', '25'),
                              command=lambda: self.clicked("D"))
        self.button9.grid(column=2, row=2)
        self.button10 = Button(self.master, text="Y", bg="Blue", fg="Black", width=3, height=1, font=('sans', '25'),
                               command=lambda: self.clicked("Y"))
        self.button10.grid(column=3, row=2)
        self.button11 = Button(self.master, text="P", bg="Blue", fg="Black", width=3, height=1, font=('sans', '25'),
                               command=lambda: self.clicked("P"))
        self.button11.grid(column=4, row=2)
        self.button12 = Button(self.master, text="N", bg="Blue", fg="Black", width=3, height=1, font=('sans', '25'),
                               command=lambda: self.clicked("N"))
        self.button12.grid(column=5, row=2)
        self.button13 = Button(self.master, text="O", bg="Blue", fg="Black", width=3, height=1, font=('sans', '25'),
                               command=lambda: self.clicked("O"))
        self.button13.grid(column=6, row=2)
        self.button14 = Button(self.master, text="W", bg="Blue", fg="Black", width=3, height=1, font=('sans', '25'),
                               command=lambda: self.clicked("W"))
        self.button14.grid(column=7, row=2)

        self.button15 = Button(self.master, text="U", bg="Blue", fg="Black", width=3, height=1, font=('sans', '25'),
                               command=lambda: self.clicked("U"))
        self.button15.grid(column=3, row=3)
        self.button16 = Button(self.master, text="S", bg="Blue", fg="Black", width=3, height=1, font=('sans', '25'),
                               command=lambda: self.clicked("S"))
        self.button16.grid(column=4, row=3)
        self.button17 = Button(self.master, text="L", bg="Blue", fg="Black", width=3, height=1, font=('sans', '25'),
                               command=lambda: self.clicked("L"))
        self.button17.grid(column=5, row=3)
        self.button18 = Button(self.master, text="V", bg="Blue", fg="Black", width=3, height=1, font=('sans', '25'),
                               command=lambda: self.clicked("V"))
        self.button18.grid(column=6, row=3)

        self.button19 = Button(self.master, text="M", bg="Blue", fg="Black", width=3, height=1, font=('sans', '25'),
                               command=lambda: self.clicked("M"))
        self.button19.grid(column=4, row=4)
        self.button20 = Button(self.master, text="E", bg="Blue", fg="Black", width=3, height=1, font=('sans', '25'),
                               command=lambda: self.clicked("E"))
        self.button20.grid(column=7, row=3)

        self.button21 = Button(self.master, text="G", bg="Blue", fg="Black", width=3, height=1, font=('sans', '25'),
                               command=lambda: self.clicked("G"))
        self.button21.grid(column=3, row=4)
        self.button22 = Button(self.master, text="K", bg="Blue", fg="Black", width=3, height=1, font=('sans', '25'),
                               command=lambda: self.clicked("K"))
        self.button22.grid(column=8, row=2)

        self.button24 = Button(self.master, text="F", bg="Blue", fg="Black", width=3, height=1, font=('sans', '25'),
                               command=lambda: self.clicked("F"))
        self.button24.grid(column=1, row=2)
        self.button25 = Button(self.master, text="H", bg="Blue", fg="Black", width=3, height=1, font=('sans', '25'),
                               command=lambda: self.clicked("H"))
        self.button25.grid(column=2, row=3)
        self.button26 = Button(self.master, text="J", bg="Blue", fg="Black", width=3, height=1, font=('sans', '25'),
                               command=lambda: self.clicked("J"))
        self.button26.grid(column=5, row=4)
        self.button27 = Button(self.master, text="Q", bg="Blue", fg="Black", width=3, height=1, font=('sans', '25'),
                               command=lambda: self.clicked("Q"))
        self.button27.grid(column=6, row=4)

        # Quit button
        self.buttonq1 = Button(self.master, image=self.qui, command=self.master.quit)
        self.buttonq1.grid(row=6, column=9)

        self.label1 = Label(self.master, text="Hanging it in 4 Lives ")
        self.label1.grid(row=5, column=0)

    # Validate if selected letter is correct and making it appear if it is.
    def clicked(self, letters):
        print(letters)
        if letters in self.answer:
            postions = Level.charposition(self.answer, letters)
            for char in postions:
                self.grid[char]["text"] = letters
                self.pos += 1

            pass
        # Change image when answer is wrong
        else:
            wrtn = "Lives remaining " + str(self.live)
            self.label1.configure(text=wrtn)
            self.image = Image.open(self.image_view[self.lives])
            self.image = self.image.resize((200, 200), Image.ANTIALIAS)
            self.imgn = ImageTk.PhotoImage(self.image)
            self.panel.configure(image=self.imgn)
            self.panel.image = self.imgn
            self.lives -= 1
            self.live -= 1
            if self.live <= 0:
                self.messagebox.showinfo("Game Over!", "You Hung the man")
                self.master.destroy()
        # Message display if you win game
        if (self.pos == len(self.answer)):
            messagebox.showinfo("You Won", "not all heroes \n Wear capes")

        print(self.live)

        # Creating self.buttons dynamically
        print(self.answer)

    def answer_grid(self,word):
        column = 2
        for i in word:
            self.button = Button(self.master, text=" ", bg="white", fg="Black", width=3, height=1, font=('sans', '25'))
            self.button.grid(column=column, row=0)
            self.grid.append(self.button)
            column += 1


#     def main():
#     answer_grid(self.level)
#     window = Tk()
#     myhangman = Game(window)
#     window.mainloop()
#
# if __name__ == __main