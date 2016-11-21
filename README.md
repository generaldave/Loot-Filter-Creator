Written using Python 3.4.3 and tkinter (for GUI).

To start the wizard, user clicks on the Start menu and chooses whether to including dynamic leveling or not.

Once the wizard is done user can goto Export in the File menu to export the file. It will be called loot.filter and stored in the folder where Loot Filter Creator was extracted to.

The name of the file can either be changed in file explorer after created or in Variables.py (FILTER_NAME) at the top.

![mainwindow](https://cloud.githubusercontent.com/assets/7481680/20356922/08985752-abf4-11e6-947f-6977a8d4467d.png)

This functions completely, but will currently allow user to mess up his or her filter. For example, Quest Items should not have socket and rarity information, but currently defaults to including. The Commit button commits to the current rule and allows another to be created. The Done button commits the block or rules for the specific item class and moves on to the next class. User has to click commit before done or the newest ruleset will not be included.

![screenshot-body armours](https://cloud.githubusercontent.com/assets/7481680/20400737/ea2c4be0-acc3-11e6-88e8-ee5d640bb236.png)

This app is still under construction. Layout is not concrete.

Todo:

Work on commenting.

Include BaseTypes.
