########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Item class for my Path of Exile Loot Filter Creator.                 #
#                                                                      #
# Created on 2016-11-27                                                #
#                                                                      #
########################################################################


########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from StringTokenizer import *   # For handling defaults string

########################################################################
#                                                                      #
#                              ITEM CLASS                              #
#                                                                      #
########################################################################

class Item(object):
    defaults = ""
    attributes = {}
    attributeLabels = ("Class", "BaseType", "Rarity", "Quality",         \
                       "ItemLevel", "DropLevel", "Sockets",              \
                       "LinkedSockets", "SocketGroup", "FontSize",       \
                       "TextColour", "BorderColour", "BackgroundColour" ,\
                       "SoundFile" , "SoundLevel")

    # Constructor calls method to set defaults
    def __init__(self, defaults):
        self.defaults = defaults   # Defaults string
        self.attributes = {}
        self.setDefaults()

    # Method sets defaults
    def setDefaults(self):
        # String to tokenize for attribute dictionary
        tokenizer = StringTokenizer(',')
        tokenizer.setString(self.defaults)

        # Create attribute dictionary
        while (not tokenizer.atEnd()):
            for i in range(len(self.attributeLabels)):
                self.attributes[self.attributeLabels[i]] = tokenizer.getToken()

    # Method returns a specific attribute
    # PRE: Valid Dictionary Key
    # POST: Corresponding Dictionary Value
    def getAttribute(self, dictKey):
        return self.attributes[dictKey]

    # Method sets a specific attribute
    def setAttribute(self, dictKey, value):
        self.attributes[dictKey] = value
