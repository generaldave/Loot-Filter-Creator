########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Loot Filter Creator for Path of Exile                                #
#                                                                      #
# Created on 2016-11-13                                                #
#                                                                      #
########################################################################


########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from tkinter       import *            # For GUI
from tkinter       import messagebox   # For messagebox
from MenuBar       import *            # For File Menu
from MainLeft      import *            # For leftFrame
from MainRight     import *            # For rightFrame
from GeneratedText import *            # Loot filter description,
                                       #      headings, etc
from Variables     import *            # Variables file
from FileHandler   import *            # Save Loot Filter
from Block         import *            # Loot filter blocks
import os                              # Used for clean exiting of app

#######################################################################
#                                                                     #
#                              CONSTANTS                              #
#                                                                     #
#######################################################################

TITLE    = "Loot Filter Creator"   # GUI Title.
GEOMETRY = "800x850"               # GUI screen size.

#######################################################################
#                                                                     #
#                              GUI CLASS                              #
#                                                                     #
#######################################################################

class LootFilterCreator(object):
    def __init__(self, parent):
        # GUI Attributes
        self.parent = parent
        self.parent.title(TITLE)
        self.parent.geometry(GEOMETRY)
        image = PhotoImage(file = ICON_PATH)   # Icon
        self.parent.tk.call('wm', 'iconphoto', self.parent._w, image)

        # Create GUI Frames
        self.parent.fileMenu = MenuBar(self, self.parent)
        self.leftFrame       = MainLeft(self.parent)
        self.rightFrame      = MainRight(self.parent)

        # Display notes
        self.rightFrame.notesAreaInsert(startComment)

    # Method exports filter
    def exportFilter(self):
        # 1.0 = first line character 0. end-1c = end minus return
        # carriage
        text = self.rightFrame.editArea.get("1.0", 'end-1c')
        fileObj = FileHandler(FILTER_NAME)
        fileObj.write(text, "")

    # Method creates filter
    # PRE: dynamic = true or false
    def createFilter(self):
        # Start with a blank preview window
        self.rightFrame.clearEditArea()

        # Uncheck all Class Checkboxes
        self.leftFrame.deselectButtons()
        
        # Array of Heading objects
        headingsArray = []
        headingsArray.append(None)

        # Loot filter description
        description = GeneratedText()
        description.createDescription()
        description.insertDescription(headings)
        description.endDescription()

        # Insert description in editArea
        self.rightFrame.editAreaInsert(description.getText())

        # Insert headings and rules in editArea
        for i in range(1, len(headings) - 1):
            # Heading string
            string = str(i) + "." + headings[i]

            # Store Heading object
            text = GeneratedText()
            text.createHeading(string.upper())
            headingsArray.append(text)

            # Create Blocks
            popup = Block(headings[i], i)
            popup.wait_window()   # Pause until complete
            block = popup.getText()

            # Check appropriate box, showing class completion
            self.leftFrame.selectButton(i)

            # Show Filter preview
            self.rightFrame.editAreaInsert(headingsArray[i].getText())
            for text in block:
                self.rightFrame.editAreaInsert(text)

        # Fail safe Show
        length = len(headings) - 1
        string = str(length) + "." + headings[length]
        showHeading = GeneratedText()
        showHeading.createHeading(string.upper())
        self.leftFrame.selectButton(length)
        self.rightFrame.editAreaInsert(showHeading.getText())
        self.rightFrame.editAreaInsert("Show")

    # Method closes app without error
    def appClose(self):
        result = messagebox.askyesno("Quit", \
                                     "Are you sure you want to quit?")
        if result == True:
            os._exit(0)

#######################################################################
#                                                                     #
#                                DRIVER                               #
#                                                                     #
#######################################################################

# Define main - app handler
def main():
    # Initialize GUI
    root = Tk()

    # Initialize LootFilterCreator
    creator = LootFilterCreator(root)

    # Protocol to handle app close
    root.protocol("WM_DELETE_WINDOW", creator.appClose)

    # Keep app running
    root.mainloop()

# Start app
main()
