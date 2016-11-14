########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Block class for my Path of Exile Loot Filter Creator.                #
#                                                                      #
# Created on 2016-11-13                                                #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from tkinter       import *   # For GUI
from Variables     import *   # Variables file
from GeneratedText import *   # For comment lines

########################################################################
#                                                                      #
#                              BLOCK CLASS                             #
#                                                                      #
########################################################################

class Block(Toplevel):
    def __init__(self, title, index, dynamic):
        # Set up GUI
        Toplevel.__init__(self)
        self.title(title)
        self.geometry("400x400")

        self.index= index

        # Create GUI Frames
        self.leftFrame = Frame(self)
        self.rightFrame = Frame(self)

        # Create Rarity options menu (Left Frame)
        self.rarityText = StringVar()
        self.rarityText.set(rarities[0])
        rarityMenu = OptionMenu(self.leftFrame, \
                                self.rarityText, \
                                *rarities, \
                                command = self.rarityUpdate)

        # Create Text Preview (Right Frame)
        self.previewText = StringVar(self)
        self.previewText.set("")
        self.preview = Entry(self.rightFrame, \
                             textvariable = self.previewText)

        # Place GUI Frames
        self.leftFrame.pack(side = LEFT, padx = 5)
        self.rightFrame.pack(side = LEFT, padx = 5)

        # Place Left Frame GUI Widgets
        rarityMenu.pack()

        # Place Right Frame GUI Widgets
        self.preview.pack()

        # Set preview text
        self.previewText.set(headings[index].lstrip())

        # Create comment
        self.comment = GeneratedText()
        self.comment.createComment(headings[index])

        # Call method to create Block text
        self.createBlockText()

    # Method returns text
    def getText(self):
        return self.text

    # Method updates rarity selected
    def rarityUpdate(self, value):
        self.rarityText.set(value)

        # Call method to create Block text
        self.createBlockText()

    # Method creates Block text
    def createBlockText(self):
        self.text = self.comment.getText()        + "\n"  + \
                    "Show"                        + "\n"  + \
                    "    Class \""                        + \
                    headings[self.index].lstrip() + "\""  + "\n" + \
                    "    Rarity " + self.rarityText.get() + "\n"
