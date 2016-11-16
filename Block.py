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

from tkinter              import *      # For GUI
from tkinter              import font   # For fonts
from Variables            import *      # Variables file
from GeneratedText        import *      # For comment lines
from tkinter.colorchooser import *      # For choosing colours

########################################################################
#                                                                      #
#                              BLOCK CLASS                             #
#                                                                      #
########################################################################

class Block(Toplevel):
    def __init__(self, title, index, dynamic):
        # Variables
        self.index       = index
        self.font        = font.Font(family = "Helvetica",  size = 12)
        self.fontSize    = DEFAULT_FONT
        self.textColor   = (0, 0, 0)
        self.bgColor     = (0, 0, 0)
        self.borderColor = (0, 0, 0)
        self.textArray = []
        self.text = GeneratedText()
        
        # Set up GUI
        Toplevel.__init__(self)
        self.setupGUI(title)

        # Create comment
        self.comment = GeneratedText()
        self.comment.createComment(headings[self.index])

        # Call method to create Block text
        self.text.createBlockText(self.index, self.rarityText, \
                                  self.fontSize, self.textColor, \
                                  self.borderColor, self.bgColor)

        # Call method to preview text
        self.editAreaInsert()

    # Method sets up GUI
    def setupGUI(self, title):
        self.title(title)
        self.geometry("425x400")

        # Create GUI Frames
        self.leftFrame  = Frame(self)
        self.rightFrame = Frame(self)

        # Create Left GUI Widgets
        self.rarityText = StringVar()
        self.rarityText.set(rarities[0])
        self.rarityMenu = OptionMenu(self.leftFrame, \
                          self.rarityText, \
                          *rarities, \
                          command = self.rarityUpdate)
        self.fontSizeText = StringVar()
        self.fontSizeText.set(str(self.fontSize))
        self.fontSizeMenu = OptionMenu(self.leftFrame, \
                                       self.fontSizeText, \
                                       *fontSizes, \
                                       command = self.fontSizeUpdate)
        self.textColorButton = Button(self.leftFrame, \
                                      text = "Text Colour", \
                                      command = self.setTextColor)
        self.bgColorButton = Button(self.leftFrame, \
                                    text = "Background Colour", \
                                    command = self.setBGColor)
        self.borderColorButton = Button(self.leftFrame, \
                                        text = "Border Colour", \
                                        command = self.setBorderColor)
        self.emptySpace = Button(self.leftFrame, \
                                 state = "disabled", \
                                 borderwidth = 0)
        self.emptySpace2 = Button(self.leftFrame, \
                                 state = "disabled", \
                                 borderwidth = 0)
        self.commitButton = Button(self.leftFrame, \
                                   text = "Commit", \
                                   command = self.commitText)
        self.doneButton = Button(self.leftFrame, \
                                 text = "Done", \
                                 command = self.destroy)

        # Create Right GUI Widgets
        self.previewText = StringVar(self)
        self.previewText.set("")
        self.preview = Entry(self.rightFrame, \
                             width = 0, \
                             font = self.font, \
                             justify = "center", \
                             textvariable = self.previewText)

        self.scrollbar = Scrollbar(self.rightFrame)
        self.editArea = Text(self.rightFrame, \
                        width = 39,
                        height = 17, \
                        wrap = "word", \
                        yscrollcommand = self.scrollbar.set, \
                        borderwidth = 1)
        self.scrollbar.config(command = self.editArea.yview)

        # Place GUI Frames
        self.leftFrame.pack(side = LEFT, padx = 5)
        self.rightFrame.pack(side = RIGHT, padx = 5)

        # Place Left Frame GUI Widgets
        self.rarityMenu.pack(fill = X)
        self.fontSizeMenu.pack(fill = X)
        self.textColorButton.pack(fill = X)
        self.borderColorButton.pack(fill = X)
        self.bgColorButton.pack(fill = X)
        self.emptySpace.pack(fill = X)
        self.emptySpace2.pack(fill = X)
        self.commitButton.pack(fill = X)
        self.doneButton.pack(fill = X)

        # Place Right Frame GUI Widgets
        self.preview.pack(side = TOP, anchor = W)
        self.scrollbar.pack(side = RIGHT, fill = Y)
        self.editArea.pack(side = RIGHT, fill = BOTH, expand = True)

        # Set preview text
        self.previewText.set(headings[self.index].lstrip())

    # Method returns text
    def getText(self):
        return self.textArray

    # Method commits text
    def commitText(self):
        self.textArray.append(self.text.getText())

        # Reset defaults
        self.text.setText("")
        self.fontSize    = DEFAULT_FONT
        self.textColor   = (0, 0, 0)
        self.bgColor     = (0, 0, 0)
        self.borderColor = (0, 0, 0)

        self.rarityUpdate(rarities[0])
        self.fontSizeUpdate(DEFAULT_FONT)
        self.fontSizeText.set(str(self.fontSize))
        self.preview.config(fg = "#000000")
        self.preview.config(bg = "#F0F0ED")
        self.preview.config(highlightbackground = "#F0F0ED")

        # Call method to create Block text
        self.text.createBlockText(self.index, self.rarityText, \
                                  self.fontSize, self.textColor, \
                                  self.borderColor, self.bgColor)

        # Call method to preview text
        self.editAreaInsert()

    # Method shows preview code
    def editAreaInsert(self):
        self.editArea.delete(1.0, END)
        for text in self.textArray:
            self.editArea.insert(INSERT, self.comment.getText())
            self.editArea.insert(INSERT, text)
            self.editArea.insert(INSERT, "\n")
        self.editArea.insert(INSERT, self.comment.getText())
        self.editArea.insert(INSERT, self.text.getText())

    # Method decides font size
    def decideFontSize(self, sizeIn):
        if (sizeIn == 18 or sizeIn == 19):
            return 8
        if (sizeIn == 20 or sizeIn == 21 or \
            sizeIn == 22 or sizeIn == 23):
            return 9
        if (sizeIn == 24 or sizeIn ==25 or \
            sizeIn == 26):
            return 10
        if (sizeIn == 27 or sizeIn == 28 or \
            sizeIn == 29):
            return 11
        if (sizeIn == 30 or sizeIn == 31 or \
            sizeIn == 32 or sizeIn == 33):
            return 12
        if (sizeIn == 34 or sizeIn == 35 or \
            sizeIn == 36):
            return 13
        if (sizeIn == 37 or sizeIn == 38 or \
            sizeIn == 39):
            return 14
        if (sizeIn == 40 or sizeIn == 41 or \
            sizeIn == 42 or sizeIn == 43):
            return 15
        if (sizeIn == 44 or sizeIn ==45):
            return 16
        return 0   # This suggests an error

    # Method sets border colour
    def setBorderColor(self):
        color = askcolor()
        self.preview.config(highlightbackground = color[1])   # hex color
        self.borderColor = color[0]                           # rgb color

        # Call method to create Block text
        self.text.createBlockText(self.index, self.rarityText, \
                                  self.fontSize, self.textColor, \
                                  self.borderColor, self.bgColor)

        # Call method to preview text
        self.editAreaInsert()

    # Method sets background colour
    def setBGColor(self):
        color = askcolor()
        self.preview.config(bg = color[1])   # hex color
        self.bgColor = color[0]              # rgb color

        # Call method to create Block text
        self.text.createBlockText(self.index, self.rarityText, \
                                  self.fontSize, self.textColor, \
                                  self.borderColor, self.bgColor)

        # Call method to preview text
        self.editAreaInsert()

    # Method sets text colour
    def setTextColor(self):
        color = askcolor()
        self.preview.config(fg = color[1])   # hex color
        self.textColor = color[0]            # rgb color

        # Call method to create Block text
        self.text.createBlockText(self.index, self.rarityText, \
                                  self.fontSize, self.textColor, \
                                  self.borderColor, self.bgColor)

        # Call method to preview text
        self.editAreaInsert()

    # Method updates font size
    def fontSizeUpdate(self, value):
        self.fontSize = value
        self.font.config(size = str(self.decideFontSize(value)))
        self.preview.config(font = self.font)

        # Call method to create Block text
        self.text.createBlockText(self.index, self.rarityText, \
                                  self.fontSize, self.textColor, \
                                  self.borderColor, self.bgColor)

        # Call method to preview text
        self.editAreaInsert()

    # Method updates rarity selected
    def rarityUpdate(self, value):
        self.rarityText.set(value)

        # Call method to create Block text
        self.text.createBlockText(self.index, self.rarityText, \
                                  self.fontSize, self.textColor, \
                                  self.borderColor, self.bgColor)

        # Call method to preview text
        self.editAreaInsert()


