##########  ########    ######     ########     
    ##      #      #    #     #    #      #
    ##      #      #    #     #    #      #
    ##      #      #    #     #    #      #
    ##      ########    ######     ########
#-------------------------------------------#
#-----------Primary Features------------------#
#-Write story
#-Re-write the first room to be in theme and to be more extensive
#-Make a bunch of items
#-Fix ref_mkd
#-Bug fixing
#-Fix heal
#-Double check defense

#------Secondary Features (post story writing)--------#
#-Make different classes receive different items, but, make some non-class specific (this might be really complicated?)
#-Clean up my disgusting code... >:( and add comments
#-Create system where player can only wear/carry one item for each body part at a time (eg. Two Hand items, one headwear, one arm...)
#-Factor in clearing the screen (os.system('cls'))
#-Add enemy classes and extra damage
#-Potions and consumables
#-Combat run command
#-Make every while loop have a help screen, there is no stopping manman
#-Implement curses to get that thicc press any key to continue...
#-Balance enemies & bosses

#------------Tertiary Features-----------#
#-Map
#-Create GFX
#-Make it web-based so anyone can play it without Python (this could mean potentially converting it to JS or some other language...)

#-------------Current Features (that are 100% solid)-----------------#
#- Room system
#- Robust combat
#- Random loot system
#- Shops


import Character as c

import Functions as f

import Rooms as r

import Shop as s

#import Loot_Pool as l

#Half of a menu

f.start_menu()

#Apparantly this is bad code, but oh well...

global player_input

#Self-explanitory

c.initialize_player()

#Names the world and welcomes the player

f.world_build()

#Starting dialogue
r.room()

#run-time code
f.do()

