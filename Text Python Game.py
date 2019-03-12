# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 11:10:20 2018

@author: yzhan
"""

####
""" 
Story of the game: 
    This is one of the Dungeon in Game World of Warcraft. Lick King
is the King of Death in Icecrown Ciradel Dungeon. Before getting to him, there are 
some rooms in the Icecrown Citadel Dungeon before Lick King. Also, to kill Lick King
you would become Kings-Slayer which is a nice tittle for a lot of people.

"""

###############################################################################
## Part 1: Building up one room at a time (no fail function)
###############################################################################

import time
import random

print ("Welcome to World of Warcraft!")

time.sleep(3)

############### 2. Type your name
player_name =  input("What's your name? >")

print("Your name is {}. Welcome to Icecrown Citadel Dungeon. It's time to be Kings-slayer."
      .format(player_name.upper(), "Death knight"))

time.sleep(3)

###################

def fail():
    print("You've failed, but thanks for playing!")
    input('<Press any key to exit>\n')
    
###################

print ("""You enter a first dark room of Icecrown Ciradel Dungeon. 
       It is dark and you can only make out a blue light sword on the floor.""")
ch1 = str(input("Do you take it? [y/n]: "))

# SWORD TAKEN
if ch1 in ['y', 'Y', 'Yes', 'YES', 'yes']:
    print("You have taken the sword!! Please move to the next room.")
    time.sleep(2)

# SWORD NOT TAKEN
else:
    print("I am super man, I dont need a sword to kill!!!!!") 

###################
# Constructing room_blood and calling it to start the game
###################

def room_blood():
    print("You're in room_blood!\n")
    input('<Press any key to continue>\n')
    

room_blood() # This starts the game



###################
# Adding room_frost and linking it to room_blood
###################

def room_blood():
    print("You're in room_blood!\n")
    input('<Press any key to continue>\n')
    
    room_frost() # This moves us into room_frost



def room_frost():
    print("You're in room_frost!\n")
    input('<Press any key to continue>\n')


room_blood() # Calling the first function in our map will start our game



###################
# Adding room_plague and linking it to room_frost
###################

def room_blood():
    print("You're in room_blood!\n")
    input('<Press any key to continue>\n')
    
    room_frost() # This moves us into room_frost



def room_frost():
    print("You're in room_frost!\n")
    input('<Press any key to continue>\n')
    
    room_plague() # This moves us into room_plague



def room_plague():
    print("You're in room_plague!\n")
    input('<Press any key to exit>\n')

room_blood() # Calling the first function in our map will start our game



###############################################################################
## Part 2: Adding in a fail function and ways to fail
###############################################################################

def room_blood():
    print("You're in room_blood!\n")
    input('<Press any key to continue>\n')
    
    print("Press 1 to go to room_frost.")
    print("Press 2 to fail.")
    
    choice = input("> ")
    
    if choice == '1':
        room_frost() # This moves us into room_frost

    elif choice == '2':
        fail() # This moves us into fail
    
    else:
        print("Invalid entry. Please try again.\n")
        room_blood() # Brings us back to the beginning of room_blood to try again
    


def room_frost():
    print("You're in room_frost!\n")
    input('<Press any key to continue>\n')
    
    print("Press 1 to go to room_plague.")
    print("Press 2 to fail.")
    
    choice = input("> ")
    
    if choice == '1':
        room_plague() # This moves us into room_frost

    elif choice == '2':
        fail() # This moves us into fail
    
    else:
        print("Invalid entry. Please try again.\n")
        input('<Press any key to continue>\n')
        
        room_frost() # Brings us back to the beginning of room_blood to try again



def room_plague():
    print("You're in room_plague!\n")
    input('<Press any key to exit>\n')



def fail():
    print("You've failed, but thanks for playing!")
    input('<Press any key to exit>\n')


room_blood() # EVERYTHING goes before this clause


###############################################################################
## Part 3: Adding more functionality to the game
###############################################################################

def room_blood():
    print("You're in room_blood!\n")
    input('<Press any key to continue>\n')
    
    print("Press 1 to go to room_frost.")
    print("Press 2 to fail.")
    
    choice = input("> ")
    
    if choice == '1':
        print("Then you must answer this question.\n")
        
        print( 
"""
The Master of Lick King is just there in frone of you, he is sleeping row. Are you going to kill him?
1) No, I don't have a sword. You are my Master, Lick King!!!!!!!.
2) Yes, Get a shiny blue sword to kill him and I would be the Lick King!!!!!!!.
        
""")
        
        choice = input("> ")
        
        # Start of nested conditional
        if choice == '1':
            print("That's incorrect.")
            
            fail()
 
           
            
        elif choice =='2':
            print("That's correct! Please enjoy room_frost!")
            input('<Press any key to continue>\n')
            
            room_frost()
            
        # End of nested conditional
        
        
    elif choice == '2':
        fail()
    
    else:
        print("Invalid entry. Please try again.\n")
        input('<Press any key to continue>\n')
        room_blood()
    


def room_frost():
    print("You're in room_frost!\n")
    input('<Press any key to continue>\n')
    
    print("Press 1 to go to room_plague.")
    print("Press 2 to fail.")
    
    choice = input("> ")
    
    if choice == '1':
        room_plague()

    elif choice == '2':
        fail()
    
    else:
        print("Invalid entry. Please try again.\n")
        room_2()



def room_plague():
    print("You're in room_plague!\n")
    print("All you have to do to attack the Lick King three times by pressing any key three times.\n")
    
    presses = 3
    
    while presses > 0:
        input('<Press any key>\n')
        presses -= 1
    
    print("Oh, the Lick King is killed by you. You win!!, you are the Kings-Slayer now!!!! GG. You Win!!")



def fail():
    print("You've failed, but thanks for playing!")
    input('<Press any key to exit>\n')


room_blood()


