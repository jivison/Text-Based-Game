import time

def bw():
    print("")
    time.sleep(1)

import os

import Rooms as r

import Enemy as e

import Character as c

import Loot_Pool as lp

import Long_Print_Jobs as lpj

import random

global player_input

world_name = ''



def test():
    print("test")

def print_game_over():
    bw()
    os.system('cls')
    print(" ▄▀▀▀▀▄    ▄▀▀█▄   ▄▀▀▄ ▄▀▄  ▄▀▀█▄▄▄▄      ▄▀▀▀▀▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄ ")
    time.sleep(0.5)
    print("█         ▐ ▄▀ ▀▄ █  █ ▀  █ ▐  ▄▀   ▐     █      █ █   █    █ ▐  ▄▀   ▐ █   █   █ ")
    time.sleep(0.5)
    print("█    ▀▄▄    █▄▄▄█ ▐  █    █   █▄▄▄▄▄      █      █ ▐  █    █    █▄▄▄▄▄  ▐  █▀▀█▀  ")
    time.sleep(0.5)
    print("█     █ █  ▄▀   █   █    █    █    ▌      ▀▄    ▄▀    █   ▄▀    █    ▌   ▄▀    █  ")
    time.sleep(0.5)
    print("▐▀▄▄▄▄▀ ▐ █   ▄▀  ▄▀   ▄▀    ▄▀▄▄▄▄         ▀▀▀▀       ▀▄▀     ▄▀▄▄▄▄   █     █   ")
    time.sleep(0.5)
    print("▐         ▐   ▐   █    █     █    ▐                            █    ▐   ▐     ▐   ")
    time.sleep(0.5)
    print("                  ▐    ▐     ▐                                 ▐                  ")
    quit()

def add(player_input):
    r.choices.append(player_input)

def print_stats():
    bw()
    print("Your attack power is {}, your health is {}, your defense is {}, your heal is {}, your money is {}, and you have made {} decisions so far...".format(c.player.attack_power, c.player.health, c.player.defense, c.player.heal, c.player.money, len(r.choices)))
    bw()

def asr():
    shop_bool = True
    while (shop_bool == True):
        if shop_input == "0" or shop_input == "1" or shop_input == "2":
            shop_buy_item()
            shop_bool = False
        elif shop_input == "exit":
            print("You choose to exit the shop")
            #Exit shop
            shop_bool = False
        elif shop_input == 'quit':
            quit()
        else:
            shop_input = input("<--Please type a valid character or 'exit' to exit--> ")

def create_combat(name, health, damage1, damage2):
    enemy = e.Enemy(name, health, damage1, damage2)
    damage_var = -1
    print("Oh, no! You have encountered a " + enemy.name + "!")
    bw()
    while enemy.has_died == False:

        #This boolean is used as a value to keep the while loop running

        combat_bool = True

        #This boolean stores whether the player has defended

        has_defended = False

        while combat_bool == True:
            print("You have " + str(c.player.health) + " health, " + str(c.player.attack_power) + " damage, and " + str(c.player.defense) + " defense." )
            bw()
            combat_input = input("Type 'attack' to attack, 'item' to use item, 'defend' to defend, or 'run' to try to flee... ")
            bw()
            if combat_input == 'attack' or combat_input == 'defend' or combat_input == 'run' or combat_input == 'quit' or combat_input == 'do nothing' or combat_input == 'kys':
                combat_bool = False
            elif combat_input == 'item':
                print("This feature is not in the game yet...")
                bw()
            elif combat_input == 'help':
                print_help('combat')
                bw() 
            else: 
                combat_input = input("<--Please enter a valid move--> ")
                bw()
        if combat_input == 'attack':
            enemy.take_damage(c.player.attack_power)
        elif combat_input == 'do nothing':
            pass
        elif combat_input == 'kys':
            c.player.take_damage(10)
        elif combat_input == 'item':
            #this is too complicated for now...
            pass 
        elif combat_input == 'defend':
            c.player.health += c.player.defense
            has_defended = True
            print("You defend for " + str(c.player.defense) + "!")
            bw()
        elif combat_input == 'run':
            #run
            pass
        elif combat_input == 'quit':
            quit()

        if enemy.has_died == False:
            enemy.deal_damage()
        
        if c.player.health <= 0:
            print_game_over()
            quit

        #This is used when the player defends. It makes sure that the player cannot gain health from defending

        if has_defended == True:
            if damage_var == 0:
                c.player.health -= c.player.defense - enemy.damage1
            else:
               c.player.health -= c.player.defense - enemy.damage2

    if c.player.health < c.player.max_health and (c.player.max_health - c.player.health) > (c.player.heal - 1):
        c.player.health += c.player.heal
        print("You heal for " + str(c.player.heal) + ".")

def start_menu():
    os.system('cls')
    lpj.titlescreen()
    bw()
    start_input = input("Enter anything to start and enter 'quit' to quit... ")
    if start_input == 'quit':
        quit()
    elif start_input == 'anything':
        easter_egg_discovered = True
        bw()
        print("You've discovered an easter egg...")
        bw()
    elif start_input == 'help':
        print_help('start menu')
    else: 
        bw()
    lpj.controls()
    print("At any point, you can type in 'help' for a list of available commands.\n")
    print("When making a decision, you can type in 'print stats' to see your stats or 'print i' to see your inventory.\n")
    print("When in a shop, you can type 'print stats' to see the stats of an item, you will be prompted about which you would like to see.\n")
    print("You can also type 'print i' to see your inventory.\n")
    print("Other than that, follow directions and you'll be fine!\n")
    input("Enter anything to continue...\n")


def world_build():
    global world_name
    world_name = input("What is your world called? ")
    bw()
    print("Welcome to", world_name + "!")
    bw()

def do():
    while True:
        r.wai()

def add_stats(item_value):
    types = lp.check_type(item_value)
    if types == 'defense':
        c.player.defense += lp.loot_pool.item_list[item_value]['defense']
    elif types == 'damage':
        c.player.attack_power += lp.loot_pool.item_list[item_value]['damage']
    elif types == 'heal':
        c.player.heal += lp.loot_pool.item_list[item_value]['heal']
    elif types == 'money':
        c.player.money += lp.loot_pool.item_list[item_value]['money']


def remove_stats(item_value):
    types = lp.check_type(item_value)
    if types == 'defense':
        c.player.defense -= lp.loot_pool.item_list[item_value]['defense']
    elif types == 'damage':
        c.player.attack_power -= lp.loot_pool.item_list[item_value]['damage']
    elif types == 'heal':
        c.player.heal -= lp.loot_pool.item_list[item_value]['heal']

def easy_combat():
    create_combat("Spider", 5, 1, 1)

def print_help(setting):
    print("\n\n")
    print("**   *  ******  **      ******")
    print("**   *  **      **      *    *")
    print("******  *****   **      ******")
    print("**   *  **      **      **")
    print("**   *  ******  ******  **\n")
    if setting == 'shop':
        print("The shop commands are:\n")
        print("'0', '1', or '2' ..................... Selects an item\n")
        print("'print stats'    ..................... Displays the stats of an item (prompt after)\n")
        print("'print i'        ..................... Displays your inventory\n")
        print("'exit'           ..................... Leaves the shop\n")
        print("'quit'           ..................... Quits the game\n")
    elif setting == 'combat':
        print("The combat commands are:\n")
        print("'attack'         ..................... Attacks the enemy\n")
        print("'defend'         ..................... Blocks damage\n")
        print("'item'           ..................... Doesn't do anything\n")
        print("'run'            ..................... Doesn't do anything\n")
        print("'quit'           ..................... Quits the game\n")
        print("'kys'            ..................... You take 10 damage\n")
    elif setting == 'decision':
        print("The decision commands are:\n")
        print("'0' or '1'       ..................... Makes a decision\n")
        print("'print stats'    ..................... Prints your stats\n")
        print("'print i'        ..................... Prints your inventory\n")
        print("'quit'           ..................... Quits the game\n")
    elif setting == 'start menu':
        print("The commands for the start menu are:\n")
        print("'anything'       ..................... Gives you and easter egg\n")
        print("'quit'           ..................... Quits the game\n")
        print("anything else    ..................... Progresses the menu\n")
    elif setting == 'class selection':
        print("The commands for the class selection screen are:\n")
        print("'mage'           ..................... Selects the mage class\n")
        print("'scavenger'      ..................... Selects the scavenger class\n")
        print("'warrior'        ..................... Selects the warrior class\n")
        print("'god mode'       ..................... Selects the developer class\n")
        print("'quit'           ..................... Quits the game\n")
    elif setting == 'loot pickup':
        print("The commands for the loot pickup screen are:\n")
        print("'yes'            ..................... Picks up the item\n")
        print("'no'             ..................... Leaves the item behind\n")
        print("'quit'           ..................... Quits the game\n")
    elif setting == 'shop print stats prompt':
        print("The commands for the print stats prompt in the shop screen are:\n")
        print("'0', '1', or '2' ..................... Prints an item's stats\n")
        print("'exit'           ..................... Exits the print stats prompt in the shop screen\n")
        print("'quit'           ..................... Quits the game\n")
    
    input("Enter anything to continue...\n")

