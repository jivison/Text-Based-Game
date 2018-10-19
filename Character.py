#My own library of useful functions

import Functions as f

import Loot_Pool as lp

#This object holds all of the information for the player

class Character(object):

  #This is the basic info for the player

  has_visited_shop = False
  inventory = {}
  value_inventory = []
  slot = 0
  removed_slot = 0
  item_removed_is_true = False
  player_class = ""
  
  def __init__(self, name, health, attack_power, money, defense, heal):

    #More basic info

    self.max_health = health
    self.heal = heal
    self.name = name
    self.health = health
    self.attack_power = attack_power
    self.money = money
    self.defense = defense

  #Shorthand for adding to the players inventory

  def add_to_inventory(self, item_value):

    f.add_stats(item_value)

    print("{} added to your inventory!".format(lp.loot_pool.item_list[item_value]['name']))

    #This complicated code makes sure that when you remove an item from your inventory, you don't lose that slot forever
    if self.item_removed_is_true == True:
      self.inventory[self.removed_slot] = lp.loot_pool.item_list[item_value]['name']
      self.item_removed_is_true = False 
      self.value_inventory.append(item_value)
      
    else:  
      self.inventory[self.slot] = lp.loot_pool.item_list[item_value]['name']
      self.slot += 1
      self.value_inventory.append(item_value)
  
  def remove_from_inventory(self, slot):

    #This function is shorthand for removing something from inventory

    print(self.inventory[slot], "removed from inventory")
    self.value_inventory.remove(lp.get_value(self.inventory[slot]))
    f.remove_stats(lp.get_value(self.inventory[slot]))
    self.inventory[slot] = "Nothing"  
    self.removed_slot = slot
    self.item_removed_is_true = True
    self.slot += 1
    
  def replace_inventory_item(self, slot, replacing_item_value):
    
    print("{} replaced with {}!".format(self.inventory[slot], lp.loot_pool.item_list[replacing_item_value]['name']))

    #Pretty self-explanitory
    self.value_inventory.remove(lp.get_value(self.inventory[slot]))
    f.remove_stats(lp.get_value(self.inventory[slot]))
    self.value_inventory.append(replacing_item_value)
    self.inventory[slot] = lp.loot_pool.item_list[replacing_item_value]
    f.add_stats(replacing_item_value)


  def take_damage(self, damage_taken):

    #Shorthand for taking damage

    self.health -= damage_taken

  def debuff(self, stat, i):

    #Mostly made for the boss combat, but lowers a stat

    if stat == 'attack_power':
      self.attack_power -= i
    elif stat == 'money':
      self.money -= i
    elif stat == 'defense':
      self.defense -= i 

  def check_items():

    #This function is supposed to be an items system :(

    pass

def initialize_player():

  #This initializes the player and gets the players name

  #Player(name, health, attack, money, defense, heal)
  bools = True
  global player
  print("What class would you like to be?")
  f.bw()
  while bools == True:
    player_class_input = input("'scavenger', 'mage', or 'warrior'? ")
    f.bw()
    if player_class_input == 'scavenger':
      #The scavanger is going to have garbage like weapons
      player = Character(input("What is your villainous name? "), 10, 5, 10, 2, 3)
      bools = False
      #player.add_to_inventory("A Broken Bottle")
      f.bw()
    elif player_class_input == 'mage':
      #The mage class is going to have computer like weapons...
      player = Character(input("What is your wizardly name? "), 12, 4, 10, 5, 4)
      bools = False
      #player.add_to_inventory("UNIX and a laptop")
      f.bw()
    elif player_class_input == 'warrior':
      #The warrior class is going to have everyday items
      player = Character(input("What is your knightly name? "), 15, 5, 10, 1, 2)
      bools = False
      #player.add_to_inventory("A Sharp Spatula")
      f.bw()
    elif player_class_input == 'god mode':
      player = Character('Developer', 99, 99, 99, 99, 99)
      bools = False
    elif player_class_input == 'help':
      f.print_help('class selection')
    elif player_class_input == 'quit':
      quit()
    else:
      print("<--Please enter a valid class-->")
      f.bw()

