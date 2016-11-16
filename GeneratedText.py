########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# GeneratedText class for my Path of Exile Loot Filter Creator.        #
#                                                                      #
# Created on 2016-11-13                                                #
#                                                                      #
########################################################################


########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from datetime  import date   # For today's date
from Variables import *      # Variables file

########################################################################
#                                                                      #
#                         GENERATED TEXT CLASS                         #
#                                                                      #
########################################################################

class GeneratedText(object):
    def __init__(self):
        self.text = ""
        self.start = ""
        self.end = ""

    # Get text
    def getText(self):
        return self.text

    # Set text
    def setText(self, t):
        self.text = t

    # Returns a 72 character line of # symbols
    def poundLine(self):
        line = ""
        for i in range(71):
            line = line + "#"
        return line

    # Returns a 72 character line that begins and ends with a # symbol
    # and only space in between
    def blankLine(self):
        line = "#"
        for i in range(69):
            line = line + " "
        line = line + "#"
        return line

    # PRE: A line of text
    # POST: A 72 character line containing the input line, filled out
    # with spaces and ending with a # symbol
    def lineFiller(self, line):
        length = 70 - len(line)
        for i in range(length):
            line = line + " "
        line = line + "#"
        return line

    # Method begins description
    def createDescription(self):
        line1 = "# Path of Exile Loot Filter generated with generaldave's"
        line1 = self.lineFiller(line1)

        line2 = "# Loot Filter Creator."
        line2 = self.lineFiller(line2)

        line3 = "# Created on " + str(date.today())
        line3 = self.lineFiller(line3)

        self.text = self.text        + \
                    self.poundLine() + "\n" + \
                    self.blankLine() + "\n" + \
                    line1            + "\n" + \
                    line2            + "\n" + \
                    self.blankLine() + "\n" + \
                    line3            + "\n" + \
                    self.blankLine()

    # Method inserts description lines
    def insertDescription(self, headings):
        for i in range(1, len(headings)):
            line = "# " + str(i) + ". " + headings[i]
            line = self.lineFiller(line)
            self.text = self.text + "\n" + line

    #  Method ends description
    def endDescription(self):
        self.text = self.text        + "\n" + \
                    self.blankLine() + "\n" + \
                    self.poundLine() + "\n"

    # Method creates heading
    def createHeading(self, heading):
        self.text = self.poundLine()                + "\n" + \
                    self.blankLine()                + "\n" + \
                    self.lineFiller("# " + heading) + "\n" + \
                    self.blankLine()                + "\n" + \
                    self.poundLine()                + "\n"

    # Method creates and returns a comment
    def createComment(self, comment):
        self.text =  "# " + comment.lstrip()

    # Method creates Block text
    def createBlockText(self, index, rarityText, fontSize, \
                        textColor, borderColor, bgColor, \
                        comment):
        # Show Class
        self.text = comment + "\n" + \
                    "Show"                   + "\n"  + \
                    "    Class \""                        + \
                    headings[index].lstrip() + "\""  + "\n"

        # Rarity
        if (rarityText.get() != "All"):
            self.text = self.text + \
                    "    Rarity " + rarityText.get() + "\n"

        # Font Size
        self.text = self.text + \
                    "    SetFontSize " + str(fontSize)    + "\n"

        # Text Color
        self.text = self.text                    + \
                    "    SetTextColor "          + \
                    str(int(textColor[0])) + " " + \
                    str(int(textColor[1])) + " " + \
                    str(int(textColor[2])) + "\n"

        # Border Color
        self.text = self.text                     + \
                    "    SetBorderColor "         + \
                    str(int(borderColor[0])) + " " + \
                    str(int(borderColor[1])) + " " + \
                    str(int(borderColor[2])) + "\n"

        # Background Color
        self.text = self.text                       + \
                    "    SetBackgroundColor "       + \
                    str(int(bgColor[0])) + " " + \
                    str(int(bgColor[1])) + " " + \
                    str(int(bgColor[2])) + "\n"
