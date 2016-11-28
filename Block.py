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
from BlockLeft            import *      # For Left Frame
from BlockRight           import *      # For Right Frame
from Variables            import *      # Variables file
from BaseTypes            import *      # BaseTypes file
from GeneratedText        import *      # For comment lines
from Comments             import *      # For comment textbox
from tkinter.colorchooser import *      # For choosing colours

########################################################################
#                                                                      #
#                              BLOCK CLASS                             #
#                                                                      #
########################################################################

class Block(Toplevel):
    def __init__(self, title, index):
        # Variables
        self.index       = index
        self.font        = font.Font(family = "Helvetica",  size = 12)
        self.fontSize    = DEFAULT_FONT
        self.textArray   = []
        self.colorSet    = False

        # Populate soundLevels, 0 - 300
        for i in range(301):
            soundLevels.append(i)

        # Populate levels, 1 - 100
        for i in range(1, 101):
            levels.append(i)

        # Populate qualities, 0 - 20
        for i in range(21):
            qualities.append(i)
        
        # Set up GUI
        Toplevel.__init__(self)
        self.setupGUI(title)

        # Create comment
        self.comment = GeneratedText()
        self.comment.createComment(headings[self.index])

        # Set up defaults
        self.setDefaults()

        # Call method to preview text
        self.editAreaInsert()

    # Method sets up GUI
    def setupGUI(self, title):
        self.title(title)
        self.geometry("632x625")
        self.resizable(0, 0)   # Not-resizable
        image = PhotoImage(file = ICON_PATH)   # Icon
        self.tk.call('wm', 'iconphoto', self._w, image)

        # Create GUI Frames
        self.leftFrame     = BlockLeft(self)
        self.rightFrame    = BlockRight(self)

    # Method returns text
    def getText(self):
        return self.textArray

    # Method sets up defaults
    def setDefaults(self):
        self.fontSize    = DEFAULT_FONT
        self.textColor   = (200, 200, 200)
        self.bgColor     = (0, 0, 0)
        self.borderColor = (0, 0, 0)
        self.text = GeneratedText()
        self.text.setText("")
        self.colorSet = False
        self.rightFrame.setDefaults()
        self.leftFrame.setDefaults()

        # Set preview text
        self.rightFrame.setPreviewText(headings[self.index].lstrip())

        # Set up comments area
        self.rightFrame.clearCommentArea()
        self.rightFrame.insertCommentArea(commentsArray[self.index])

    # Method commits text
    def commitText(self):
        self.textArray.append(self.text.getText())

        # Reset defaults
        self.setDefaults()

        # Call method to preview text
        self.editAreaInsert()

    # Method shows preview code
    def editAreaInsert(self):
        # Cannot have 1 link
        if (self.leftFrame.linkText.get() == "1"):
            self.leftFrame.linkText.set("0")
                  
        # Call method to create Block text
        self.text.createBlockText(self.index, self.leftFrame.rarityText, \
                                  self.fontSize, self.textColor, \
                                  self.borderColor, self.bgColor, \
                                  self.comment.getText(), \
                                  self.leftFrame.showHideText, \
                                  self.leftFrame.soundFileText, \
                                  self.leftFrame.soundLevelText,
                                  self.leftFrame.dropOperatorText, \
                                  self.leftFrame.dropLevelText, \
                                  self.leftFrame.itemOperatorText, \
                                  self.leftFrame.itemLevelText, \
                                  self.leftFrame.qualityText,
                                  self.leftFrame.qualityOperatorText, \
                                  self.leftFrame.countText, \
                                  self.leftFrame.countOperatorText, \
                                  self.leftFrame.linkText, \
                                  self.leftFrame.linkOperatorText, \
                                  self.leftFrame.isRGB, \
                                  self.rightFrame.baseTypeText)
        
        # Show preview
        self.rightFrame.clearEditArea()
        for text in self.textArray:
            self.rightFrame.insertEditArea(text + '\n')            
        self.rightFrame.insertEditArea(self.text.getText())

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

    # Method sets BaseType
    def setBaseType(self, value):
        self.rightFrame.baseTypeText.set(value)
        if (value != "All"):
            self.rightFrame.setPreviewText(value)
        else:
            self.rightFrame.setPreviewText(headings[self.index].lstrip())

        # Call method to preview text
        self.editAreaInsert()

    # Method sets whether to show chromatic or not
    def setRGB(self):
        # Call method to preview text
        self.editAreaInsert()

    # Method set socket link operator
    def setLinkOperator(self, value):
        self.leftFrame.linkOperatorText.set(value)

        # Call method to preview text
        self.editAreaInsert()

    # Method sets socket link count
    def setLink(self, value):
        self.leftFrame.linkText.set(value)

        # Call method to preview text
        self.editAreaInsert()

    # Method set socket count operator
    def setCountOperator(self, value):
        self.leftFrame.countOperatorText.set(value)

        # Call method to preview text
        self.editAreaInsert()

    # Method sets socket count
    def setCount(self, value):
        self.leftFrame.countText.set(value)

        # Call method to preview text
        self.editAreaInsert()

    # Method set quality operator
    def setQualityOperator(self, value):
        self.leftFrame.qualityOperatorText.set(value)

        # Call method to preview text
        self.editAreaInsert()

    # Method sets quality
    def setQuality(self, value):
        self.leftFrame.qualityText.set(str(value))

        # Call method to preview text
        self.editAreaInsert()

    # Method sets drop level
    def setItemLevel(self, value):
        self.leftFrame.itemLevelText.set(str(value))

        # Call method to preview text
        self.editAreaInsert()

    # Method sets drop operator
    def setItemOperator(self, value):
        self.leftFrame.itemOperatorText.set(value)

        # Call method to preview text
        self.editAreaInsert()

    # Method sets drop level
    def setDropLevel(self, value):
        self.leftFrame.dropLevelText.set(str(value))

        # Call method to preview text
        self.editAreaInsert()

    # Method sets drop operator
    def setDropOperator(self, value):
        self.leftFrame.dropOperatorText.set(value)

        # Call method to preview text
        self.editAreaInsert()

    # Method sets sound file
    def setSoundFile(self, value):
        self.leftFrame.soundFileText.set(str(value))

        # Call method to preview text
        self.editAreaInsert()

    # Method set sound level
    def setSoundLevel(self, value):
        self.leftFrame.soundLevelText.set(str(value))

        # Call method to preview text
        self.editAreaInsert()

    # Method sets border colour
    def setBorderColor(self):
        try:
            color = askcolor(parent = self)
            self.rightFrame.preview.config(highlightbackground = color[1])   # hex color
            self.borderColor = color[0]                                      # rgb color
            self.colorSet = True

            # Call method to preview text
            self.editAreaInsert()
        except:
            self.borderColor = (0, 0, 0)

    # Method sets background colour
    def setBGColor(self):
        try:
            color = askcolor(parent = self)
            self.rightFrame.preview.config(bg = color[1])   # hex color
            self.bgColor = color[0]                         # rgb color
            self.colorSet = True

            # Call method to preview text
            self.editAreaInsert()
        except:
            self.bgColor = (0, 0, 0)

    # Method sets text colour
    def setTextColor(self):
        previousColor = self.textColor
        try:
            color = askcolor(parent = self)
            self.rightFrame.preview.config(fg = color[1])   # hex color
            self.textColor = color[0]                       # rgb color
            self.colorSet = True

            # Call method to preview text
            self.editAreaInsert()
        except:
            self.textColor = previousColor

    # Method sets show or hide
    def showHideUpdate(self, value):
        self.leftFrame.showHideText.set(value)

        # Call method to preview text
        self.editAreaInsert()

    # Method updates font size
    def fontSizeUpdate(self, value):
        self.fontSize = value
        self.font.config(size = str(self.decideFontSize(value)))
        self.rightFrame.preview.config(font = self.font)

        # Call method to preview text
        self.editAreaInsert()

    # Method updates rarity selected
    def rarityUpdate(self, value):
        self.leftFrame.rarityText.set(value)
        self.leftFrame.setDefaultColours(value)

        # Call method to preview text
        self.editAreaInsert()

    # Method disables rarity options
    def disableRarity(self):
        self.leftFrame.disableRarity()

    # Method disables quality options
    def disableQuality(self):
        self.leftFrame.disableQuality()

    # Method disables socket options
    def disableSockets(self):
        self.leftFrame.disableSocket()
