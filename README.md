Written using Python 3.4.3 and tkinter (for GUI).

To start the wizard, user clicks on the Start menu and chooses whether to including dynamic leveling or not.

Once the wizard is done user can goto Export in the File menu to export the file. It will be called loot.filter and stored in the folder where Loot Filter Creator was extracted to.

The name of the file can either be changed in file explorer after created or in Variables.py (FILTER_NAME) at the top.

![mainwindow](https://cloud.githubusercontent.com/assets/7481680/20356922/08985752-abf4-11e6-947f-6977a8d4467d.png)

User can currently change rarity, text size, text colour, border colour, and background colour. The Commit button commits to that rule and allows another to be created. The Done button commits the block and moves on to the next class. Currently user has to click commit before done.

![blockwindow](https://cloud.githubusercontent.com/assets/7481680/20356967/2f69c2ee-abf4-11e6-9cc0-2c11b5b90218.png)

This app is still under construction. Layout is not concrete.

Todo:

Work on commenting.

Include Item Level, Drop Level, Quality,  BaseType, Sockets, Height, and Width options.

Include Alert Sound action.

Appropriate default colours.
