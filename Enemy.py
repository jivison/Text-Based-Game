#This library allows me to generate random numbers

import random

#These are my libraries, pretty self-explanatory

import Functions as f

import Character as c

import Loot_Pool as lp

#This object holds all of the methods and information for the enemy

class Enemy(object):
    def __init__(self, name, health, damage1, damage2):
        self.name = name
        self.health = health
        self.damage1 = damage1
        self.damage2 = damage2
        self.has_died = False

    def deal_damage(self):
        if random.randint(1, 10) % 2 == 0:
            c.player.take_damage(self.damage1)
            damage_var = 0
            print("The enemy attacks for " + str(self.damage1) + "!")
            f.bw()
        else:
            c.player.take_damage(self.damage2)
            damage_var = 1
            print("The enemy attacks for " + str(self.damage2) + "!")
            f.bw()

    def die(self):
        self.has_died = True
        print("You have killed the " + self.name + "!")
        f.bw()
        random_var = random.randint(1, 2)
        if random_var == 1:
            loot_input_bool = True
            current_player_loot_value = lp.get_loot()
            current_player_loot = lp.loot_pool.item_list[current_player_loot_value]['name']
            while loot_input_bool == True:
                loot_input = input("Would you like to keep it? <--'yes' or 'no'--> ")
                if loot_input == 'yes':
                    c.player.add_to_inventory(current_player_loot_value)
                    f.bw()
                    print("You take the " + current_player_loot + ".")
                    loot_input_bool = False
                elif loot_input == 'no':
                    f.bw()
                    print("You decide to skip the loot...")
                    loot_input_bool = False
                elif loot_input == 'help':
                    f.print_help('loot pickup')
                elif loot_input == 'quit':
                    quit()
                else:
                    loot_input = input("<--Please type in 'yes' or 'no'--> ")
        else:
            print("No loot this time :(")  

        gold_dropped = random.randint(1, 10)
        f.bw()
        print("You loot " + str(gold_dropped) + " gold from the dead " + self.name + "!")
        f.bw()

    def die_no_loot(self):
        self.has_died = True
        print("You have killed the " + self.name + "!")
        f.bw()
        gold_dropped = random.randint(1, 10)
        f.bw()
        print("You loot " + str(gold_dropped) + " gold from the dead " + self.name + "!")
        f.bw()

    def take_damage(self, damage_taken):
        self.health -= damage_taken
        print("The " + self.name + " took " + str(damage_taken) + " damage!")
        f.bw()
        if self.health <= 0:
            self.die()       

def initialize_enemy():
    global enemy
    enemy = Enemy("null", 0, 0, 0, 0, "null")