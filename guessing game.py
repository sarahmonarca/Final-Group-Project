from tkinter import *
import random
import sys
from tkinter import Tk, Label, Button, Entry, StringVar, DISABLED, NORMAL, END, W, E

class GuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Guessing Game")

        self.secret_number = random.randint(1, 50)
        self.guess = None
        self.num_guesses = 0

        self.message = "OH NO, The riddler got away. The only way to find him is to guess what building he went into! Quick, the apartment numbers range from 1-50! "
        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.label = Label(master, textvariable=self.label_text, foreground = "black", background = "white")
        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.guess_button = Button(master, text="Guess", command=self.guess_number)
        self.reset_button = Button(master, text="Next Riddle", command=self.quit_game, state=DISABLED)
        self.label.grid(row=0, column=0, columnspan=2, sticky=W+E)
        self.entry.grid(row=1, column=0, columnspan=2, sticky=W+E)
        self.guess_button.grid(row=2, column=0)
        self.reset_button.grid(row=2, column=1)

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.guess = None
            return True
        try:
            guess = int(new_text)
            if 1 <= guess <= 50:
                self.guess = guess
                return True
            else:
                return False
        except ValueError:
            return False

    def guess_number(self):
        self.num_guesses += 1
        if self.guess is None:
            self.message = "Guess a number from 1 to 50"
        elif self.guess == self.secret_number:
            suffix = '' if self.num_guesses == 1 else 'es'
            self.message = "Congratulations! You guessed the number after %d guess%s." % (self.num_guesses, suffix)
            self.guess_button.configure(state=DISABLED)
            self.reset_button.configure(state=NORMAL)
        elif self.guess < self.secret_number:
            self.message = "Too low! Guess again!"
        else:
            self.message = "Too high! Guess again!"

        self.label_text.set(self.message)
  
    def quit_game(self):
        root5 = Tk()
        root5.title("Main")
        root5.geometry("600x600")
        global e1
        global e2
        root.destroy()
        
        
        Label(root5, text = "Dear Batmann...").place(x= 5, y = 5)
        root5.mainloop()
        time.sleep(1)
        GPIO.cleanup()
        sys.exit()

root = Tk()
my_gui = GuessingGame(root)
root.mainloop()