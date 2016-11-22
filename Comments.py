########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Comments for Loot Filter Creator for Path of Exile                   #
#                                                                      #
# Created on 2016-11-21                                                #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#                            Generic                                   #
#                                                                      #
########################################################################

startComment = "Checkbuttons on the left of this window are "        + \
               "disabled. They are a progress meter once you "       + \
               "start the wizard.\n\n"                               + \
               "You can start by going to File -> New.\n\n"          + \
               "BaseTypes All\n"                                     + \
               "Rarity All\n"                                        + \
               "Quality >= 0\n"                                      + \
               "ItemLevel >= 1\n"                                    + \
               "DropLevel >= 1\n"                                    + \
               "Sockets >= 0\n"                                      + \
               "LinkedSockets >= 0\n"                                + \
               "Non-Chromatic\n\n"                                   + \
               "Encompasses all items of a given Class.\n\n"         + \
               "All defaults are pre-selected as you go. You "       + \
               "can change them as you see fit.\n\n"                 + \
               "All classes only allow options that apply to them. " + \
               "For example: Quest Items cannot have Rarity, "       + \
               "Quality, or Sockets.\n\n"                            + \
               "Don't forget about things like Chaos and Regal "     + \
               "recipes, Chromatic items, 6 links, and 6 "           + \
               "sockets.\n\n"                                        + \
               "Also, you must hit commit in order to commit a set " + \
               "of rules. And then hit Done once you are done with " + \
               "a given class. The wizard will automatically go on " + \
               "to the next class.\n\n"                              + \
               "Once you are done, go to File -> Export. The "       + \
               "filter will be saved into the folder where all of "  + \
               "wizard's files were executed to, named loot.filter."

########################################################################
#                                                                      #
#                          QUEST ITEMS                                 #
#                                                                      #
########################################################################

questComment = "N/A"

########################################################################
#                                                                      #
#                         LABYRINTH ITEM                               #
#                                                                      #
########################################################################

labyrinthItemComment = "Silver Key\nGolden Key\nTreasure Key"

########################################################################
#                                                                      #
#                        LABYRINTH TRINKET                             #
#                                                                      #
########################################################################

labyrinthTrinketComment = "They will be consumed in the next "       + \
                          "fight against Izaro and provide a buff, " + \
                          "destroy one of his 3 support mechanics, " + \
                          "or minions very fast. To use it, "        + \
                          "simply have it in your inventory when "   + \
                          "entering the arena."

########################################################################
#                                                                      #
#                       LABYRINTH MAP ITEM                             #
#                                                                      #
########################################################################

labyrinthMapItemComment = "Offering to the Goddess"

########################################################################
#                                                                      #
#                          MAP FRAGMETNS                               #
#                                                                      #
########################################################################

mapFragmentsComment = "Sacrifice Set\nMortal Set\nPale Court Keys\n" + \
                      "Shaper's Realm Fragments"

########################################################################
#                                                                      #
#                           LIFE FLASKS                                #
#                                                                      #
########################################################################

lifeFlaskComment = "Possible Uniques:\n\n" + \
                   "Sanctified Life Flask = Blood of the Karui"

########################################################################
#                                                                      #
#                           MANA FLASKS                                #
#                                                                      #
########################################################################

manaFlaskComment = "Possible Uniques:\n\n"                     + \
                   "Greater Mana Flask = Doedre's Elixier\n"   + \
                   "Grand Mana Flask = Zerphi's Last Breath\n" + \
                   "Sanctified Mana Flask = Lavianga's Spirit"

########################################################################
#                                                                      #
#                          HYBRID FLASKS                               #
#                                                                      #
########################################################################

hybridFlaskComment = "Possible Uniques:\n\n"                        + \
                     "Large Hybrid Flask = Divination Distillate\n" + \
                     "Hallowed Hybrid Flask = The Writhing Jar"

########################################################################
#                                                                      #
#                          UTILITY FLASKS                              #
#                                                                      #
########################################################################

utilityFlaskComment = "Possible Uniques:\n\n"                     + \
                      "Ruby Flask = Coruscating Elixir\n"         + \
                      "Ruby Flask = Dying Sun\n"                  + \
                      "Sapphire Flask = Taste of hate\n"          + \
                      "Silver Flask = Kiara's Determination\n"    + \
                      "Quartz Flask = Forbidden Taste\n"          + \
                      "Granite Flask = Lion's Roar\n"             + \
                      "Granite Flask = Rumi's Concoction\n"       + \
                      "Sulphur Flask = The Overflowing Chalice\n" + \
                      "Sulhur Flask = The Sorrow of the Divine\n" + \
                      "Quicksilver Flask = Rotgut\n"              + \
                      "Stibnite Flask = Witchfire Brew\n"         + \
                      "Amethyst Flask = Atziri's Promise\n"       + \
                      "Topaz Flask = Vessel of Vinktar"



########################################################################
#                                                                      #
#                     CRITICAL UTILITY FLASKS                          #
#                                                                      #
########################################################################

criticalUtilityFlaskComment = "N/A"

########################################################################
#                                                                      #
#                         ACTIVE SKILL GEMS                            #
#                                                                      #
########################################################################

activeSkillGemComment = "N/A"

########################################################################
#                                                                      #
#                         SUPPORT SKILL GEMS                           #
#                                                                      #
########################################################################

supportSkillGemComment = "N/A"

########################################################################
#                                                                      #
#                              CURRENCY                                #
#                                                                      #
########################################################################

currencyComment = "N/A"

########################################################################
#                                                                      #
#                           DIVINATION CARDS                           #
#                                                                      #
########################################################################

divinationComment = "FIX ME"

########################################################################
#                                                                      #
#                               JEWELS                                 #
#                                                                      #
########################################################################

jewelComment = "N/A"

########################################################################
#                                                                      #
#                                MAPS                                  #
#                                                                      #
########################################################################

mapComment = "Tier 11-16 (High) = DropLevel >= 78\n"                + \
             "Tier 6-10 (Mid) = DropLevel >= 73\n"                  + \
             "Tier 1-5 (Low) = DropLevel >= 58\n\n"                 + \
             "Guardians are Tier 16. If you are going to apply "    + \
             "separate rules for them, do them before other map rules."

########################################################################
#                                                                      #
#                            FISHING RODS                              #
#                                                                      #
########################################################################

fishingRodComment = "Possible Uniques:\n\n" + \
                    "Reefbane\n"            + \
                    "Song of the Sirens"

########################################################################
#                                                                      #
#                            BODY ARMOURS                              #
#                                                                      #
########################################################################

armourComment = "Possible Uniques:\n\n" + \
                "FIX ME"

########################################################################
#                                                                      #
#                           TWO HAND SWORD                             #
#                                                                      #
########################################################################

twoHandSwordComment = "Possible Uniques:\n\n" + \
                      "FIX ME"

########################################################################
#                                                                      #
#                            TWO HAND AXE                              #
#                                                                      #
########################################################################

twoHandAxeComment = "Possible Uniques:\n\n" + \
                    "FIX ME"

########################################################################
#                                                                      #
#                            TWO HAND MACE                             #
#                                                                      #
########################################################################

twoHandMaceComment = "Possible Uniques:\n\n" + \
                     "FIX ME"

########################################################################
#                                                                      #
#                               BOWS                                   #
#                                                                      #
########################################################################

bowComment = "Possible Uniques:\n\n" + \
             "FIX ME"

########################################################################
#                                                                      #
#                              STAVES                                  #
#                                                                      #
########################################################################

stavesComment = "Possible Uniques:\n\n" + \
                "FIX ME"

########################################################################
#                                                                      #
#                              QUIVERS                                 #
#                                                                      #
########################################################################

quiverComment = "Possible Uniques:\n\n" + \
                "FIX ME"

########################################################################
#                                                                      #
#                               CLAWS                                  #
#                                                                      #
########################################################################

clawComment = "Possible Uniques:\n\n" + \
              "FIX ME"

########################################################################
#                                                                      #
#                              DAGGERS                                 #
#                                                                      #
########################################################################

daggerComment = "Possible Uniques:\n\n" + \
                "FIX ME"

########################################################################
#                                                                      #
#                               WANDS                                  #
#                                                                      #
########################################################################

wandComment = "Possible Uniques:\n\n" + \
              "FIX ME"

########################################################################
#                                                                      #
#                           ONE HAND SWORDS                            #
#                                                                      #
########################################################################

oneHandSwordComment = "Possible Uniques:\n\n" + \
                      "FIX ME"

########################################################################
#                                                                      #
#                      THRUSTING ONE HAND SWORDS                       #
#                                                                      #
########################################################################

thrustingOneHandSwordComment = "Possible Uniques:\n\n" + \
                               "FIX ME"

########################################################################
#                                                                      #
#                           ONE HAND AXES                              #
#                                                                      #
########################################################################

oneHandAxeComment = "Possible Uniques:\n\n" + \
                    "FIX ME"

########################################################################
#                                                                      #
#                           ONE HAND MACES                             #
#                                                                      #
########################################################################

oneHandMaceComment = "Possible Uniques:\n\n" + \
                     "FIX ME"

########################################################################
#                                                                      #
#                              SCEPTRES                                #
#                                                                      #
########################################################################

sceptreComment = "Possible Uniques:\n\n" + \
                 "FIX ME"

########################################################################
#                                                                      #
#                               SHIELDS                                #
#                                                                      #
########################################################################

shieldComment = "Possible Uniques:\n\n" + \
                "FIX ME"

########################################################################
#                                                                      #
#                                GLOVES                                #
#                                                                      #
########################################################################

gloveComment = "Possible Uniques:\n\n" + \
               "FIX ME"

########################################################################
#                                                                      #
#                                BOOTS                                 #
#                                                                      #
########################################################################

bootComment = "Possible Uniques:\n\n" + \
              "FIX ME"

########################################################################
#                                                                      #
#                               HELMETS                                #
#                                                                      #
########################################################################

helmetComment = "Possible Uniques:\n\n" + \
                "FIX ME"

########################################################################
#                                                                      #
#                                BELTS                                 #
#                                                                      #
########################################################################

beltComment = "Possible Uniques:\n\n" + \
              "FIX ME"

########################################################################
#                                                                      #
#                                AMULETS                               #
#                                                                      #
########################################################################

amuletComment = "Possible Uniques:\n\n" + \
                "FIX ME"

########################################################################
#                                                                      #
#                                  RNGS                                #
#                                                                      #
########################################################################

ringComment = "Possible Uniques:\n\n" + \
              "FIX ME"

########################################################################
#                                                                      #
#                            COMMENTS ARRAY                            #
#                                                                      #
########################################################################

commentsArray = []
commentsArray.append("N/A")                          # 0
commentsArray.append(questComment)                   # 1
commentsArray.append(labyrinthItemComment)           # 2
commentsArray.append(labyrinthTrinketComment)        # 3
commentsArray.append(labyrinthMapItemComment)        # 4
commentsArray.append(mapFragmentsComment)            # 5
commentsArray.append(lifeFlaskComment)               # 6
commentsArray.append(manaFlaskComment)               # 7
commentsArray.append(hybridFlaskComment)             # 8
commentsArray.append(utilityFlaskComment)            # 9
commentsArray.append(criticalUtilityFlaskComment)    # 10
commentsArray.append(activeSkillGemComment)          # 11
commentsArray.append(supportSkillGemComment)         # 12
commentsArray.append(currencyComment)                # 13
commentsArray.append(divinationComment)              # 14
commentsArray.append(jewelComment)                   # 15
commentsArray.append(mapComment)                     # 16
commentsArray.append(fishingRodComment)              # 17
commentsArray.append(armourComment)                  # 18
commentsArray.append(twoHandSwordComment)            # 19
commentsArray.append(twoHandAxeComment)              # 20
commentsArray.append(twoHandMaceComment)             # 21
commentsArray.append(bowComment)                     # 22
commentsArray.append(stavesComment)                  # 23
commentsArray.append(quiverComment)                  # 24
commentsArray.append(clawComment)                    # 25
commentsArray.append(daggerComment)                  # 26
commentsArray.append(wandComment)                    # 27
commentsArray.append(oneHandSwordComment)            # 28
commentsArray.append(thrustingOneHandSwordComment)   # 29
commentsArray.append(oneHandAxeComment)              # 30
commentsArray.append(oneHandMaceComment)             # 31
commentsArray.append(sceptreComment)                 # 32
commentsArray.append(shieldComment)                  # 33
commentsArray.append(gloveComment)                   # 34
commentsArray.append(bootComment)                    # 35
commentsArray.append(helmetComment)                  # 36
commentsArray.append(beltComment)                    # 36
commentsArray.append(amuletComment)                  # 38
commentsArray.append(ringComment)                    # 39
