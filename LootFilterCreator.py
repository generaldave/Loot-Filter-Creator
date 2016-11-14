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

from tkinter       import *   # For GUI
from GeneratedText import *   # Loot filter description, headings, etc
from Variables     import *   # Variables file
from FileHandler   import *   # Save Loot Filter
from Block         import *   # Loot filter blocks

#######################################################################
#                                                                     #
#                              CONSTANTS                              #
#                                                                     #
#######################################################################

TITLE    = "Loot Filter Creator"   # GUI Title.
GEOMETRY = "800x775"               # GUI screen size.

#######################################################################
#                                                                     #
#                              GUI CLASS                              #
#                                                                     #
#######################################################################

class LootFilterCreator(object):
    def __init__(self, parent):
        # Set up GUI
        self.parent = parent
        self.parent.title(TITLE)
        self.parent.geometry(GEOMETRY)

        # Create File menu
        menubar = Menu(parent)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label = "Export", \
                             command = self.exportFilter)
        fileMenu.add_separator()
        fileMenu.add_command(label = "Exit", command = parent.destroy)

        # Create Start menu
        startMenu = Menu(menubar)
        startMenu.add_command(label = "Dynamic", \
                              command = lambda: self.createFilter(True))
        startMenu.add_command(label = "Not", \
                              command = lambda: self.createFilter(False))

        # Create GUI Frames
        self.leftFrame = Frame(parent)
        self.rightFrame = Frame(parent)

        # Create Left GUI Widgets
        checkButtonsArray = []
        for i in range(0, len(headings)):
            checkButtonsArray.append(Checkbutton(self.leftFrame, \
                                     text = headings[i]))

        # Create Righg GUI Widgets
        self.scrollbar = Scrollbar(self.rightFrame)
        self.editArea = Text(self.rightFrame, \
                        width = 82,
                        height = 51, \
                        wrap = "word", \
                        yscrollcommand = self.scrollbar.set, \
                        borderwidth = 1)
        self.scrollbar.config(command = self.editArea.yview)

        # Place File and start menu
        menubar.add_cascade(label = "File", menu = fileMenu)
        menubar.add_cascade(label = "Start", menu = startMenu)
        parent.config(menu = menubar)

        # Place GUI Frames
        self.leftFrame.pack(side = LEFT, padx = 5)
        self.rightFrame.pack(side = LEFT, padx = 5)

        # Place Left GUI Widgets
        for i in range(1, len(headings)):
            checkButtonsArray[i].pack(anchor = W)

        # Place Right GUI Widgets
        self.scrollbar.pack(side = RIGHT, fill = Y)
        self.editArea.pack(side = LEFT, fill = BOTH, expand = True)

    # Method exports filter
    def exportFilter(self):
        # 1.0 = first line character 0. end-1c = end minus return
        # carriage
        text = self.editArea.get("1.0", 'end-1c')
        writer = FileHandler(FILTER_NAME)
        writer.write(text, "")

    # Method appeneds text to editArea
    def editAreaInsert(self, token):
        self.editArea.insert(INSERT, token + "\n")

    # Method creates filter
    # PRE: dynamic = true or false
    def createFilter(self,dynamic):
        # Array of Heading objects
        headingsArray = []
        headingsArray.append(None)

        # Loot filter description
        description = GeneratedText()
        description.createDescription()
        description.insertDescription(headings)
        description.endDescription()

        # Insert description in editArea
        self.editAreaInsert(description.getText())

        # Insert headings and rules in editArea
        for i in range(1, len(headings)):
            # Heading string
            string = str(i) + "." + headings[i]

            # Store Heading object
            text = GeneratedText()
            text.createHeading(string.upper())
            headingsArray.append(text)

            # Create Blocks
            popup = Block(headings[i], dynamic)
            block = popup.createBlock(i)

            # Show Filter preview
            self.editAreaInsert(headingsArray[i].getText())
            self.editAreaInsert(block)

#######################################################################
#                                                                     #
#                                DRIVER                               #
#                                                                     #
#######################################################################

def main():
    # Initialize GUI
    root = Tk()

    # Initialize LootFilterCreator
    creator = LootFilterCreator(root)

    # Keep app running
    root.mainloop()

# Start app
main()
