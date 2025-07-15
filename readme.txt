
This is the manual for setting up the program, some stuff needs to be installed before it can be executed
1. Install Apache Openoffice which can be found in the folder named "Installation files"
2. Install Python 3.7 (Can be found in "Installation Files")
3. Search for "Default app settings" on your computer and click "choose default app after file type"
4. Find the filetype .csv and choose open office
5. When you open a csv file with open office it should open with the following settings:
Character set: Unicode (UTF-8)
Language: English (UK)
Separated by: Semicolon
Text Delimiter: "
6. When you want to update the program, edit the source code then you google "auto-py-to-exe" which is downloadable and run from the terminal.
After you're done with editing the source code, run auto-py-to-exe and create the program into one file. 
Make sure that you have installed the necessary packages on your windows using pip install as they need to be installed in order for the program to be able to be run everywhere

Known errors:
If it can't find a module, write "pip install <module name>" in the terminal

If .ssh/known_hosts isn't found: run ssh root@lundsnaturvetarkar.se in the terminal
Then if it asks, "Are you sure you want to continue connecting", write yes. Don't do anything else, turn off the terminal and try uploading again

If it can't load or find the Qt platform plugin "windows":
1. Right click on "My computer" and go into "Properties" and "Advanced System settings"
2. Go into "Environment variables" 
3.Create the system variable "QT_PLUGIN_PATH" with directory c:\ProgramData\Anaconda3\Library\plugins or wherever your "plugins" folder for anaconda is.


Files:
The html file named list is the quest list. This is updated through the csv file named quest_list
To update the html file all you need to do is change what you want to change in the csv file and upload everything using the program

The image named Points_Plot is the points plot for the different teams. This is also updated using the program
The data.csv file is the file containing the points and the time of inputting the points.

The folder "Other" contains Data from previous years, the password for uploading, scripts for the program as well as images used. 
It also contains a Test.txt file which has been used to test the program.

The program contains several functions. In the program (opens very slowly), you can click the tab "Options" and go to "Help" which will tell you all about the features.

The image PM_logo is the logo for the main window, it needs to be in the same folder as the program. The same goes for the files: "data.csv", "quest_list.csv", list and Points_Plot