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
        # Variables
        self.index = index
        
        # Set up GUI
        Toplevel.__init__(self)
        self.setupGUI(title)

        # Call method to create Block text
        self.createBlockText()

    # Method sets up GUI
    def setupGUI(self, title):
        self.title(title)
        self.geometry("400x400")

        # Create GUI Frames
        self.leftFrame = Frame(self)
        self.rightFrame = Frame(self)

        # Create Left GUI Widgets
        self.rarityText = StringVar()
        self.rarityText.set(rarities[0])
        self.rarityMenu = OptionMenu(self.leftFrame, \
                          self.rarityText, \
                          *rarities, \
                          command = self.rarityUpdate)

        # Create Right GUI Widgets
        self.previewText = StringVar(self)
        self.previewText.set("")
        self.preview = Entry(self.rightFrame, \
                             width = 39, \
                             font = "Helvetica 20", \
                             justify = "center", \
                             textvariable = self.previewText)

        self.scrollbar = Scrollbar(self.rightFrame)
        self.editArea = Text(self.rightFrame, \
                        width = 39,
                        height = 15, \
                        wrap = "word", \
                        yscrollcommand = self.scrollbar.set, \
                        borderwidth = 1)
        self.scrollbar.config(command = self.editArea.yview)

        # Place GUI Frames
        self.leftFrame.pack(side = LEFT, padx = 5)
        self.rightFrame.pack(side = RIGHT, padx = 5)

        # Place Left Frame GUI Widgets
        self.rarityMenu.pack()

        # Place Right Frame GUI Widgets
        self.preview.pack(side = TOP, anchor = W)
        self.scrollbar.pack(side = RIGHT, fill = Y)
        self.editArea.pack(side = RIGHT, fill = BOTH, expand = True)

        # Set preview text
        self.previewText.set(headings[self.index].lstrip())

        # Create comment
        self.comment = GeneratedText()
        self.comment.createComment(headings[self.index])

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
        self.text = self.comment.getText()        + \
                    "Show"                        + "\n"  + \
                    "    Class \""                        + \
                    headings[self.index].lstrip() + "\""  + "\n"
        if (self.rarityText.get() != "All"):
            self.text = self.text + \
                    "    Rarity " + self.rarityText.get() + "\n"

    # Method appends to Block text
    def appendBlockText(self):
        self.text = self.text + "\n" + \
                    self.comment.getText()        + \
                    "Show"                        + "\n"  + \
                    "    Class \""                        + \
                    headings[self.index].lstrip() + "\""  + "\n"
        if (self.rarityText.get() != "All"):
            self.text = self.text + \
                    "    Rarity " + self.rarityText.get() + "\n"

