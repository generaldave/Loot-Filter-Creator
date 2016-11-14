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
    def __init__(self, title, dynamic):
        # Set up GUI
        Toplevel.__init__(self)
        self.title(title)
        self.geometry("400x400")

        # Create GUI Frames
        self.leftFrame = Frame(self)
        self.rightFrame = Frame(self)

        # Create Rarity options menu (Left Frame)
        self.var = StringVar()
        self.var.set(rarities[0])
        rarityMenu = OptionMenu(self.leftFrame, self.var, *rarities)

        # Create Text Preview (Right Frame)
        self.previewText = StringVar()
        self.previewText.set("test")
        self.preview = Entry(self.rightFrame, \
                             textvariable = self.previewText)

        # Place GUI Frames
        self.leftFrame.pack(side = LEFT, padx = 5)
        self.rightFrame.pack(side = LEFT, padx = 5)

        # Place Left Frame GUI Widgets
        rarityMenu.pack()

        # Place Right Frame GUI Widgets
        self.preview.pack()

    def createBlock(self, index):
        # Set preview text
        self.previewText.set(headings[index].lstrip())

        # Create comment
        comment = GeneratedText()
        comment.createComment(headings[index])

        # Create Block text
        blockText = comment.getText()        + "\n" + \
                    "Show"                   + "\n" + \
                    "    Class \""                  + \
                    headings[index].lstrip() + "\"" + "\n"

        # Return Block text  
        return blockText
