########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# MenuBar Class for Path of Exile                                      #
#                                                                      #
# Created on 2016-11-27                                                #
#                                                                      #
########################################################################


########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from tkinter import *   # For GUI

#######################################################################
#                                                                     #
#                            MENUBAR CLASS                            #
#                                                                     #
#######################################################################

class MenuBar(object):
    def __init__(self, parent, grandparent):
        self.parent      = parent        # LootFilterCreator
        self.grandparent = grandparent   # Root

        # Create Menu
        menubar = Menu(self.grandparent)
        fileMenu = Menu(menubar, tearoff = False)
        fileMenu.add_command(label = "New", \
                             command = self.parent.createFilter)
        fileMenu.add_separator()
        fileMenu.add_command(label = "Export", \
                             command = self.parent.exportFilter)
        fileMenu.add_separator()
        fileMenu.add_command(label = "Exit", \
                             command = self.grandparent.destroy)

        # Place Menu
        menubar.add_cascade(label = "File", menu = fileMenu)
        self.grandparent.config(menu = menubar)
