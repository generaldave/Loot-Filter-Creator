########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# MainLeft Class for Path of Exile                                     #
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
#                           MAINLEFT CLASS                            #
#                                                                     #
#######################################################################

class MainLeft(object):
    # Set up GUI
    def __init__(self, parent):
        self.parent      = parent

        # Create leftFrame
        self.leftFrame = Frame(self.parent)

        # Create Checkbuttons
        self.checkButtonsArray = []
        for i in range(0, len(headings)):
            self.checkButtonsArray.append(Checkbutton(self.leftFrame, \
                                          text = headings[i], \
                                          state = DISABLED))

        # Place Checkbuttons
        for i in range(1, len(headings)):
            self.checkButtonsArray[i].pack(anchor = W)

        # Place leftFrame
        self.leftFrame.pack(side = LEFT, padx = 5)

    # Method clears all check marks
    def deselectButtons(self):
        for i in range(1, len(headings)):
            self.checkButtonsArray[i].deselect()

    # Method checks appropriate box, given an index
    def selectButton(self, index):
        self.checkButtonsArray[index].select()
        
