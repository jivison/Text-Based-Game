global types

import random as r

import Functions as f

import Long_Print_Jobs as lpj

class Loot_Pool(object):

    item_list = [
        {'value' : 0,  'type' : 'none', 'name' : 'none', 'positiion' : 'n/a', 'description' : 'You should not have seen this...'},
        {'value' : 1,  'type' : 'attack', 'name' : "that plastic toy packaging", 'position' : 'hand', 'damage' : 3, 'description' : 'This packaging is very sharp, and ironically, is one of the least "Child Safe" things to package something in.'},
        {'value' : 2,  'type' : 'attack', 'name' : "fidget spinner", 'position' : 'hand', 'damage' : -1, 'description' : 'Back in the year of 2017, these brain-cell and soul destroying monstrocities became wildly popular. Today they lie rotting on bottom shelves, to be there for all eternity.'},
        {'value' : 3,  'type' : 'attack', 'name' : "some wacky looking tic-tacs", 'position' : 'hand', 'damage' : 2, 'description' : 'reddit.com/r/wackytictacs'},
        {'value' : 4,  'type' : 'attack', 'name' : "spare change, but in between your knuckles", 'position' : 'hand', 'damage' : 1, 'description' : "Normally, this change couldn't even buy you a coffee, but now it will smite the bad guys!" },
        {'value' : 5,  'type' : 'attack', 'name' : "covfefe", 'position' : 'hand', 'damage' : 1, 'description' : lpj.donald_trump_tweet},
        {'value' : 6,  'type' : 'attack', 'name' : 'sharpened popsicle stick', 'position' : 'hand', 'damage' : 3, 'description' : 'This sharp childrens crafting ingredient is VERY sharp.'},
        {'value' : 7,  'type' : 'attack', 'name' : 'sharp spoon', 'position' : 'hand', 'damage' : 3, 'description'  : "This strange utensil is more dangerous than you might think... Crafted by master crafter Benjamin Styles"},
        {'value' : 8,  'type' : 'attack', 'name' : 'car parts', 'position' : 'hand', 'damage' : 4, 'description' : 'These car parts are weighty and could be used as a weapon...'},
        {'value' : 9,  'type' : 'attack', 'name' : 'standard pipe wrench', 'position' : 'hand', 'damage' : 2, 'description' : "Just your standard pipe wrench!"},
        {'value' : 10, 'type' : 'healng', 'name' : 'some useful bandages', 'position' : "n/a", 'heal' : 1, 'description' : 'Hopefully, these bandages aren\'t used!'},
        {'value' : 11, 'type' : 'defens', 'name' : 'a surprisingly thick piece of cardboard', 'position' : 'hand', 'defense' : 1, 'description' : "This was probably used by a homeless person, but it will still work as a shield."},
        {'value' : 12, 'type' : 'money_', 'name' : 'an old wallet', 'position' : 'n/a', 'money' : 40, 'description' : 'Someone dropped their wallet, and now it\'s yours!'}
    ]

    value_name_dict = {'none' : 0, 'that plastic toy packaging' : 1, 'fidget spinner' : 2, 'some wacky looking tic-tacs' : 3, 'spare change, but in between your knuckles' : 4, 'covfefe' : 5, 'sharpened popsicle stick' : 6, 'sharp spoon' : 7, 'car parts' : 8, 'standard pipe wrench' : 9, 'some useful bandages' : 10, 'a surprisingly thick piece of cardboard' : 11, 'an old wallet' : 12}
    boss_item_list = [
        {'value' : 0, 'name' : 'Katana', 'position' : 'hand', 'damage' : 7, 'description' : 'This awesome sword is handcrafted in Japan and is very dangerous. Its blade is so sharp, just looking at it will cut you!'},
        {'value' : 1, 'name' : 'Spiked Cricket Bat', 'position' : 'hand', 'damage' : 5, 'description' : 'Someone hammered nails into this cricket bat.'}
    ]

    banned_items = []

    def __init__(self):
        pass

loot_pool = Loot_Pool()

def get_boss_loot():
    loot_var = r.randint(0, len(loot_pool.boss_item_list) - 1)
    loot = loot_pool.boss_item_list[loot_var]
    print_item(loot_var)
    loot_pool.boss_item_list = loot_pool.boss_item_list.pop(loot_var)
    return loot

def shop_get_loot():
    some_bool = True
    global loot_var
    while some_bool == True:            
        loot_var = r.randint(1, len(loot_pool.item_list) - 1)
        if loot_var not in loot_pool.banned_items:
            some_bool = False
            loot_pool.banned_items.append(loot_var)
            loot = loot_pool.item_list[loot_var]['value']
            return loot         
    
def get_loot():
    loot_var = r.randint(1, len(loot_pool.item_list) - 1)
    loot = loot_pool.item_list[loot_var]['value']
    print("It seems that this enemy was guarding something.")
    f.bw()
    print("You find a:")
    f.bw()
    print_item(loot)
    return loot 

def check_type(item_value):
    if loot_pool.item_list[item_value]['type'] == 'attack':
        return 'damage'
    elif loot_pool.item_list[item_value]['type'] == 'defens':
        return 'defense'
    elif loot_pool.item_list[item_value]['type'] == 'healng':
        return 'heal'
    elif loot_pool.item_list[item_value]['type'] == 'money_':
        return 'money'

def print_item(item_value):
    print("Item no. {}, {}. It gives {} {}. \"{}\"".format(loot_pool.item_list[item_value]['value'], loot_pool.item_list[item_value]['name'], loot_pool.item_list[item_value][check_type(item_value)], check_type(item_value), loot_pool.item_list[item_value]['description']))
    f.bw()

def get_value(item_name):
    value = loot_pool.value_name_dict[item_name]
    return value
