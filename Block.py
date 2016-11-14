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
    def __init__(self, title):
        Toplevel.__init__(self)
        self.title(title)
        self.geometry("400x400")

    def createBlock(self, index):
        self.wait_window()

        comment = GeneratedText()
        comment.createComment(headings[index])
            
        return comment.getText()
