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
GEOMETRY = "800x800"               # GUI screen size.

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
        fileMenu.add_command(label = "New", \
                             command = self.createFilter)
        fileMenu.add_separator()
        fileMenu.add_command(label = "Export", \
                             command = self.exportFilter)
        fileMenu.add_separator()
        fileMenu.add_command(label = "Exit", command = parent.destroy)

        # Create GUI Frames
        self.leftFrame    = Frame(parent)
        self.rightFrame   = Frame(parent)
        self.previewFrame = Frame(self.rightFrame)
        self.notesFrame   = Frame(self.rightFrame)

        # Create Left GUI Widgets
        self.checkButtonsArray = []
        for i in range(0, len(headings)):
            self.checkButtonsArray.append(Checkbutton(self.leftFrame, \
                                          text = headings[i], \
                                          state = DISABLED))

        # Create Right GUI Widgets
        self.previewLabel = Label(self.rightFrame, \
                                  text = "Preview:")
        self.scrollbar = Scrollbar(self.previewFrame)
        self.editArea = Text(self.previewFrame, \
                        width = 80,
                        height = 28, \
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
                        height = 19, \
                        wrap = "word", \
                        yscrollcommand = self.scrollbar2.set, \
                        borderwidth = 1)
        self.scrollbar2.config(command = self.notesArea.yview)

        # Place File and start menu
        menubar.add_cascade(label = "File", menu = fileMenu)
        parent.config(menu = menubar)

        # Place GUI Frames
        self.leftFrame.pack(side = LEFT, padx = 5)
        self.rightFrame.pack(side = RIGHT, padx = 5)

        # Place Left GUI Widgets
        for i in range(1, len(headings)):
            self.checkButtonsArray[i].pack(anchor = W)

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

        # Display notes
        self.notesArea.config(state = "normal")
        self.notesArea.insert(END, startComment)
        self.notesArea.config(state = "disabled")

    # Method exports filter
    def exportFilter(self):
        # 1.0 = first line character 0. end-1c = end minus return
        # carriage
        text = self.editArea.get("1.0", 'end-1c')
        writer = FileHandler(FILTER_NAME)
        writer.write(text, "")

    # Method appeneds text to editArea
    def editAreaInsert(self, token):
        self.editArea.config(state = "normal")
        self.editArea.insert(END, token + "\n")
        self.editArea.config(state = "disabled")

    # Method creates filter
    # PRE: dynamic = true or false
    def createFilter(self):
        # Start with a blank preview window
        self.editArea.delete(1.0, END)

        # Uncheck all Class Checkboxes
        for i in range(1, len(headings)):
            self.checkButtonsArray[i].deselect()
        
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
            self.checkButtonsArray[i].select()

            # Show Filter preview
            self.editAreaInsert(headingsArray[i].getText())
            for text in block:
                self.editAreaInsert(text)

        # Fail safe Show
        length = len(headings) - 1
        string = str(length) + "." + headings[length]
        showHeading = GeneratedText()
        showHeading.createHeading(string.upper())
        self.checkButtonsArray[length].select()
        self.editAreaInsert(showHeading.getText())
        self.editAreaInsert("Show")    

#######################################################################
#                                                                     #
#                                DRIVER                               #
#                                                                     #
#######################################################################

# Method closes app without error
def appClose():
    if messagebox.askokcancel("Quit", "Did you mean to hit X?"):
        os._exit(0)

# Define main - app handler
def main():
    # Initialize GUI
    root = Tk()

    # Initialize LootFilterCreator
    creator = LootFilterCreator(root)

    # Protocol to handle app close
    root.protocol("WM_DELETE_WINDOW", appClose)

    # Keep app running
    root.mainloop()

# Start app
main()
