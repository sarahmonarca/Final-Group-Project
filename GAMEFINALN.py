# the blueprint for a room
keys=[]
class Room:
# the constructor
    def __init__(self, name):
# rooms have a name, exits (e.g., south), exit
# locations (e.g., to the south is room n), items
# (e.g., table), item descriptions (for each item),
# and grabbables (things that can be taken into
# inventory)
        self.name = name
        self.exits = []
        self.exitLocations = []
        self.items = []
        self.itemDescriptions = []
        self.grabbables = []
# getters and setters for the instance variables
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
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
# the exit is a string (e.g., north)
# the room is an instance of a room
    def addExit(self, exit, room):
# append the exit and room to the appropriate lists
        self._exits.append(exit)
        self._exitLocations.append(room)
# adds an item to the room
# the item is a string (e.g., table)
# the desc is a string that describes the item (e.g., it is
# made of wood)
    def addItem(self, item, desc):
# append the item and exit to the appropriate lists
        self._items.append(item)
        self._itemDescriptions.append(desc)
# adds a grabbable item to the room
# the item is a string (e.g., key)
    def addGrabbable(self, item):
# append the item to the list
        self._grabbables.append(item)
# removes a grabbable item from the room
# the item is a string (e.g., key)
    def delGrabbable(self, item):
# remove the item from the list
        self._grabbables.remove(item)
# returns a string description of the room
    def __str__(self):
# first, the room name
        s = "You are in {}.\n".format(self.name)
# next, the items in the room
        s += "You see: "
        for item in self.items:
            s += item + " "
        s += "\n"
        for grabbables in self.grabbables:
            s += grabbables + " "
        s += "\n"
# next, the exits from the room
        s += "Exits: "
        for exit in self.exits:
            s += exit + " "
        return s
            
# creates the rooms
def createRooms():
# r1 through r4 are the four rooms in the mansion
# currentRoom is the room the player is currently in (which
# can be one of r1 through r4)
# since it needs to be changed in the main part of the
# program, it must be global
    global currentRoom
# create the rooms and give them meaningful names
    r1 = Room("Room 1")
    r2 = Room("Room 2")
    r3 = Room("Room 3")
    r4 = Room("Room 4")
    r5 = Room("Room 5")
    r6 = Room("Room 6")
    r7 = Room("Room 7")
    r8 = Room("Room 8")
    r9 = Room("Room 9")
    r10 = Room("Room 10")
    r11 = Room("Room 11")
    r12 = Room("Room 12")
    r13 = Room("Room 13")
    r14 = Room("Room 14")
    r15 = Room("Room 15")
    r16 = Room("Room 16")
    r17 = Room("Room 17")
    r18 = Room("Room 18")
    r19 = Room("Room 19")
    r20 = Room("Room 20")
    r21 = Room("Room 21")
    r22 = Room("Room 22")
    r23 = Room("Room 23")
    r24 = Room("Room 24")
    r25 = Room("Room 25")


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
    r15.addExit("north", r10)

    #room 16
    r16.addExit("east", r17)
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
    r24.addExit("north", r19)

    #room 25
    r25.addExit("west", r24)

    
# of the game
    currentRoom = r1
    
# START THE GAME!!!
print("READ ALL RULES")
print("COLLECT ALL THE KEYS TO ADVANCE TO ROOM 25 TO WIN!!" + " there are seven keys, each key is called a different name. Key-Key1-Key2 etc. They are placed in order by room")
print("RULES -- move using /go/ and then the direction you want")
print("COLLECT -- using the word /take/ and then the item you would like")
inventory = [] # nothing in inventory...yet
createRooms() # add the rooms to the game
# play forever (well, at least until the player dies or asks to
# quit)
while (True):
# set the status so the player has situational awareness
# the status has room and inventory information
    status = "{}\nYou are carrying: {}\n".format(currentRoom, inventory)
# if the current room is None, then the player is dead
# this only happens if the player goes south when in room 4
    if (currentRoom == None):
        status = "You are dead."
# display the status
    print("=========================================")
    print(status)
# if the current room is None (and the player is dead),
# exit the game
    if (currentRoom == None):
        death()
        break
# prompt for player input
# the game supports a simple language of <verb> <noun>
# valid verbs are go, look, and take
# valid nouns depend on the verb
    action = input("What to do? ")
# set the user's input to lowercase to make it easier to
# compare the verb and noun to known values
    action = action.lower()
# exit the game if the player wants to leave (supports
# quit, exit, and bye)
    if (action == "quit" or action == "exit" or action == "bye"):
        break
# set a default response
    response = "I don't understand. Try verb noun. Valid verbs are go, look, and take"
# split the user input into words (words are separated by
# spaces)
    words = action.split()
    
# the game only understands two word inputs
    if (len(words) == 2):
# isolate the verb and noun
        verb = words[0]
        noun = words[1]
# the verb is: go
        if (verb == "go"):
# set a default response
            response = "Invalid exit."
# check for valid exits in the current room
            for i in range(len(currentRoom.exits)):
# a valid exit is found
                if (noun == currentRoom.exits[i]):
# change the current room to the one
# that is associated with the specified
                    if (currentRoom.name == 'Room 24') and (noun == "east"):
                        if (('key1' in inventory) and ('key2' in inventory) and ('key3' in inventory) and ('key4' in inventory) and ('key5' in inventory) and ('key6' in inventory) and ('key7' in inventory)):
                            response = "WINNER WINNER CHICKEN DINNER!!"
                        else:
                            response = "You are missing some of the required keys"
                    else: 
                        currentRoom = currentRoom.exitLocations[i]
# set the response (success)
                        response = "Room changed."
# no need to check any more exits\

                         
# if (currentRoom [24] = "go east")
#     if (('key1' in inventoy) and ('key2' in inventory) and ('key3' in inventory) and ('key4' in inventory) and ('key5' in inventory) and ('key6' in inventory) and ('key7' in inventory))
#         response = "Room changed"
#     else
#         response = "You are missing some of the required keys"\


#                     if ((noun == currentRoom.exits [i])):                     #put this inside another if
#                     # IF in room 24 and IF want to go to room 25, then do this
#                         if (('key1' in inventoy) and ('key2' in inventory) and ('key3' in inventory) and ('key4' in inventory) and ('key5' in inventory) and ('key6' in inventory) and ('key7' in inventory)):
#                             status = "door open"
#                         else:
#                             status = "door closed"
#                     # leave the break here
                    break
# the verb is: look
        elif (verb == "look"):
# set a default response
            response = "I don't see that item."
# check for valid items in the current room
            for i in range(len(currentRoom.items)):
# a valid item is found
                if (noun == currentRoom.items[i]):
# set the response to the item's
# description
                    response = currentRoom.itemDescriptions[i]
# no need to check any more items
                    break
# the verb is: take
        elif (verb == "take"):
# set a default response
            response = "I don't see that item."
# check for valid grabbable items in the current
# room
            for grabbable in currentRoom.grabbables:
# a valid grabbable item is found
                if (noun == grabbable):
# add the grabbable item to the player's
# inventory
                    inventory.append(grabbable)
# remove the grabbable item from the
# room
                    currentRoom.delGrabbable(grabbable)
# set the response (success)
                    response = "Item grabbed."
# no need to check any more grabbable
# items
                    break
# display the response
    print("\n{}".format(response))
