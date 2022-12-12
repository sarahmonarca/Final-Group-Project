from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox
from tkinter import ttk
from time import strftime
from tkinter import messagebox
import time










    
now = strftime("OH NO, the Riddler captured my son!! Batman can you please catch him and retrieve my son?")

#make image bigger
root=Tk()
root.title("BATMAN VS THE RIDDLER")
canvas= Canvas(root, width = 300, height=300)
canvas.pack()
photo=PhotoImage(file='riddler.gif')
canvas.create_image(0, 0, anchor = NW, image=photo)




tkinter.messagebox.showinfo("RIDDLES", now)

name = tkinter.simpledialog.askstring("??", "DO YOU HAVE WHAT IT TAKES TO TRACK DOWN THE RIDDLER" )

output = " %s Thank you so much. When the riddler took my son he gave me this note to give to you (close the picture to view note)" %name

tkinter.messagebox.showinfo(now, output)

def on_closing():
        
    if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol(on_closing)
root.mainloop()



    


root = Tk()
root.title("Main")
root.geometry("550x400")
global e1
global e2


Label(root, text = " Dear Batman, \n \n \n I see the woman has told you about her son, \n I knew it would get your attention!. \n So heres the deal Batsy, you complete my riddles, and I will set the boy free. \n Sounds pretty fare doesnt it? \n There are seven riddles that progressively will get harder. \n Once you have completed all of them, \n the boy will be set free. We will start off simply \n ARE YOU READY \n \n \n \n FROM ENIGMA AKA RIDDLER").place(x=5, y=5)
root.mainloop()
time.sleep(1)
    
    

# nameb = tkinter.simpledialog.askstring("??", "DO YOU HAVE WHAT IT TAKES TO TRACK DOWN THE RIDDLER" )


root.quit()




noww = strftime("FIRST RIDDLE")


root2=Tk()
root2.title("BATMAN VS THE RIDDLER")
canvas= Canvas(root2, width = 350, height=250)
canvas.pack()
#CAN ADD A DIFFERENT PICTURE BELOW IF WANT
photo=PhotoImage(file='riddler.gif') 
canvas.create_image(0, 0, anchor = NW, image=photo)

tkinter.messagebox.showinfo("RIDDLES", noww)

nameb = tkinter.simpledialog.askstring("??", "Riddle: What time is it when an elephant sits on a fence? Answer: Time to fix the fence!" )

# try creating new root names for each pop up and then closing them for the next one to be created
C = 3
while (C > 0):
    if (nameb != "b"):
        print(C, "more trys")
        C = C - 1
        nameb = tkinter.simpledialog.askstring("??", "Riddle: What time is it when an elephant sits on a fence? Answer: Time to fix the fence!" )
        #DETERMINE WHAT WILL HAPPEN IF C RUNS OUT
    elif(nameb == "b"):
        root2 = Tk()
        root2.title("Main")
        root2.geometry("900x500")
        global e1
        global e2
        Label(root2, text = "Congratulations BATMAN. You have completed my simplest riddle. Time to step it up. You are about to play what I like ot calls the PREASSURE RIDDLE. \n A little hint to help you solve this. Find the right preassure HAHA GOODLUCK BATMAN").place(x=5, y=5)
        C = 0
    

root2.mainloop()
time.sleep(1)

# 
# 

#################PREASSURE SENSOR
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#define the pin that goes to the circuit
pin_to_circuit = 4

def rc_time (pin_to_circuit):
    count = 0

    #Output on the pin for
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)

    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1
    if count < 30:
        print(count)
        quit()
    return count

#Catch when script is interrupted, cleanup correctly
try:
    # Main loop
    while True:
        print(rc_time(pin_to_circuit))
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
##############PREASSURE SENSOR
##############RIDDLE 2
noww = strftime("THIRD RIDDLE")


root2=Tk()
root2.title("BATMAN VS THE RIDDLER")
canvas= Canvas(root2, width = 350, height=250)
canvas.pack()
#CAN ADD A DIFFERENT PICTURE BELOW IF WANT
photo=PhotoImage(file='riddler.gif') 
canvas.create_image(0, 0, anchor = NW, image=photo)

tkinter.messagebox.showinfo("RIDDLES", noww)

namea = tkinter.simpledialog.askstring("??", "Riddle: I can be cracked, I can be made, I can be told, and I can be played. What am I" )

# try creating new root names for each pop up and then closing them for the next one to be created
B = 3
while (B > 0):
    if (namea != "A joke"):
        if(B == 0):
            break
        else:
            print(B, "more trys")
            B = B - 1
            namea = tkinter.simpledialog.askstring("??", "I can be cracked, I can be made, I can be told, and I can be played. What am I ?" )
            #DETERMINE WHAT WILL HAPPEN IF C RUNS OUT
    elif(namea == "A joke"):
        root2 = Tk()
        root2.title("Main")
        root2.geometry("900x500")
        global e1
        global e2
        Label(root2, text = "Congratulations BATMAN. You have completed my simplest riddle. Time to step it up. You are about to play what I like ot calls the PREASSURE RIDDLE. \n A little hint to help you solve this. Find the right preassure HAHA GOODLUCK BATMAN").place(x=5, y=5)
        B = 0
    

root2.mainloop()
time.sleep(1)

##############RIDDLE 2
##############BEEP COLOR
import RPi.GPIO as GPIO
from time import sleep
from random import randint
import pygame

playtime = 1
delay = .5

DEBUG = True

pygame.init()

leds = [6,13,19,21]
switches = [20,16,12,26]

sounds = [pygame.mixer.Sound("one.wav"),
          pygame.mixer.Sound("two.wav"),
          pygame.mixer.Sound("three.wav"),
          pygame.mixer.Sound("four.wav")]

GPIO.setmode(GPIO.BCM)
GPIO.setup(leds,GPIO.OUT)
GPIO.setup(switches, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def all_on():
    for i in leds:
        GPIO.output(leds,True)
       
def all_off():
    for i in leds:
        GPIO.output(leds,False)
       
def lose():
    for i in range(0,4):
        all_on()
        sleep(.5)
        all_off()
        sleep(.5)

seq = []

seq.append(randint(0,3))
seq.append(randint(0,3))

print("Welcome to simon")
print("Try to play the sequence back by pressing the switches.")
print("Press the Ctrl+C to exit...")

print("Press the switches or Ctrl+C to exit")


try:
    while (True):
#         delay = sleep(.5)
#         plau = sleep(1)
        seq.append(randint(0,3))
        print(seq)
        if(DEBUG):
           
           
            if (len(seq) >= 3):
                print()
           
            print("seq={}".format(seq))
            if (len(seq) >= 5):
                 root4 = Tk()
                 root4.title("Main")
                 root4.geometry("550x400")
                 global e1
                 global e2


                 Label(root4, text = " Dear Batman, \n \n \n I see the woman has told you about her son, \n I knew it would get your attention!. \n So heres the deal Batsy, you complete my riddles, and I will set the boy free. \n Sounds pretty fare doesnt it? \n There are seven riddles that progressively will get harder. \n Once you have completed all of them, \n the boy will be set free. We will start off simply \n ARE YOU READY \n \n \n \n FROM ENIGMA AKA RIDDLER").place(x=5, y=5)
                 root4.mainloop()
                 time.sleep(1)
                 print ("Riddle Complete")
                 break
#                  playtime = .2
#                  delay = .1
#             elif (len(seq) >= 7):
#                  playtime = .8
#                  delay = .3
#             elif (len(seq) >= 10):
#                  playtime = .7
#                  delay = .25
#             elif (len(seq) >= 13):
#                  playtime = .6
#                  delay =.15
#              
#                  
        for s in seq:
            if(len(seq) < 15):
                GPIO.output(leds[s], True)
            sounds[s].play()
            sleep(playtime)
            if (len(seq) < 15):
                GPIO.output(leds[s],False)
            sleep(delay)
        switch_count = 0
     
        while(switch_count < len(seq)):
            pressed = False
           
            while(not pressed):
                for i in range(len(switches)):
                    while (GPIO.input(switches[i]) == True):
                        val = i
                        pressed = True
            if (DEBUG):
                print(val),
            GPIO.output(leds[val], True)
            sounds[val].play()
            sleep(1)
            GPIO.output(leds[val] , False)
            sleep(.25)
           
            if(val != seq[switch_count]):
                lose()
                GPIO.cleanup()
                exit(0)
            switch_count += 1
except KeyboardInterrupt:
    GPIO.cleanup()
    '''
        pressed = False
        while (not pressed):
            for i in range(len(switches)):
                while(GPIO.input(switches[i]) == True):
                      val = i
                      pressed = True
        GPIO.output(leds[val], True)
        sounds[val].play()
        sleep(1)
        GPIO.output(leds[val],False)
        sleep(0.25)
        '''
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nBbye")
##############BEEP COLOR
##############RIDDLE 3
noww = strftime("THIRD RIDDLE")


root9=Tk()
root9.title("BATMAN VS THE RIDDLER")
canvas= Canvas(root9, width = 350, height=250)
canvas.pack()
#CAN ADD A DIFFERENT PICTURE BELOW IF WANT
photo=PhotoImage(file='riddler.gif') 
canvas.create_image(0, 0, anchor = NW, image=photo)

tkinter.messagebox.showinfo("RIDDLES", noww)

nameq = tkinter.simpledialog.askstring("??", "Riddle: I can be cracked, I can be made, I can be told, and I can be played. What am I" )

# try creating new root names for each pop up and then closing them for the next one to be created
Z = 3
while (Z > 0):
    if (nameq != "A joke"):
        if(Z == 0):
            break
        else:
            print(Z, "more trys")
            Z = Z - 1
            nameq = tkinter.simpledialog.askstring("??", "I can be cracked, I can be made, I can be told, and I can be played. What am I ?" )
            #DETERMINE WHAT WILL HAPPEN IF C RUNS OUT
    elif(nameq == "A joke"):
        root9 = Tk()
        root9.title("Main")
        root9.geometry("900x500")
        global e1
        global e2
        Label(root9, text = "Congratulations BATMAN. You have completed my simplest riddle. Time to step it up. You are about to play what I like ot calls the PREASSURE RIDDLE. \n A little hint to help you solve this. Find the right preassure HAHA GOODLUCK BATMAN").place(x=5, y=5)
        Z = 0
    

root9.mainloop()
time.sleep(1)

##############RIDDLE 3
##############DISTANCE SENSOR
#RANGE SENSOR CODE

##############DISTANCE SENSOR
##############GUESSING GAME
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
        self.reset_button = Button(master, text="Enter Building", command=self.quit_game, state=DISABLED)
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
        root5.geometry("500x500")
        global e1
        global e2
        root.destroy()

        Label(root5, text = " Dear Batman, \n \n \n I see the woman has told you about her son, \n I knew it would get your attention!. \n So heres the deal Batsy, you complete my riddles, and I will set the boy free. \n Sounds pretty fare doesnt it? \n There are seven riddles that progressively will get harder. \n Once you have completed all of them, \n the boy will be set free. We will start off simply \n ARE YOU READY \n \n \n \n FROM ENIGMA AKA RIDDLER").place(x=5, y=5)
        root5.mainloop()
        time.sleep(1)
        GPIO.cleanup()
        sys.exit()

root = Tk()
my_gui = GuessingGame(root)
root.mainloop()


##############GUESSING GAME
##############ROOM GAME
keys =[]
VERBS = [ "go", "look", "take" ]
QUIT_COMMANDS = [ "exit", "quit", "bye" ]

WIDTH = 800
HEIGHT = 600

class Room:
    def __init__(self, name, image):
        self._name = name
        self._image = image
        self._description = ""
        self._exits = []
        self._exitLocations = []
        self._items = []
        self._itemDescriptions = []
        self._grabbables = []

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
   
    @property
    def image(self):
        return self._image
    @image.setter
    def image(self, value):
        self._image = value

    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, value):
        self._description = value
   
    @property
    def exits(self):
        return self._exits
    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def exitLocations(self):
        return self._exitLocations
    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value
   
    @property
    def items(self):
        return self._items
    @items.setter
    def items(self, value):
        self._items = value

    @property
    def itemDescriptions(self):
        return self._itemDescriptions
    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value
   
    @property
    def grabbables(self):
        return self._grabbables
    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    # adds an exit to the room
    def addExit(self, exit, room):
        self._exits.append(exit)
        self._exitLocations.append(room)

    # adds an item to the room
    def addItem(self, item, desc):
        self._items.append(item)
        self._itemDescriptions.append(desc)

    # adds a grabbable item to the room
    def addGrabbable(self, grabbable):
        self._grabbables.append(grabbable)
       
    def __str__(self):
        s = "{}\n".format(self._name)
        s += "{}\n".format(self._description)
        s += "You see: "
       
        for item in self._items:
            s += item + " "
        s += "\n"
        
        s += "Grabbables: "
        for grabbable in self._grabbables:
            s += grabbable + ""
        s += "\n"
            
        s += "Exits: "
        for exit in self._exits:
            s += exit + " "
           
        return s

################################################################
class Game(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

    def createRooms(self):
        Game.rooms = []
        r1 = Room("Room 1", "gif1.gif")
        r2 = Room("Room 2", "gif2.gif")
        r3 = Room("Room 3", "gif3.gif")
        r4 = Room("Room 4", "gif4.gif")
        r5 = Room("Room 5", "gif5.gif")
        r6 = Room("Room 6","gif6.gif")
        r7 = Room("Room 7","gif7.gif")
        r8 = Room("Room 8","gif8.gif")
        r9 = Room("Room 9","gif9.gif")
        r10 = Room("Room 10","gif10.gif")
        r11 = Room("Room 11","gif11.gif")
        r12 = Room("Room 12","gif12.gif")
        r13 = Room("Room 13","gif13.gif")
        r14 = Room("Room 14","gif14.gif")
        r15 = Room("Room 15","gif15.gif")
        r16 = Room("Room 16","gif16.gif")
        r17 = Room("Room 17","gif17.gif")
        r18 = Room("Room 18","gif18.gif")
        r19 = Room("Room 19","gif19.gif")
        r20 = Room("Room 20","gif20.gif")
        r21 = Room("Room 21","gif21.gif")
        r22 = Room("Room 22","gif22.gif")
        r23 = Room("Room 23","gif23.gif")
        r24 = Room("Room 24","gif24.gif")
        r25 = Room("Room 25","gif25.gif")
        # room 1
        # add exits to room 1
        r1.addExit("east", r2) #move the locations to the room numbers
        r1.addExit("south", r6)
    # add grabbables to room 1
    # add items to room 1
        r1.addItem("chair", "It is made of wicker and no one is sitting on it.")
        r1.addItem("table", "It is made of oak. A golden key rests on it.")
    # add exits to room 2
        r2.addExit("west", r1)
        r2.addExit("east", r3)
    # add items to room 2
        r2.addItem("rug", "It is nice and Indian. It also needs to be vacuumed.")
        r2.addItem("fireplace", "It is full of ashes.")
    # add exits to room 3
        r3.addExit("west", r2)
        r3.addExit("east", r4)

        r3.addExit("south",r8)
    # add grabbables to room 3
        r3.addGrabbable("book")
    # add items to room 3
        r3.addItem("bookshelves", "They are empty. Go figure.")
        r3.addItem("statue", "There is nothing special about it.")
        r3.addItem("desk", "The statue is resting on it. So is a book.")
    # add exits to room 4
        r4.addExit("east", r5)
        r4.addExit("west", r3)
       
         
         
         
         
         
        r4.addExit("south", r9) 
    # add grabbables to room 4
        r4.addGrabbable("6-pack")
        r4.addGrabbable("key1")
        r4.addItem("table", "It is made of oak. A golden key rests on it.")

    # add items to room 4
        r4.addItem("brew_rig", "Gourd is brewing some sort of oatmeal stout on the brew rig. A 6-pack is resting beside it.")
    # set room 1 as the current room at the beginning
        #room 5
        r5.addExit("west", r4) #move the locations to the room numbers
        #room 6
        r6.addExit("north", r1)
        r6.addExit("south", r11)
        r6.addGrabbable("key2")
        r6.addItem("table", "It is made of oak. A golden key rests on it.")

        #room 7
        r7.addExit("east", r8)
        #room 8
        r8.addExit("west", r7)
        r8.addExit("north", r3)
        r8.addGrabbable("key3")
        r8.addItem("table", "It is made of oak. A golden key rests on it.")

        #room 9
        r9.addExit("south", r14)
        r9.addExit("west", r8)

        #room 10
        r10.addExit("south", r15)
        r10.addExit("west", r9)
        r10.addGrabbable("key4")
        r10.addItem("table", "It is made of oak. A golden key rests on it.")

        #room 11
        r11.addExit("north", r6)
        r11.addExit("east", r12)

        #room 12
        r12.addExit("south", r17)
        r12.addExit("east", r13)
        r12.addExit("west", r11)
        r12.addGrabbable("key5")
        r12.addItem("table", "It is made of oak. A golden key rests on it.")

        #room 13
        r13.addExit("south", r18)
        r13.addExit("east", r14)
        r13.addExit("west", r12)

        #room 14
        r14.addExit("south", r19)
        r14.addExit("east", r15)
        r14.addExit("west", r13)

        #room 15
        r15.addExit("south", r20)
        r15.addExit("west", r14)
        r15.addItem("kitchen", "A marble counter with a knife on it")
        r15.addExit("north", r10)

        #room 16
        r16.addExit("east", r17)
        r16.addItem("Fridge","There is a fridge in this room with orange juice in it")
        #room 17
        r17.addExit("west", r16)
        r17.addExit("north", r12)
        r17.addGrabbable("key6")
        r17.addItem("table", "It is made of oak. A golden key rests on it.")

        #room 18
        r18.addExit("south", r23)
        r18.addExit("north", r13)

        #room 19
        r19.addExit("west", r18)
        r19.addExit("north", r14)
        r19.addExit("south", r24)

        #room 20
        r20.addExit("north", r15)
        r20.addGrabbable("key7")
        r20.addItem("table", "It is made of oak. A golden key rests on it.")

        #room 21
        r21.addExit("east", r22)
        #room 22
        r22.addExit("west", r21)
        r22.addExit("north", r17)

        #room 23
        r23.addExit("west", r22)
        r23.addExit("north", r18)

        #room 24
        r24.addExit("east", r25)
        r24.addItem("Mirror","There is a mirror in this room that is shattered with a smudge of dirt on it")
        r24.addExit("north", r19)

        #room 25
        r25.addExit("west", r24)
# set room 1 as the current room at the beginning of the game
        Game.currentRoom = r1
        Game.inventory = []

# sets up the GUI
    def setupGUI(self):
        self.pack(fill=BOTH, expand=1)
        Game.player_input = Entry(self, bg="white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.bind("<Tab>", self.complete)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()

        img = None
        Game.image = Label(self, width=WIDTH // 2, image=img)
        Game.image.image = img
        Game.image.pack(side=LEFT, fill=Y)
        Game.image.pack_propagate(False)

        text_frame = Frame(self, width=WIDTH // 2)
        Game.text = Text(text_frame, bg="lightgray", state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)

    def setRoomImage(self):
        if (Game.currentRoom == None):
            Game.img = PhotoImage(file="skull.gif")
   
        else:
            Game.img = PhotoImage(file=Game.currentRoom.image)
            Game.image.config(image=Game.img)
            Game.image.image = Game.img


    def setStatus(self, status):
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        if (Game.currentRoom == None):
            Game.text.insert(END, "You are dead. The only thing you can do now \nis quit.\n")
        else:
            Game.text.insert(END, "{}\n\n{}\nYou are carrying: {}\n\n".format(status, Game.currentRoom, Game.inventory))
            Game.text.config(state=DISABLED)
        if (Game.currentRoom != None):
            Game.words = VERBS + QUIT_COMMANDS + Game.inventory + Game.currentRoom.exits + Game.currentRoom.items + Game.currentRoom.grabbables

# play the game
    def play(self):
        self.createRooms()
        self.setupGUI()
        self.setRoomImage()
        self.setStatus("WELCOME TO ROOM ADVENTURE!")

# processes the player's input
    def process(self, event):
        action = Game.player_input.get()
        action = action.lower().strip()
       
        if (action in QUIT_COMMANDS):
            exit(0)

        if (Game.currentRoom == None):
            Game.player_input.delete(0, END)
            return

        response = "I don't understand. Try verb noun. Valid verbs\nare {}.". format(", ".join(VERBS))
        words = action.split()

        if (len(words) == 2):
            verb = words[0].strip()
            noun = words[1].strip()
           
            if (verb in VERBS):
                if (verb == "go"):
                    response = "You can't go in that direction."
   
                    if (noun in Game.currentRoom.exits):
                        i = Game.currentRoom.exits.index(noun)
                        response = "You walk {} and enter another room.".format(noun)
                        
                        if (Game.currentRoom.name == 'Room 24') and (noun == 'east'):
                            if (('key1' in Game.inventory) and ('key2' in Game.inventory) and ('key3' in Game.inventory) and ('key4' in Game.inventory) and ('key5' in Game.inventory) and ('key6' in Game.inventory) and ('key7' in Game.inventory)):
                                response = "Winner!"
                                Game.currentRoom = Game.currentRoom.exitLocations[i]
                            else:
                                response = "You are missing some of the required keys"
                        else:
                            Game.currentRoom = Game.currentRoom.exitLocations[i]

                        

                elif (verb == "look"):
                    response = "You don't see that item."
                   
                    if (noun in Game.currentRoom.items):
                        i = Game.currentRoom.items.index(noun)
                        response = Game.currentRoom.itemDescriptions[i]
                elif (verb == "take"):
                    response = "You don't see that item."
                   
                    if (noun in Game.currentRoom.grabbables and noun not in Game.inventory):
                        i = Game.currentRoom.grabbables.index(noun)
                        Game.inventory.append(Game.currentRoom.grabbables[i])
                        response = "You take {}.".format(noun)

            if (len(words) == 2):
                self.setStatus(response)
                self.setRoomImage()
                Game.player_input.delete(0, END)
               
    def complete(self, event):
        words = Game.player_input.get().split()
        if (len(words)):
            last_word = words[-1]
            results = [ x for x in Game.words if x.startswith(last_word) ]
            match = None
        if (len(results) == 1):
            match = results[0]  
        elif (len(results) > 1):
            for i in range(1, len(min(results, key=len)) + 1):
                match = results[0][:i]
                matches = [ x for x in results if x.startswith(match) ]
                if (len(matches) != len(results)):
                    match = match[:-1]
                    break
        if (match):
            Game.player_input.delete(0, END)
            for word in words[:-1]:
                Game.player_input.insert(END, "{} ".format(word))
                Game.player_input.insert(END, "{}{}".format(match, " " if (len(results) == 1) else ""))

window = Tk()
window.title("Room Adventure")
g = Game(window)
g.play()
window.mainloop()
##############ROOM GAME

