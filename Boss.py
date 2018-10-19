#Allows me to generate random numbers

import math

import random

#My wrtten libraries, pretty self explanatory

import Character as c

import Functions as f

import Enemy as e

import Loot_Pool as lp

#This object stores all of the information for a boss

class Boss(object):
    has_died = False
    debuff_index = 0
    attack_power = 0

    def __init__(self, name, health, debuff, max_attack):
        
        #Stores basic info

        self.name = name
        self.health = health
        self.debuff = debuff

        #This is max attack because the attack is randomized

        self.max_attack = max_attack

    #This function decides what move the boss should make  

    def decide_action(self):
        action_dict = {0 : 'attack1', 1 : 'attack2', 2 : 'special_move'}
        action = action_dict[random.randint(0, len(action_dict) - 1)]
        getattr(self, action)()

    #The first attack, slightly worse than the second one

    def attack1(self):
        self.attack_power = self.max_attack * (random.randint(4, 10)/10)
        print("The {} hit you for {}!".format(self.name, self.attack_power))
        f.bw()
        c.player.take_damage(self.attack_power)

    #The second attack, slightly better than the first one

    def attack2(self):
        self.attack_power = self.max_attack * (random.randint(6, 10)/10)
        print("The {} hit you for {}!".format(self.name, self.attack_power))
        f.bw()
        c.player.take_damage(self.attack_power)

    #Special move, lowers a players attack, defense, or money...

    def special_move(self):

        #This if statement checks if the player has already lost too much of a stat

        if getattr(c.player, self.debuff) > 1:
            c.player.debuff(self.debuff, 1)
            print("The {} lowered your {} by 1!".format(self.name, self.debuff))
            f.bw()
            self.debuff_index += 1
        else:
            f.bw()
            print("This stat cannot be lowered any further!")

    #This function runs when the boss dies; it stops the combat, alerts the player, and gets loot

    def die(self):
        self.has_died = True
        print("You have slain the " + self.name + "!")
        f.bw()
        lp.get_boss_loot()

    #This function makes the boss loose health

    def take_damage(self, amount):
        self.health -= amount
        print("The {} took {} damage!".format(self.name, amount))
        f.bw()

#This function simplfies the process for creating a combat

def create_boss_combat(name, health, debuff, max_attack):

    #This intializes the Boss object with the inputted parameters

    boss = Boss(name, health, debuff, max_attack)
    while boss.has_died == False:

        #This boolean is used as a value to keep the while loop running

        combat_bool = True

        #This bolean stores whether the player has defended

        has_defended = False

        #Displays the players stats

        print("You have " + str(math.ceil(c.player.health)) + " health, " + str(c.player.attack_power) + " damage, and " + str(c.player.defense) + " defense." )
        f.bw()

        #This is the while combat loop that checks if the player inputted a valid response

        combat_input = input("Type 'attack' to attack, 'item' to use item, 'defend' to defend, or 'run' to try to flee... ")
        f.bw()
        while combat_bool == True:
            if combat_input == 'attack' or combat_input == 'defend' or combat_input == 'run' or combat_input == 'quit' or combat_input == 'do nothing' or combat_input == 'kys':
                combat_bool = False
            elif combat_input == 'item':
                print("This feature is not in the game yet...")
                f.bw()
                combat_input = input("<--Please enter a valid move--> ")
            else: 
                combat_input = input("<--Please enter a valid move--> ")
                f.bw()
        if combat_input == 'attack':
            boss.take_damage(c.player.attack_power)
        elif combat_input == 'do nothing':
            pass
        elif combat_input == 'kys':
            c.player.take_damage(10)
        elif combat_input == 'item':
            #this is too complicated for now...
            pass 
        elif combat_input == 'defend':
            pass
            c.player.health += c.player.defense
            has_defended = True
            print("You defend for " + str(c.player.defense) + "!")
            f.bw()
        elif combat_input == 'run':
            #run
            pass
        elif combat_input == 'quit':
            quit()

        #Checks if the boss has died yet

        if boss.health <= 0:
            boss.die()

        #Runs the decide.action function

        if boss.has_died == False:
            boss.decide_action()
        
        #Checks if the player has died

        if c.player.health <= 0:
            print_game_over()
            quit

        #This if statement makes sure the player doesn't gain health by defending

        if has_defended == True:
            c.player.health -= c.player.defense - boss.attack_power

    #This heals the player, but makes sure that they cannot heal more health than their maximum

    if c.player.health < c.player.max_health and (c.player.max_health - c.player.health) > (c.player.heal - 1):
        c.player.health += c.player.heal
        print("You heal for " + str(c.player.heal) + ".")

    #This terrible if statement checks which debuff the boss has and runs that on c.player

    if boss.debuff == 'attack_power':
        c.player.attack_power += boss.debuff_index

    elif boss.debuff == 'defense':
        c.player.defense += boss.debuff_index


