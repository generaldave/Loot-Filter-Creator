########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# BlockLeft Class for Path of Exile                                    #
#                                                                      #
# Created on 2016-11-28                                                #
#                                                                      #
########################################################################


########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from tkinter   import *      # For GUI
from tkinter   import font   # For fonts
from Variables import *      # Variables file
from BaseTypes import *      # BaseTypes file

#######################################################################
#                                                                     #
#                           BLOCKLEFT CLASS                           #
#                                                                     #
#######################################################################

class BlockLeft(object):
    # Set up GUI
    def __init__(self, parent):
        self.parent   = parent
        self.index    = self.parent.index
        self.font     = font.Font(family = "Helvetica",  size = 12)
        self.fontSize = DEFAULT_FONT
        self.colorSet = self.parent.colorSet

        # Create Left Right Frame
        self.leftFrame     = Frame(self.parent)
        self.rarityFrame   = Frame(self.leftFrame)
        self.soundFrame    = Frame(self.leftFrame)
        self.fontFrame     = Frame(self.leftFrame)
        self.dropFrame     = Frame(self.leftFrame)
        self.itemFrame     = Frame(self.leftFrame)
        self.qualityFrame  = Frame(self.leftFrame)
        self.socketFrame   = Frame(self.leftFrame)
        self.countFrame    = Frame(self.socketFrame)
        self.linkFrame     = Frame(self.socketFrame)

        # Create Left GUI Widgets
        self.showHideText = StringVar()
        self.showHideText.set(showHide[0])
        self.showHideMenu = OptionMenu(self.leftFrame, \
                          self.showHideText, \
                          *showHide, \
                          command = self.parent.showHideUpdate)
        self.emptySpace3 = Button(self.leftFrame, \
                                  state = "disabled", \
                                  borderwidth = 0)
        self.rarityLabel = Label(self.rarityFrame, text = "Rarity:")
        self.rarityText = StringVar()
        self.rarityText.set(rarities[0])
        self.rarityMenu = OptionMenu(self.rarityFrame, \
                          self.rarityText, \
                          *rarities, \
                          command = self.parent.rarityUpdate)
        self.rarityMenu.config(width = 10)
        self.qualityLabel = Label(self.qualityFrame, text = "Quality:")
        self.qualityOperatorText = StringVar()
        self.qualityOperatorText.set(operators[3])
        self.qualityOperatorMenu = OptionMenu(self.qualityFrame, \
                                      self.qualityOperatorText, \
                                      *operators, \
                                      command = self.parent.setQualityOperator)
        self.qualityText = StringVar()
        self.qualityText.set(qualities[0])
        self.qualityMenu = OptionMenu(self.qualityFrame, \
                                     self.qualityText, \
                                     *qualities, \
                                     command = self.parent.setQuality)
        self.itemLevelLabel = Label(self.itemFrame, text = "Item Level:")
        self.itemOperatorText = StringVar()
        self.itemOperatorText.set(operators[3])
        self.itemOperatorMenu = OptionMenu(self.itemFrame, \
                                          self.itemOperatorText, \
                                          *operators, \
                                          command = self.parent.setItemOperator)
        self.itemLevelText = StringVar()
        self.itemLevelText.set(str(levels[0]))
        self.itemLevelMenu = OptionMenu(self.itemFrame, \
                                        self.itemLevelText, \
                                        *levels, \
                                        command = self.parent.setItemLevel)
        self.dropOperatorText = StringVar()
        self.dropOperatorText.set(operators[3])
        self.dropOperatorMenu = OptionMenu(self.dropFrame, \
                                          self.dropOperatorText, \
                                          *operators, \
                                          command = self.parent.setDropOperator)
        self.dropLevelLabel = Label(self.dropFrame, text = "Drop Level:")
        self.dropLevelText = StringVar()
        self.dropLevelText.set(str(levels[0]))
        self.dropLevelMenu = OptionMenu(self.dropFrame, \
                                        self.dropLevelText, \
                                        *levels, \
                                        command = self.parent.setDropLevel)
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
                                            command = self.parent.setCountOperator)
        self.countText = StringVar()
        self.countText.set(str(sockets[1]))
        self.countMenu = OptionMenu(self.countFrame, \
                                   self.countText, \
                                   *sockets, \
                                   command = self.parent.setCount)
        self.linkLabel = Label(self.linkFrame, text = "Linked:")
        self.linkOperatorText = StringVar()
        self.linkOperatorText.set(operators[3])
        self.linkOperatorMenu = OptionMenu(self.linkFrame, \
                                            self.linkOperatorText, \
                                            *operators, \
                                            command = self.parent.setLinkOperator)
        self.linkText = StringVar()
        self.linkText.set(str(sockets[0]))
        self.linkMenu = OptionMenu(self.linkFrame, \
                                   self.linkText, \
                                   *sockets, \
                                   command = self.parent.setLink)
        self.linkMenu['menu'].entryconfigure(1, state = "disabled")
        self.isRGB = IntVar()
        self.rgbCheckbutton = Checkbutton(self.socketFrame, \
                                          text = "Chromatic?",
                                          variable = self.isRGB, \
                                          command = self.parent.setRGB)        
        self.emptySpace5 = Button(self.leftFrame, \
                                  state = "disabled", \
                                  borderwidth = 0)
        self.fontLabel = Label(self.fontFrame, text = "Font:")
        self.fontSizeText = StringVar()
        self.fontSizeText.set(str(self.fontSize))
        self.fontSizeMenu = OptionMenu(self.fontFrame, \
                                       self.fontSizeText, \
                                       *fontSizes, \
                                       command = self.parent.fontSizeUpdate)
        self.fontSizeMenu.config(width = 10)
        self.textColorButton = Button(self.leftFrame, \
                                      text = "Text Colour", \
                                      command = self.parent.setTextColor)
        self.borderColorButton = Button(self.leftFrame, \
                                        text = "Border Colour", \
                                        command = self.parent.setBorderColor)
        self.bgColorButton = Button(self.leftFrame, \
                                    text = "Background Colour", \
                                    command = self.parent.setBGColor)
        self.soundLabelText = "Sound File:     Volume:"
        self.soundLabel = Label(self.soundFrame, \
                                text = self.soundLabelText)
        self.soundFileText = StringVar()
        self.soundFileText.set(str(sounds[0]))
        self.soundFile = OptionMenu(self.soundFrame, \
                                     self.soundFileText, \
                                     *sounds, \
                                     command = self.parent.setSoundFile)
        self.soundFile.config(width = 6)
        self.soundLevelText = StringVar()
        self.soundLevelText.set(str(soundLevels[0]))
        self.soundLevel = OptionMenu(self.soundFrame, \
                                     self.soundLevelText, \
                                     *soundLevels, \
                                     command = self.parent.setSoundLevel)
        self.soundLevel.config(width = 6)
        self.emptySpace = Button(self.leftFrame, \
                                 state = "disabled", \
                                 borderwidth = 0)
        self.emptySpace2 = Button(self.leftFrame, \
                                 state = "disabled", \
                                 borderwidth = 0)
        self.commitButton = Button(self.leftFrame, \
                                   text = "Commit", \
                                   command = self.parent.commitText)
        self.doneButton = Button(self.leftFrame, \
                                 text = "Done", \
                                 command = self.parent.destroy)

        # Place Block Left Frame
        self.leftFrame.pack(side = LEFT, padx = 5)

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

    # Method sets defaults
    def setDefaults(self):
        self.showHideText.set(showHide[0])
        self.rarityText.set(rarities[0])
        self.qualityOperatorText.set(operators[3])
        self.qualityText.set(qualities[0])
        self.itemOperatorText.set(operators[3])
        self.itemLevelText.set(str(levels[0]))
        self.dropOperatorText.set(operators[3])
        self.dropLevelText.set(str(levels[0]))
        self.countOperatorText.set(operators[3])
        self.countText.set(str(sockets[1]))
        self.linkOperatorText.set(operators[3])
        self.linkText.set(str(sockets[0]))
        self.rgbCheckbutton.config(state = 'normal')
        self.isRGB.set(0)
        self.fontSizeText.set(str(self.parent.fontSize))
        self.soundFileText.set(str(sounds[0]))
        self.soundLevelText.set(str(soundLevels[0]))

        # Disable optoions appropriately
        if (self.index in enableRarity):
            self.disableRarity()
        if (self.index in enableQuality):
            self.disableQuality()
        if (self.index in enableSockets):
            self.disableSockets()

        # Call method to set default colours
        self.setDefaultColours(rarities[0])

        self.parent.editAreaInsert()

    # Method sets default colours
    def setDefaultColours(self, value):
        # Set default colors
        if (not self.colorSet and \
            (headings[self.index].lstrip() == "Active Skill Gems" or \
             headings[self.index].lstrip() == "Support Skill Gems")):
            self.parent.textColor = (27, 162, 155)
            self.parent.rightFrame.preview.config(fg = "#1BA29B")
        elif (not self.colorSet and \
            headings[self.index].lstrip() == "Currency"):
            self.parent.textColor = (170, 158, 130)
            self.parent.rightFrame.preview.config(fg = "#AA9E82")
        elif (not self.colorSet and \
            headings[self.index].lstrip() == "Quest Items"):
            self.parent.textColor = (74, 230, 58)
            self.parent.rightFrame.preview.config(fg = "#4AE63A")
        elif (not self.colorSet and \
            headings[self.index].lstrip() == "Divination Card"):
            self.parent.textColor = (170, 230, 230)
            self.parent.rightFrame.preview.config(fg = "#AAE6E6")  
        elif (not self.colorSet and \
            (value == "All" or value == "Normal")):
            self.parent.textColor = (200, 200, 200)
            self.parent.rightFrame.preview.config(fg = "#C8C8C8")
        elif (not self.colorSet and value == "Unique"):
            self.parent.textColor = (175, 96, 37)
            self.parent.rightFrame.preview.config(fg = "#AF6025")
        elif (not self.colorSet and value == "Rare"):
            self.parent.textColor = (255, 255, 119)
            self.parent.rightFrame.preview.config(fg = "#FFFF77")
        elif (not self.colorSet and value == "Magic"):
            self.parent.textColor = (136, 136, 255)
            self.parent.rightFrame.preview.config(fg = "#8888FF")

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
        
