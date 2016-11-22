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

        # Create GUI Frames
        self.leftFrame     = Frame(self)
        self.rightFrame    = Frame(self)
        self.rarityFrame   = Frame(self.leftFrame)
        self.soundFrame    = Frame(self.leftFrame)
        self.fontFrame     = Frame(self.leftFrame)
        self.dropFrame     = Frame(self.leftFrame)
        self.itemFrame     = Frame(self.leftFrame)
        self.qualityFrame  = Frame(self.leftFrame)
        self.socketFrame   = Frame(self.leftFrame)
        self.countFrame    = Frame(self.socketFrame)
        self.linkFrame     = Frame(self.socketFrame)
        self.baseTypeFrame = Frame(self.rightFrame)
        self.editFrame     = Frame(self.rightFrame)
        self.commentFrame  = Frame(self.rightFrame)

        # Create Left GUI Widgets
        self.showHideText = StringVar()
        self.showHideText.set(showHide[0])
        self.showHideMenu = OptionMenu(self.leftFrame, \
                          self.showHideText, \
                          *showHide, \
                          command = self.showHideUpdate)
        self.emptySpace3 = Button(self.leftFrame, \
                                  state = "disabled", \
                                  borderwidth = 0)
        self.rarityLabel = Label(self.rarityFrame, text = "Rarity:")
        self.rarityText = StringVar()
        self.rarityText.set(rarities[0])
        self.rarityMenu = OptionMenu(self.rarityFrame, \
                          self.rarityText, \
                          *rarities, \
                          command = self.rarityUpdate)
        self.rarityMenu.config(width = 10)
        self.qualityLabel = Label(self.qualityFrame, text = "Quality:")
        self.qualityOperatorText = StringVar()
        self.qualityOperatorText.set(operators[3])
        self.qualityOperatorMenu = OptionMenu(self.qualityFrame, \
                                      self.qualityOperatorText, \
                                      *operators, \
                                      command = self.setQualityOperator)
        self.qualityText = StringVar()
        self.qualityText.set(qualities[0])
        self.qualityMenu = OptionMenu(self.qualityFrame, \
                                     self.qualityText, \
                                     *qualities, \
                                     command = self.setQuality)
        self.itemLevelLabel = Label(self.itemFrame, text = "Item Level:")
        self.itemOperatorText = StringVar()
        self.itemOperatorText.set(operators[3])
        self.itemOperatorMenu = OptionMenu(self.itemFrame, \
                                          self.itemOperatorText, \
                                          *operators, \
                                          command = self.setItemOperator)
        self.itemLevelText = StringVar()
        self.itemLevelText.set(str(levels[0]))
        self.itemLevelMenu = OptionMenu(self.itemFrame, \
                                        self.itemLevelText, \
                                        *levels, \
                                        command = self.setItemLevel)
        self.dropOperatorText = StringVar()
        self.dropOperatorText.set(operators[3])
        self.dropOperatorMenu = OptionMenu(self.dropFrame, \
                                          self.dropOperatorText, \
                                          *operators, \
                                          command = self.setDropOperator)
        self.dropLevelLabel = Label(self.dropFrame, text = "Drop Level:")
        self.dropLevelText = StringVar()
        self.dropLevelText.set(str(levels[0]))
        self.dropLevelMenu = OptionMenu(self.dropFrame, \
                                        self.dropLevelText, \
                                        *levels, \
                                        command = self.setDropLevel)
        self.emptySpace4 = Button(self.leftFrame, \
                                  state = "disabled", \
                                  borderwidth = 0)
        self.socketLabel = Label(self.socketFrame, text = "Sockets:")
        self.countLabel = Label(self.countFrame, text = "Count:")
        self.countOperatorText = StringVar()
        self.countOperatorText.set(operators[3])
        self.countOperatorMenu = OptionMenu(self.countFrame, \
                                            self.countOperatorText, \
                                            *operators, \
                                            command = self.setCountOperator)
        self.countText = StringVar()
        self.countText.set(str(sockets[1]))
        self.countMenu = OptionMenu(self.countFrame, \
                                   self.countText, \
                                   *sockets, \
                                   command = self.setCount)
        self.linkLabel = Label(self.linkFrame, text = "Linked:")
        self.linkOperatorText = StringVar()
        self.linkOperatorText.set(operators[3])
        self.linkOperatorMenu = OptionMenu(self.linkFrame, \
                                            self.linkOperatorText, \
                                            *operators, \
                                            command = self.setLinkOperator)
        self.linkText = StringVar()
        self.linkText.set(str(sockets[0]))
        self.linkMenu = OptionMenu(self.linkFrame, \
                                   self.linkText, \
                                   *sockets, \
                                   command = self.setLink)
        self.isRGB = IntVar()
        self.rgbCheckbutton = Checkbutton(self.socketFrame, \
                                          text = "Chromatic?",
                                          variable = self.isRGB, \
                                          command = self.setRGB)        
        self.emptySpace5 = Button(self.leftFrame, \
                                  state = "disabled", \
                                  borderwidth = 0)
        self.fontLabel = Label(self.fontFrame, text = "Font:")
        self.fontSizeText = StringVar()
        self.fontSizeText.set(str(self.fontSize))
        self.fontSizeMenu = OptionMenu(self.fontFrame, \
                                       self.fontSizeText, \
                                       *fontSizes, \
                                       command = self.fontSizeUpdate)
        self.fontSizeMenu.config(width = 10)
        self.textColorButton = Button(self.leftFrame, \
                                      text = "Text Colour", \
                                      command = self.setTextColor)
        self.borderColorButton = Button(self.leftFrame, \
                                        text = "Border Colour", \
                                        command = self.setBorderColor)
        self.bgColorButton = Button(self.leftFrame, \
                                    text = "Background Colour", \
                                    command = self.setBGColor)
        self.soundLabelText = "Sound File:     Volume:"
        self.soundLabel = Label(self.soundFrame, \
                                text = self.soundLabelText)
        self.soundFileText = StringVar()
        self.soundFileText.set(str(sounds[0]))
        self.soundFile = OptionMenu(self.soundFrame, \
                                     self.soundFileText, \
                                     *sounds, \
                                     command = self.setSoundFile)
        self.soundFile.config(width = 6)
        self.soundLevelText = StringVar()
        self.soundLevelText.set(str(soundLevels[0]))
        self.soundLevel = OptionMenu(self.soundFrame, \
                                     self.soundLevelText, \
                                     *soundLevels, \
                                     command = self.setSoundLevel)
        self.soundLevel.config(width = 6)
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
        self.baseTypeLabel = Label(self.baseTypeFrame, \
                                   text = "Base Types:")
        self.baseTypeArray = self.whichBaseTypes()
        self.baseTypeText = StringVar()
        self.baseTypeText.set(self.baseTypeArray[0])
        self.baseTypeMenu = OptionMenu(self.baseTypeFrame, \
                                       self.baseTypeText, \
                                       *self.baseTypeArray, \
                                       command = self.setBaseType)
        self.baseTypeMenu.config(width = 28)
        self.emptySpace6 = Button(self.rightFrame, \
                                  state = "disabled", \
                                  borderwidth = 0)
        self.previewText = StringVar(self)
        self.previewText.set("")
        self.preview = Entry(self.editFrame, \
                             width = 0, \
                             font = self.font, \
                             justify = "center", \
                             textvariable = self.previewText, \
                             highlightthickness = 2, \
                             relief = FLAT)
        self.scrollbar = Scrollbar(self.editFrame)
        self.editArea = Text(self.editFrame, \
                        width = 57,
                        height = 15, \
                        wrap = "word", \
                        yscrollcommand = self.scrollbar.set, \
                        borderwidth = 1)
        self.scrollbar.config(command = self.editArea.yview)
        self.commentLabelText = StringVar()
        self.commentLabelText.set("Comments:")
        self.commentLabel = Label(self.rightFrame, \
                                  textvariable = self.commentLabelText)
        self.emptySpace7 = Button(self.rightFrame, \
                                  state = "disabled", \
                                  borderwidth = 0)
        self.scrollbar2 = Scrollbar(self.commentFrame)
        self.commentArea = Text(self.commentFrame, \
                           width = 57,
                           height = 15, \
                           wrap = "word", \
                           yscrollcommand = self.scrollbar2.set, \
                           borderwidth = 1)
        self.commentArea.config(state = "disabled")
        self.scrollbar2.config(command = self.editArea.yview)
        
        # Place GUI Frames
        self.leftFrame.pack(side = LEFT, padx = 5)
        self.rightFrame.pack(side = RIGHT, padx = 5)

        # Place Left Frame GUI Widgets
        self.showHideMenu.pack(fill = X)
        self.emptySpace3.pack(fill = X)
        self.rarityFrame.pack(fill = X)
        self.rarityLabel.pack(side = LEFT)
        self.rarityMenu.pack(side = RIGHT)
        self.qualityFrame.pack(fill = X)
        self.qualityLabel.pack(side = LEFT)
        self.qualityMenu.pack(side = RIGHT)
        self.qualityOperatorMenu.pack(side = RIGHT)
        self.itemFrame.pack(fill = X)
        self.itemLevelLabel.pack(side = LEFT)
        self.itemOperatorMenu.pack(side = LEFT)
        self.itemLevelMenu.pack(side = LEFT)
        self.dropFrame.pack(fill = X)
        self.dropLevelLabel.pack(side = LEFT)
        self.dropOperatorMenu.pack(side = LEFT)
        self.dropLevelMenu.pack(side = LEFT)
        self.emptySpace4.pack(fill = X)
        self.socketFrame.pack(fill = X)
        self.socketLabel.pack(fill = X)
        self.countFrame.pack(fill = X)
        self.countLabel.pack(side = LEFT)
        self.countMenu.pack(side = RIGHT)
        self.countOperatorMenu.pack(side = RIGHT)
        self.linkFrame.pack(fill = X)
        self.linkLabel.pack(side = LEFT)
        self.linkMenu.pack(side = RIGHT)
        self.linkOperatorMenu.pack(side = RIGHT)
        self.rgbCheckbutton.pack(side = RIGHT)
        self.emptySpace5.pack(fill = X)
        self.fontFrame.pack(fill = X)
        self.fontLabel.pack(side = LEFT)
        self.fontSizeMenu.pack(side = RIGHT)
        self.textColorButton.pack(fill = X)
        self.borderColorButton.pack(fill = X)
        self.bgColorButton.pack(fill = X)
        self.soundFrame.pack(fill = X)
        self.soundLabel.pack(fill = X)
        self.soundFile.pack(side = LEFT)
        self.soundLevel.pack(side = RIGHT)
        self.emptySpace.pack(fill = X)
        self.emptySpace2.pack(fill = X)
        self.commitButton.pack(fill = X)
        self.doneButton.pack(fill = X)

        # Place Right Frame GUI Widgets
        self.baseTypeFrame.pack(side = TOP, fill = X)
        self.baseTypeMenu.pack(side = RIGHT)
        self.baseTypeLabel.pack(side = RIGHT)
        self.emptySpace6.pack(fill = X)
        self.preview.pack(side = TOP, anchor = W)
        self.editFrame.pack(side = TOP, fill = X)
        self.scrollbar.pack(side = RIGHT, fill = Y)
        self.editArea.pack(side = RIGHT, fill = BOTH, expand = True)
        self.emptySpace7.pack(fill = X)
        self.commentLabel.pack(anchor = W)
        self.commentFrame.pack(side = TOP, fill = X)
        self.scrollbar2.pack(side = RIGHT, fill = Y)
        self.commentArea.pack(side = RIGHT, fill = BOTH, expand = True)

        # Set preview text
        self.previewText.set(headings[self.index].lstrip())

        # Set up comments area
        self.commentArea.config(state = "normal")
        self.commentArea.delete(1.0, END)
        self.commentArea.insert(END, commentsArray[self.index])
        self.commentArea.config(state = "disabled")

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
        self.preview.config(fg = "#C8C8C8")
        self.preview.config(bg = "#000000")
        self.preview.config(highlightbackground = "#000000")
        self.rarityUpdate(rarities[0])
        self.fontSizeUpdate(DEFAULT_FONT)
        self.fontSizeText.set(str(self.fontSize))
        self.setSoundFile(str(sounds[0]))
        self.setSoundLevel(str(soundLevels[0]))
        self.setDropLevel(levels[0])
        self.setDropOperator(operators[3])
        self.setItemLevel(levels[0])
        self.setItemOperator(operators[3])
        self.setQuality(qualities[0])
        self.setQualityOperator(operators[3])
        self.showHideUpdate(showHide[0])
        self.setCountOperator(operators[3])
        self.setCount(str(sockets[0]))
        self.setLinkOperator(operators[3])
        self.setLink(str(sockets[0]))
        self.rgbCheckbutton.config(state = 'normal')
        self.setRGB()
        self.setBaseType("All")        

        # Disable optoions appropriately
        if (self.index in enableRarity):
            self.disableRarity()
        if (self.index in enableQuality):
            self.disableQuality()
        if (self.index in enableSockets):
            self.disableSockets()

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
        if (self.linkText.get() == "1"):
            self.linkText.set("0")
            
        self.editArea.config(state = "normal")   
        # Call method to create Block text
        self.text.createBlockText(self.index, self.rarityText, \
                                  self.fontSize, self.textColor, \
                                  self.borderColor, self.bgColor, \
                                  self.comment.getText(), \
                                  self.showHideText, \
                                  self.soundFileText, \
                                  self.soundLevelText,
                                  self.dropOperatorText, \
                                  self.dropLevelText, \
                                  self.itemOperatorText, \
                                  self.itemLevelText, \
                                  self.qualityText,
                                  self.qualityOperatorText, \
                                  self.countText, \
                                  self.countOperatorText, \
                                  self.linkText, \
                                  self.linkOperatorText, \
                                  self.isRGB, self.baseTypeText)
        
        # Show preview
        self.editArea.delete(1.0, END)
        for text in self.textArray:
            self.editArea.insert(END, text)
            self.editArea.insert(END, "\n")
        self.editArea.insert(END, self.text.getText())
        self.editArea.config(state = "disabled")

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
        self.baseTypeText.set(value)
        if (value != "All"):
            self.previewText.set(value)
        else:
            self.previewText.set(headings[self.index].lstrip())

        # Call method to preview text
        self.editAreaInsert()

    # Method sets whether to show chromatic or not
    def setRGB(self):
        # Call method to preview text
        self.editAreaInsert()

    # Method set socket link operator
    def setLinkOperator(self, value):
        self.linkOperatorText.set(value)

        # Call method to preview text
        self.editAreaInsert()

    # Method sets socket link count
    def setLink(self, value):
        self.linkText.set(value)

        # Call method to preview text
        self.editAreaInsert()

    # Method set socket count operator
    def setCountOperator(self, value):
        self.countOperatorText.set(value)

        # Call method to preview text
        self.editAreaInsert()

    # Method sets socket count
    def setCount(self, value):
        self.countText.set(value)

        # Call method to preview text
        self.editAreaInsert()

    # Method set quality operator
    def setQualityOperator(self, value):
        self.qualityOperatorText.set(value)

        # Call method to preview text
        self.editAreaInsert()

    # Method sets quality
    def setQuality(self, value):
        self.qualityText.set(str(value))

        # Call method to preview text
        self.editAreaInsert()

    # Method sets drop level
    def setItemLevel(self, value):
        self.itemLevelText.set(str(value))

        # Call method to preview text
        self.editAreaInsert()

    # Method sets drop operator
    def setItemOperator(self, value):
        self.itemOperatorText.set(value)

        # Call method to preview text
        self.editAreaInsert()

    # Method sets drop level
    def setDropLevel(self, value):
        self.dropLevelText.set(str(value))

        # Call method to preview text
        self.editAreaInsert()

    # Method sets drop operator
    def setDropOperator(self, value):
        self.dropOperatorText.set(value)

        # Call method to preview text
        self.editAreaInsert()

    # Method sets sound file
    def setSoundFile(self, value):
        self.soundFileText.set(str(value))

        # Call method to preview text
        self.editAreaInsert()

    # Method set sound level
    def setSoundLevel(self, value):
        self.soundLevelText.set(str(value))

        # Call method to preview text
        self.editAreaInsert()

    # Method sets border colour
    def setBorderColor(self):
        color = askcolor(parent = self)
        self.preview.config(highlightbackground = color[1])   # hex color
        self.borderColor = color[0]                           # rgb color
        self.colorSet = True

        # Call method to preview text
        self.editAreaInsert()

    # Method sets background colour
    def setBGColor(self):
        color = askcolor(parent = self)
        self.preview.config(bg = color[1])   # hex color
        self.bgColor = color[0]              # rgb color
        self.colorSet = True

        # Call method to preview text
        self.editAreaInsert()

    # Method sets text colour
    def setTextColor(self):
        color = askcolor(parent = self)
        self.preview.config(fg = color[1])   # hex color
        self.textColor = color[0]            # rgb color
        self.colorSet = True

        # Call method to preview text
        self.editAreaInsert()

    # Method sets show or hide
    def showHideUpdate(self, value):
        self.showHideText.set(value)

        # Call method to preview text
        self.editAreaInsert()

    # Method updates font size
    def fontSizeUpdate(self, value):
        self.fontSize = value
        self.font.config(size = str(self.decideFontSize(value)))
        self.preview.config(font = self.font)

        # Call method to preview text
        self.editAreaInsert()

    # Method updates rarity selected
    def rarityUpdate(self, value):
        self.rarityText.set(value)
        
        # Set default colors
        if (not self.colorSet and \
            (headings[self.index].lstrip() == "Active Skill Gems" or \
             headings[self.index].lstrip() == "Support Skill Gems")):
            self.textColor = (27, 162, 155)
            self.preview.config(fg = "#1BA29B")
        elif (not self.colorSet and \
            headings[self.index].lstrip() == "Currency"):
            self.textColor = (170, 158, 130)
            self.preview.config(fg = "#AA9E82") 
        elif (not self.colorSet and \
            headings[self.index].lstrip() == "Quest Items"):
            self.textColor = (74, 230, 58)
            self.preview.config(fg = "#4AE63A") 
        elif (not self.colorSet and \
            headings[self.index].lstrip() == "Divination Card"):
            self.textColor = (170, 230, 230)
            self.preview.config(fg = "#AAE6E6")         
        elif (not self.colorSet and \
            (value == "All" or value == "Normal")):
            self.textColor = (200, 200, 200)
            self.preview.config(fg = "#C8C8C8")
        elif (not self.colorSet and value == "Unique"):
            self.textColor = (175, 96, 37)
            self.preview.config(fg = "#AF6025")
        elif (not self.colorSet and value == "Rare"):
            self.textColor = (255, 255, 119)
            self.preview.config(fg = "#FFFF77")
        elif (not self.colorSet and value == "Magic"):
            self.textColor = (136, 136, 255)
            self.preview.config(fg = "#8888FF")

        # Call method to preview text
        self.editAreaInsert()

    # Method disables rarity options
    def disableRarity(self):
        self.rarityMenu.config(state = "disabled")

    # Method disables quality options
    def disableQuality(self):
        self.qualityMenu.config(state = "disabled")
        self.qualityOperatorMenu.config(state = "disabled")

    # Method disables socket options
    def disableSockets(self):
        self.countOperatorMenu.config(state = "disabled")
        self.countMenu.config(state = "disabled")
        self.linkOperatorMenu.config(state = "disabled")
        self.linkMenu.config(state = "disabled")
        self.rgbCheckbutton.config(state = "disabled")

    # Method decides which BaseTypes to show
    def whichBaseTypes(self):
        if (self.index == 6):
            return lifeFlaskBaseTypes
        elif (self.index == 7):
            return manaFlaskBaseTypes
        elif (self.index == 8):
            return hybridFlaskBaseTypes
        elif (self.index == 9):
            return utilityFlaskBaseTypes
        elif (self.index == 10):
            return criticalUtilityFlaskBaseTypes
        elif (self.index == 13):
            return currencyBaseTypes
        elif (self.index == 14):
            return divinationBaseTypes
        else:
            return ["All"]
