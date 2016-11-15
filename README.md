Written using Python 3.4.3 and tkinter (for GUI).

To start the wizard, user clicks on the Start menu and chooses whether to including dynamic leveling or not.

Once the wizard is done user can goto Export in the File menu to export the file. It will be called loot.filter and stored in the folder where Loot Filter Creator was extracted to.

The name of the file can either be changed in file explorer after created or in Variables.py (FILTER_NAME) at the top.

![Main Form](https://cloud.githubusercontent.com/assets/7481680/20274895/54e33ff0-aa64-11e6-9602-23be3117898e.png)

User can currently change rarity, text size, text colour, border colour, and background colour. The Commit button commits to that rule and allows another to be created. The Done button commits the block and moves on to the next class. Currently user has to click commit before done.

![block](https://cloud.githubusercontent.com/assets/7481680/20327149/e5592f4a-ab59-11e6-939a-55392f0568b1.png)

This app is still under construction. Layout is not concrete.

Todo:

Work on commenting.
Include Item Level, Drop Level, Quality,  BaseType, Socket, Height, and Weight options.
Inclued Alert Sound action.
Be able to decide Show/Hide.
Drop the Dynamic option - Item Level and Drop Level for all.
