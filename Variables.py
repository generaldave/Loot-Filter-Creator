########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Variables for Loot Filter Creator for Path of Exile                  #
#                                                                      #
# Created on 2016-11-14                                                #
#                                                                      #
########################################################################

import os
from tkinter import *

# Name for exported loot filter
FILTER_NAME = "loot.filter"

# Default font size in game
DEFAULT_FONT = 32

# Path to icon
ICON_PATH = os.getcwd() + "/images/icon.gif"

# Headings = available item classes
headings = []
headings.append(None)                          # 0
headings.append(" Quest Items")                # 1
headings.append(" Labyrinth Item")             # 2
headings.append(" Labyrinth Trinket")          # 3
headings.append(" Labyrinth Map Item")         # 4
headings.append(" Map Fragments")              # 5
headings.append(" Life Flasks")                # 6
headings.append(" Mana Flasks")                # 7
headings.append(" Hybrid Flasks")              # 8
headings.append(" Utility Flasks")             # 9
headings.append("Critical Utility Flasks")     # 10
headings.append("Active Skill Gems")           # 11
headings.append("Support Skill Gems")          # 12
headings.append("Currency")                    # 13
headings.append("Divination Card")             # 14
headings.append("Jewel")                       # 15
headings.append("Maps")                        # 16
headings.append("Fishing Rods")                # 17
headings.append("Body Armours")                # 18
headings.append("Two Hand Swords")             # 19
headings.append("Two Hand Axes")               # 20
headings.append("Two Hand Maces")              # 21
headings.append("Bows")                        # 22
headings.append("Staves")                      # 23
headings.append("Quivers")                     # 24
headings.append("Claws")                       # 25
headings.append("Daggers")                     # 26
headings.append("Wands")                       # 27
headings.append("One Hand Swords")             # 28
headings.append("Thrusting One Hand Swords")   # 29
headings.append("One Hand Axes")               # 30
headings.append("One Hand Maces")              # 31
headings.append("Sceptres")                    # 32
headings.append("Shields")                     # 33
headings.append("Gloves")                      # 34
headings.append("Boots")                       # 35
headings.append("Helmets")                     # 36
headings.append("Belts")                       # 37
headings.append("Amulets")                     # 38
headings.append("Rings")                       # 39
headings.append("Fail Safe Show")              # 40

# Rarity dropdown options
rarities = []
rarities.append("All")
rarities.append("Unique")
rarities.append("Rare")
rarities.append("Magic")
rarities.append("Normal")

# Font size dropdown options
fontSizes = []
fontSizes.append(18)
fontSizes.append(19)
fontSizes.append(20)
fontSizes.append(21)
fontSizes.append(22)
fontSizes.append(23)
fontSizes.append(24)
fontSizes.append(25)
fontSizes.append(26)
fontSizes.append(27)
fontSizes.append(28)
fontSizes.append(29)
fontSizes.append(30)
fontSizes.append(31)
fontSizes.append(32)
fontSizes.append(33)
fontSizes.append(34)
fontSizes.append(35)
fontSizes.append(36)
fontSizes.append(37)
fontSizes.append(38)
fontSizes.append(39)
fontSizes.append(40)
fontSizes.append(41)
fontSizes.append(42)
fontSizes.append(43)
fontSizes.append(44)
fontSizes.append(45)

# Show or Hide dropdown options
showHide = []
showHide.append("Show")
showHide.append("Hide")

# Sound file dropdown options
sounds = []
sounds.append(1)
sounds.append(2)
sounds.append(3)
sounds.append(4)
sounds.append(5)
sounds.append(6)
sounds.append(7)
sounds.append(8)
sounds.append(9)

# Sound level dropdown options
soundLevels = []   # Create dynamically, 0-300

# Operator dropdown options
operators = []
operators.append("<")
operators.append("<=")
operators.append(">")
operators.append(">=")
operators.append("=")

# Levels dropdown options
levels = []   # Create dynamically, 1-100

# Quality dropdown options
qualities = []   # Create dynamically, 0-20

# Socket count dropdown options'
sockets = []
sockets.append(0)
sockets.append(1)
sockets.append(2)
sockets.append(3)
sockets.append(4)
sockets.append(5)
sockets.append(6)

# Array to keep track of what classes cannot have rarity
enableRarity = []
enableRarity.append(1)
enableRarity.append(2)
enableRarity.append(3)
enableRarity.append(4)
enableRarity.append(5)
enableRarity.append(11)
enableRarity.append(12)
enableRarity.append(13)
enableRarity.append(14)

# Array to keep track of what classes cannot have quality
enableQuality = []
enableQuality.append(1)
enableQuality.append(2)
enableQuality.append(3)
enableQuality.append(4)
enableQuality.append(5)
enableQuality.append(13)
enableQuality.append(14)
enableQuality.append(15)

# Array to keep track of what classes cannot have sockets
enableSockets = []
enableSockets.append(1)
enableSockets.append(2)
enableSockets.append(3)
enableSockets.append(4)
enableSockets.append(5)
enableSockets.append(6)
enableSockets.append(7)
enableSockets.append(8)
enableSockets.append(9)
enableSockets.append(10)
enableSockets.append(11)
enableSockets.append(12)
enableSockets.append(13)
enableSockets.append(14)
enableSockets.append(15)
enableSockets.append(16)
enableSockets.append(37)
enableSockets.append(38)
enableSockets.append(39)
