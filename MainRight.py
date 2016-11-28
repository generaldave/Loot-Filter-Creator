########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# MainRight Class for Path of Exile                                    #
#                                                                      #
# Created on 2016-11-27                                                #
#                                                                      #
########################################################################


########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from tkinter   import *   # For GUI
from Variables import *   # Variables file

#######################################################################
#                                                                     #
#                           MAINRIGHT CLASS                           #
#                                                                     #
#######################################################################

class MainRight(object):
    # Set up GUI
    def __init__(self, parent):
        self.parent = parent

        # Create rightFrame
        self.rightFrame   = Frame(self.parent)
        self.previewFrame = Frame(self.rightFrame)
        self.notesFrame   = Frame(self.rightFrame)

        # Create Right GUI Widgets
        self.previewLabel = Label(self.rightFrame, \
                                  text = "Preview:")
        self.scrollbar = Scrollbar(self.previewFrame)
        self.editArea = Text(self.previewFrame, \
                        width = 80,
                        height = 29, \
                        wrap = "word", \
                        yscrollcommand = self.scrollbar.set, \
                        borderwidth = 1)
        self.scrollbar.config(command = self.editArea.yview)
        self.emptySpace = Button(self.rightFrame, \
                                 state = "disabled", \
                                 borderwidth = 0)
        self.notesLabel = Label(self.rightFrame, \
                                text = "Notes:")
        self.scrollbar2 = Scrollbar(self.notesFrame)
        self.notesArea = Text(self.notesFrame, \
                        width = 80,
                        height = 20, \
                        wrap = "word", \
                        yscrollcommand = self.scrollbar2.set, \
                        borderwidth = 1)
        self.scrollbar2.config(command = self.notesArea.yview)

        # Place rightFrame
        self.rightFrame.pack(side = RIGHT, padx = 5)

        # Place Right GUI Widgets
        self.previewLabel.pack(side = TOP, anchor = W)
        self.previewFrame.pack(fill = X)
        self.scrollbar.pack(side = RIGHT, fill = Y)
        self.editArea.pack(side = LEFT, fill = BOTH, expand = True)
        self.emptySpace.pack(fill = X)
        self.notesLabel.pack(side = TOP, anchor = W)
        self.notesFrame.pack(fill = X)
        self.scrollbar2.pack(side = RIGHT, fill = Y)
        self.notesArea.pack(side = LEFT, fill = BOTH, expand = True)

    # Method Changes notesArea Text
    def notesAreaInsert(self, value):
        self.notesArea.config(state = "normal")
        self.notesArea.insert(END, value)
        self.notesArea.config(state = "disabled")

    # Method clears editArea Text
    def clearEditArea(self):
        self.editArea.delete(1.0, END)
        
    # Method changes editArea Text
    def editAreaInsert(self, value):
        self.editArea.config(state = "normal")
        self.editArea.insert(END, value + "\n")
        self.editArea.config(state = "disabled")
        
