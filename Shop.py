import Character as c

import Loot_Pool as lp

import Functions as f

import random

class Shop(object):

    banned_items = []

    def __init__(self, value1, price1, value2, price2, value3, price3):
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.item1 = lp.loot_pool.item_list[value1]['name']
        self.item2 = lp.loot_pool.item_list[value2]['name']
        self.item3 = lp.loot_pool.item_list[value3]['name']
        self.price1 = price1
        self.price2 = price2
        self.price3 = price3

    def asr(self):
        bools = True
        while bools == True:
            print(self.item1, ": " + "$" + str(self.price1), "(0) ||", self.item2, ": $" + str(self.price2), "(1) ||", self.item3, ": " + "$" + str(self.price3), "(2)")
            f.bw()
            print("You have $" + str(c.player.money))
            f.bw()
            shop_input = input("<--Type a character, 'exit' to exit or 'print stats' to view stats--> ")
            if shop_input == 'exit':
                bools = False
            if shop_input == 'quit':
                quit()
            elif shop_input == 'print stats':
                abools = True
                while abools == True:
                    f.bw()
                    stats_input = input("Which item number? (0, 1, or 2) (or 'exit' to exit) ")
                    f.bw()
                    if stats_input == '0' or stats_input == '1' or stats_input == '2':
                        abools = False
                        _stats_input = getattr(self, ("value" + str(int(stats_input) + 1)))
                        lp.print_item(_stats_input)
                    elif stats_input == 'exit':
                        abools = False
                    elif stats_input == 'help':
                        f.print_help('shop print stats prompt')
                    elif stats_input == 'quit':
                        quit()
                    else:
                        print("<--Please enter a valid item number-->")
            elif shop_input == '0' or shop_input == '1' or shop_input == '2':
                item_var = ("item" + str(int(shop_input) + 1))
                price_var = ('price' + str(int(shop_input) + 1))
                value_var = ("value" + str(int(shop_input) + 1))
                item = getattr(self, item_var)
                price = getattr(self, price_var)
                value = getattr(self, value_var)
                if shop_input in self.banned_items:
                    f.bw()
                    print("Sorry, this item is sold out.")
                    f.bw()

                elif c.player.money >= price:
                    c.player.money -= price
                    c.player.add_to_inventory(value)
                    f.bw()
                    print("You've bought " + item)
                    f.bw()
                    exec("%s = %r" % (("self." + item_var), "Sold"))
                    exec("%s = %d" % (("self." + price_var), 0))
                    self.banned_items.append(shop_input)
                    lp.loot_pool.item_list.pop(value)

                else: 
                    f.bw()
                    print("You can't afford that!")
                    f.bw()

            elif shop_input == 'print i':
                f.bw()
                print(c.player.inventory)
                f.bw()

            elif shop_input == 'help':
                f.print_help('shop')
            
            else:
                f.bw()
                print("<--Please enter a valid character-->")
                f.bw()
    
    def __call__(self):    
        self.asr()

class Random_Shop(Shop):
    
    banned_items = []
    value1 = lp.shop_get_loot()
    value2 = lp.shop_get_loot()
    value3 = lp.shop_get_loot()
    item1 = lp.loot_pool.item_list[value1]['name']
    item2 = lp.loot_pool.item_list[value2]['name']
    item3 = lp.loot_pool.item_list[value3]['name']
    price1 = random.randint(1, 7)
    price2 = random.randint(1, 7)
    price3 = random.randint(1, 7)

    def __init__(self):
        pass

    def __call__(self):
        self.asr()

def create_shop(value1, price1, value2, price2, value3, price3):
    shop = Shop(value1, price1, value2, price2, value3, price3)
    shop()
    
def create_random_shop():
    shop = Random_Shop()
    shop()
