################## WHEN USING back_mkd() OPTION 0 IS ALWAYS THE ONE THAT GOES BACK#########################
################## WHEN USING ref_mkd() OPTION 1 IS ALWAYS THE ONE THAT GOES TO ANOTHER ROOM#########################

######LOOSE ENDS######
#-Room1
#-Room0
#-Room001
#-Room1
#-Room11 
#-Room111


import Functions as f

import Loot_Pool as lp

import Enemy as e 

import Boss as b

import Character as c

import time as t

global player_input

choices = []
    
def sbw():
    t.sleep(2)
    print('')

def mkd(message):
    bool = True
    while bool == True:
        player_input = input(message)
        if player_input == '0' or player_input == '1':
            bool = False
            f.add(player_input)
        elif player_input == 'quit':
            quit()
        elif player_input == 'print i':
            f.bw()
            print(c.player.inventory)
            f.bw()
        elif player_input == 'print stats':
            f.print_stats()
        elif player_input == 'help':
            f.print_help('decision')
        else:
            f.bw()
            print("<--Please enter a valid character--> ")      
            f.bw()

def back_mkd():
    ################## WHEN USING back_mkd() OPTION 0 IS ALWAYS THE ONE THAT GOES BACK#########################
    bool = True
    while bool == True:
        player_input = input(message)
        if player_input == '0': 
            bool = False
            choices.pop()
        elif player_input == '1':
            bool = False
            f.add(player_input)
        elif player_input == 'quit':
            quit()
        elif player_input == 'print i':
            f.bw()
            print(c.player.inventory)
            f.bw()
        elif player_input == 'print stats':
            f.print_stats()
        elif player_input == 'help':
            f.print_help('decision')
        else:
            f.bw()
            print("<--Please enter a valid character--> ")      
            f.bw()

def ref_mkd(message, ref):
    bool = True
    while bool == True:
        player_input = input(message)
        if player_input == '0': 
            bool = False
            f.add(player_input)
        elif player_input == '1':
            bool = False
            choices = []
            for choice in ref:
                choices.append(choice)
        elif player_input == 'quit':
            quit()
        elif player_input == 'print i':
            f.bw()
            print(c.player.inventory)
            f.bw()
        elif player_input == 'print stats':
            f.print_stats()
        elif player_input == 'help':
            f.print_help('decision')
        else:
            f.bw()
            print("<--Please enter a valid character--> ")      
            f.bw()

class Rooms(object):
    def __init__(self):
        pass
    def room0():
        b.create_boss_combat("Literally God", 17, "attack_power", 4)
    def room01():
        pass
    def room00():
        pass
    def room011():
        pass
    def room000():
        pass
    def room0111():
        pass
    def room001():
        pass


def wai():
    string = 'room'
    for i in choices:
        string += i
    getattr(Rooms, string)()

def room():
    #This needs to be changed...
    print("You wake up in a mysterious room. ")
    sbw()
    print("You see a large oak door. Walking through the door reveals a long hallway. Do you go left (0) or right (1)?")
    sbw()
    print("***Oh no! Your first decision!***")
    sbw()
    print("***Which option will you choose?***")
    sbw()
    mkd("<---Type the character in brackets to make a decision---> ")
