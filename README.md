Written using Python 3.4.3 and tkinter (for GUI).

To start the wizard, user clicks on the File menu and chooses New.

Once the wizard is done user can goto Export in the File menu to export the file. It will be called loot.filter and stored in the folder where Loot Filter Creator was extracted to.

The name of the file can either be changed in file explorer after created or in Variables.py (FILTER_NAME) at the top.

![mainwindow2](https://cloud.githubusercontent.com/assets/7481680/20509893/1f45341c-b03a-11e6-8c6d-ca80b7c4f8b6.png)

This functions completely, but is not finished. The Commit button commits to the current rule and allows another to be created. The Done button commits the block of rules for the specific item class and moves on to the next class. User has to click commit before done or the newest ruleset will not be included.

![blockwindow3](https://cloud.githubusercontent.com/assets/7481680/20509906/390ad7da-b03a-11e6-9250-f8303aa371d1.png)

This app is still under construction. Layout is not concrete.

Todo:

Work on commenting, Filtration compatibility.

Finish BaseTypes.

Default DropLevels.

Add notes, like possible uniques and Divination Card descriptions.
