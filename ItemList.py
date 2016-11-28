########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# ItemList class for my Path of Exile Loot Filter Creator.             #
#                                                                      #
# Created on 2016-11-27                                                #
#                                                                      #
########################################################################


########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from FileHandler     import *   # For handling Items file
from StringTokenizer import *   # For handling Items file
from Item            import *   # Item class for List

########################################################################
#                                                                      #
#                           ITEMLIST CLASS                             #
#                                                                      #
########################################################################

class ItemList(object):
    items = []
    itemCount = 0

    # Constructor calls method to populate array of items
    def __init__(self):
        self.populateList()

    # Populates array of items
    def populateList(self):
        file = FileHandler("Items")
        attributes = file.read()
        tokenizer = StringTokenizer('\n')
        tokenizer.setString(attributes)
        while (not tokenizer.atEnd()):
            self.items.append(Item(tokenizer.getToken()))
            self.itemCount = self.itemCount + 1

    # Accessor returns number of items in list
    def getItemCount(self):
        return self.itemCount

    # Method returns an attribute from given item
    # PRE: Valid item number and dictionary key
    # POST: Corresponding dictionary value
    def getAttribute(self, itemID, dictKey):
        return self.items[itemID].getAttribute(dictKey)

    # Method sets an attribute to a given item
    # PRE: valid item number, dictionary key, and value
    def setAttribute(self, itemID, dictKey, value):
        sefl.items[itemID].setAttribute(dictKey, value)

    # Method calls item's method to reset to defaults
    def setDefaults(self, itemID):
        sefl.items[itemID].setDefaults()
