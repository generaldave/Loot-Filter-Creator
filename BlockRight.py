########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# BlockRight Class for Path of Exile                                   #
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
#                           BLOCKRIGHT CLASS                          #
#                                                                     #
#######################################################################

class BlockRight(object):
    # Set up GUI
    def __init__(self, parent):
        self.parent = parent
        self.index = self.parent.index
        self.font = font.Font(family = "Helvetica",  size = 12)

        # Create Block Right Frame
        self.rightFrame    = Frame(self.parent)
        self.baseTypeFrame = Frame(self.rightFrame)
        self.editFrame     = Frame(self.rightFrame)
        self.commentFrame  = Frame(self.rightFrame)

        # Create Right GUI Widgets
        self.baseTypeLabel = Label(self.baseTypeFrame, \
                                   text = "Base Types:")
        self.baseTypeArray = self.whichBaseTypes()
        self.baseTypeText = StringVar()
        self.baseTypeText.set("All")
        self.baseTypeMenu = OptionMenu(self.baseTypeFrame, \
                                       self.baseTypeText, \
                                       *self.baseTypeArray, \
                                       command = self.parent.setBaseType)
        self.baseTypeMenu.config(width = 32)
        self.emptySpace6 = Button(self.rightFrame, \
                                  state = "disabled", \
                                  borderwidth = 0)
        self.previewText = StringVar()
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
        self.scrollbar2.config(command = self.commentArea.yview)

        # Place Block Right Frame
        self.rightFrame.pack(side = RIGHT, padx = 5)

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

    # Method sets defaults
    def setDefaults(self):
        self.baseTypeText.set("All")
        self.previewText.set("")
        self.preview.config(font = self.font)
        self.preview.config(fg = "#C8C8C8")
        self.preview.config(bg = "#000000")
        self.preview.config(highlightbackground = "#000000")
        self.clearEditArea()
        self.clearCommentArea()

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
        elif (self.index == 18):
            return bodyArmourBaseTypes
        elif (self.index == 19):
            return twoHandSwordBaseTypes
        elif (self.index == 20):
            return twoHandAxeBaseTypes
        elif (self.index == 21):
            return twoHandMaceBaseTypes
        elif (self.index == 22):
            return bowBaseTypes
        elif (self.index == 23):
            return staffBaseTypes
        elif (self.index == 24):
            return quiverBaseTypes
        elif (self.index == 25):
            return clawBaseTypes
        elif (self.index == 26):
            return daggerBaseTypes
        elif (self.index == 27):
            return wandBaseTypes
        elif (self.index == 28):
            return oneHandSwordBaseTypes
        elif (self.index == 29):
            return thrustingOneHandSwordBaseTypes
        elif (self.index == 30):
            return oneHandAxeBaseTypes
        else:
            return ["All"]

    # Method sets preview text
    def setPreviewText(self, value):
        self.previewText.set(value)

    # Method clears editArea
    def clearEditArea(self):
        self.editArea.config(state = "normal")
        self.editArea.delete(1.0, END)
        self.editArea.config(state = "disabled")

    # Method inserts text to editArea
    def insertEditArea(self, value):        
        self.editArea.config(state = "normal")
        self.editArea.insert(END, value)
        self.editArea.config(state = "disabled")

    # Method clears comments area
    def clearCommentArea(self):
        self.commentArea.config(state = "normal")
        self.commentArea.delete(1.0, END)
        self.commentArea.config(state = "disabled")

    # Method inserts text to commentArea
    def insertCommentArea(self, value):
        self.commentArea.config(state = "normal")
        self.commentArea.insert(END, value)
        self.commentArea.config(state = "disabled")        
