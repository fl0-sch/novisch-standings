# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 12:46:50 2018

@author: jespe
"""

#Important packages
import datetime
import os
import paramiko
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import messagebox
import tkinter as tk
from matplotlib import rcParams
from PIL import Image, ImageTk


#The GUI class
class PM(object):
    rcParams['font.family'] = 'Comic Sans MS'
    
    def __init__(self):
        #Want the first box to be the password prompt
                
        first_screen = self.first_screen = tk.Tk(screenName = "PM")
        first_screen.title("PM")
        paw = self.pw = tk.Label(first_screen, text = "Password:")
        paw.grid(row = 0, column = 0)
        
        intro_password = self.intro_password = tk.Entry(first_screen, show = "*", width = 15)
        intro_password.grid(row = 0, column = 1)
        intro_password.focus()
        
        ok_button = tk.Button(first_screen, text = "Enter Password", width = 20, command = self.try_login)
        ok_button.grid(row = 1, column = 0)
        
        cancel = tk.Button(first_screen, text = "Cancel", width = 20, command = first_screen.destroy)
        cancel.grid(row = 1, column = 1)
        
        first_screen.bind("<Return>", self.try_login)
        first_screen.mainloop()
    
    def try_login(self, event = None):
        
        if self.intro_password.get() == "mainsequence3050":
            self.main_menu()            
        else:
            tk.messagebox.showwarning(title = "Warning", message = "Incorrect password")
		
    def choose_mode(self):
        
        cmw = self.choose_mode_win = tk.Toplevel()
        cmw.attributes("-topmost",True)
        
        menu = tk.Menu(cmw)
        cmw.config(menu=menu)
        menu.add_cascade(label = "Help",command = self.mode_help)
        
        label = tk.Label(cmw,text = "Please choose Mode")
        label.pack(side = tk.TOP)
        
        single_button = tk.Button(cmw,text = "Single",width = 20,height = 4,command = self.set_single_mode)
        single_button.pack(side = tk.LEFT)
        
        single_button = tk.Button(cmw,text = "Multiple",width = 20,height = 4,command = self.set_multiple_mode)
        single_button.pack(side = tk.LEFT)
        
    def mode_help(self):
        
        tk.messagebox.showinfo("Mode Help",
        """Single mode means that only one team can get full points for a noon-repeatable experiment, other teams may only get pity points.

Multiple mode means that each team may do each non-repeatable experiment and get full points. No pity points are awarded here though as each team can only get points once per experiment

You can always change mode by pressing the bottom right button in the main menu.
        """)
        
        
        
    def set_single_mode(self):
        
        self.toggle_mode = 0
        self.toggle_button.config(text = "Single")
        self.choose_mode_win.destroy()
        
    def set_multiple_mode(self):
        
        self.toggle_mode = 1
        self.toggle_button.config(text = "Multiple")
        self.choose_mode_win.destroy()    
        
    def main_menu(self):
        self.first_screen.destroy()
        root = self.root = tk.Tk(screenName = "PM")
        root.title("PM")
        root.focus_force()
        menu = self.menu = tk.Menu(root)
        root.config(menu=menu)
        filemenu = tk.Menu(menu, tearoff = False)
        menu.add_cascade(label = "Options", menu = filemenu)
        filemenu.add_command(label = "Help", command = self.Help)
        filemenu.add_command(label = "Previous Pointmasters",command = self.pm_history)
        filemenu.add_command(label = "Exit", command = root.destroy)
        
        logo = Image.open("PM_logo.png")
        logo = logo.resize((435,438),Image.Resampling.LANCZOS)
        logo_tk = ImageTk.PhotoImage(logo)
        
        pm_logo = tk.Label(image = logo_tk)
        pm_logo.pack(side = tk.TOP)
        
        #Initiates the quest point input box
        quest_button = self.quest_button = tk.Button(root,text = "Quest",width = 10, height = 2, command = self.quest_box)
        #quest_button.grid(row = 0, column = 0)
        quest_button.pack(side = tk.LEFT)
        root.bind("<q>", self.quest_box)
               
        #Initiates the event point input box, the following do the same but for the different features
        event_button = self.event_button = tk.Button(root, text = "Event", width = 11, height = 2, command = self.event_box)
        #event_button.grid(row = 0, column = 1)
        event_button.pack(side = tk.LEFT)
        root.bind("<e>", self.event_box)
        
        upload_button = self.upload_button = tk.Button(root, text = "Upload", width = 11, height = 2, command = self.upload_window)
        #upload_button.grid(row = 1, column = 0)
        upload_button.pack(side = tk.LEFT)
        root.bind("<u>", self.upload_window)
        
        score_button = self.score_button = tk.Button(root, text = "Show score", width = 11, height = 2, command = self.score)
        #score_button.grid(row = 1, column = 1)
        score_button.pack(side = tk.LEFT)
        root.bind("<s>", self.score)
        
        plot_button = self.plot_button = tk.Button(root, text = "Plot", width = 11, height = 2, command = self.make_plot)
        #plot_button.grid(row = 2, column = 0)
        plot_button.pack(side = tk.LEFT)
        root.bind("<p>", self.make_plot)
        
        reset_button = self.reset_button = tk.Button(root, text = "Reset", width = 10, height = 2, command = self.reset_window)
        #reset_button.grid(row = 2, column = 1)
        reset_button.pack(side = tk.LEFT)
        root.bind("<r>", self.reset_window)
        
        toggle_button = self.toggle_button = tk.Button(root, text = "Choose mode", width = 10, height = 2, command = self.toggle_mode)
        toggle_button.pack(side = tk.LEFT)

        self.choose_mode()
        root.mainloop()

        
    def toggle_mode(self, tog = [0]):
        
        tog[0] = not tog[0]
        
        
        if tog[0]:
            self.toggle_button.config(text = "Single")
            self.toggle_mode = 0
            
        else:
            self.toggle_button.config(text = "Multiple")
            self.toggle_mode = 1
            
    def pm_history(self):
        
        tk.messagebox.showinfo(
            "History",
            """Previous Pointmasters:
----
Sebastian Wolsing

Alexander Ekman (Nycklis) - Created the first version of the Pointmaster program

John Wimarsson

Jesper Nielsen - Updated the Pointmaster program and addded a GUI

Caisa Kjellström & Stina Magndal

VENDELA GUSTAFSSON och love o

Lina Åkesson och Minoo Gandomi :D

Ellen Brandt Sahlberg & Alma Ragnarsson <3
            """)        
        
        
    def Help(self):#Help menu with all the information to use the program as well
        help_window = self.help_window = tk.Toplevel()
        
        label = tk.Label(help_window, text = "What do you need help with?")
        label.pack(side = tk.TOP)
        
        help_what = tk.Button(help_window, text = "What is this?", command = self.Information)
        help_what.pack(side = tk.LEFT)
        
        help_names = tk.Button(help_window, text = "Team names", command = self.name_message)
        help_names.pack(side = tk.LEFT)
    
    def Information(self):
        #Simple message box with multi line string
        tk.messagebox.showinfo(
                "Information",
                """Welcome to the pointmaster program! Here you can add points to the different teams during the novischperiod!

To add points for a single event such as a competition or finding the mascot etc., simply press the "Event" button and enter the amount of points the team won.

To add points for a quest, press the "Quest" button and enter the quest number as well as the quest number and the amount of bonus points. If the quest has been taken, you will receive the option of adding pitty points. Be sure to write the correct team names.

For information about the teamnames you should input, press the team names button in the previous window.

If you want to upload the quest list and the plot to the webpage, press "Upload". This uploads the quest list and plot to the webpage! This can only be done if all teams have achieved points and you've done more than one entry!

If you want to simply show the score, press "Show Score"

If you want to reset the data, press "Reset", you will recieve a warning so you don't accidentally reset everything 

If you only want to plot the data, press "Plot". Note that you can only plot when all teams have points, you also need more than one entry! You can also add two event entries where all the teams get 0 points if you want to plot 0 points """)
    
    def name_message(self):
        
        tk.messagebox.showinfo(
                "Team names", 
                """ The following are the team names you input in the quest box:

bug - BUG
lemur - LEMUR
snys - SNYS
glufs - GLuFS """)
      
    def quest_box(self, event = None):
        #The box which allows quest point inputs
        win = self.quest_win = tk.Toplevel()
        win.wm_title("Quest")
        
        #Simple labels and input boxes
        team = self.team = tk.Label(win, text = "Team: ", width = 20)
        team.grid(row = 0, column = 0)
        
        number = self.number = tk.Label(win, text = "Quest Number: ", width = 20)
        number.grid(row = 1, column = 0)
        
        teamname = self.teamname = tk.Entry(win)
        teamname.focus()
        number_entry = self.number_entry = tk.Entry(win)
        
        teamname.grid(row = 0, column = 1)
        number_entry.grid(row = 1, column = 1)
        
        bonus = self.bonus = tk.Label(win, text = "Bonus points: ", width = 20)
        bonus.grid(row = 2, column = 0)
        
        bonuspoints = self.bonuspoints = tk.Entry(win)
        bonuspoints.grid(row = 2, column = 1)        
        
        button = tk.Button(win, text = "Add quest points",width = 20, command = self.add_quest)
        button.grid(row = 3, column = 0)
        
        button = tk.Button(win, text = "Cancel", width = 20, command = win.destroy)
        button.grid(row = 3, column = 1)
        
        #Allows for return and escape inputs instead of only needing to press the button all the time
        win.bind("<Return>", self.add_quest)
        
       
    
    def event_box(self, event = None):#Similar to quest box but for events
        win = self.event_win = tk.Toplevel()
        win.wm_title("Event")
        
        BUG = self.BUG = tk.Label(win, text = "BUG:", width = 20)
        BUG.grid(row = 0, column = 0)
        
        lemur = self.lemur = tk.Label(win, text = "LEMUR: ", width = 20)
        lemur.grid(row = 2, column = 0)
        
        glufs = self.glufs = tk.Label(win, text = "GLuFS: ", width = 20)
        glufs.grid(row = 0, column = 1)
        
        snys = self.snys = tk.Label(win, text = "SNYS: ", width = 20)
        snys.grid(row = 2, column = 1)
    
        BUG_points = self.BUG_points = tk.Entry(win)
        BUG_points.grid(row = 1, column = 0)
        BUG_points.focus()
        
        lemur_points = self.lemur_points = tk.Entry(win)
        lemur_points.grid(row = 3, column = 0)
        
        glufs_points = self.glufs_points = tk.Entry(win)
        glufs_points.grid(row = 1, column = 1)
        
        snys_points = self.snys_points = tk.Entry(win)
        snys_points.grid(row = 3, column = 1)
        
        button = tk.Button(win, text = "Add event points", width = 20, command = self.add_event)
        button.grid(row = 4, column = 0)
        
        button = tk.Button(win, text = "Cancel", width = 20, command = win.destroy)
        button.grid(row = 4, column = 1)
        
        win.bind("<Return>", self.add_event)
        
        
    
        
    def add_event(self, event = None):
        #Defines the several data types for keywords
        da_types = {"time":str, "quest_number":int, "quest_value":int, "bonus":int, "pitty_points":int, "glufs":int, "bug":int, "lemur":int, "snys":int}
        #Reads the data files and sets the types according to da_types
        data = pd.read_csv("data.csv", encoding="utf8", delimiter=";", header=0, dtype=da_types)
        #Creates a dictionary to set the points to be added
        new_score = {"time":datetime.datetime.now(),
                   "quest_number":0,
                   "quest_value":0,
                   "bonus":0,
                   "pitty_points":0,
                   "glufs":0,
                   "bug":0,
                   "lemur":0,
                   "snys":0}
        #Sets the inputted points inside new_score
        new_score["bug"] = int(self.BUG_points.get())
        new_score["lemur"] = int(self.lemur_points.get())
        new_score["glufs"] = int(self.glufs_points.get())
        new_score["snys"] = int(self.snys_points.get())
        #Appends the new score into the data file
        data = data._append(new_score, ignore_index=True)
        #Converts to csv to spearate by ;
        data.to_csv("data.csv", header=True, index=False, sep=";")
        #Confirms that the points were added
        print("Points Added")
        self.event_win.destroy()
        
        
    def add_quest(self, event = None):
        #Sets the type for the different keywords
        qu_types = {"quest_number":int, "quest_description":str, "quest_value":int, "quest_repeat":str, "quest_owner":str}
        da_types = {"time":str, "quest_number":int, "quest_value":int, "bonus":int, "pitty_points":int, "glufs":int, "bug":int, "lemur":int, "snys":int}
        #Reads the quest and data files
        quests = pd.read_csv("quest_list.csv", encoding="utf8", delimiter=";", header=0, dtype=qu_types)
        data = pd.read_csv("data.csv", encoding="utf8", delimiter=";", header=0, dtype=da_types)
        
        #Gets the quest value from the quest list and the inputs from the quest box
        quest_owner = self.teamname.get()
        quest_number=int(self.number_entry.get())
        bonus_points=int(self.bonuspoints.get())
        quest_value = int(quests["quest_value"].loc[quests['quest_number'] == quest_number])
        quest_owner_onfile = quests.loc[quests['quest_number'] == quest_number,'quest_owner'].values[0]
        quest_repeat_onfile = quests.loc[quests['quest_number'] == quest_number,'quest_repeat'].values[0]
        
        #Checks if the inputted quest owner is the right teamname
        if self.toggle_mode == 1:    
            if quest_owner not in ("lemur","snys","glufs","bug"):
                raise TypeError("Wrong teamname")
            #check_list = ["bug","lemur","glufs","snys"]
            elif (quest_owner in quest_owner_onfile.split(",") and
            quest_repeat_onfile == "single"):
                raise TypeError("Quest already taken by this team")
            
            elif(quest_owner_onfile != "none" and
               quest_repeat_onfile == "single"):
               pitty_points = 0 
               new_addition = quest_owner_onfile+quest_owner+","
               quests.loc[quests["quest_number"] == quest_number, "quest_owner"] = new_addition
               quests.to_csv("quest_list.csv", header = True, index = False, sep = ";")
               new_score = {"time":datetime.datetime.now(),
                            "quest_number":quest_number,
                            "quest_value":quest_value,
                            "bonus":bonus_points,
                            "pitty_points":pitty_points,
                            "glufs":0,
                            "bug":0,
                            "lemur":0,
                            "snys":0}
               new_score[quest_owner]=quest_value+bonus_points+pitty_points
               data = data._append(new_score, ignore_index=True)
               data.to_csv("data.csv", header=True, index=False, sep=";")
               print("Points Added")
            #If the quest already has an owner and it cannot be repeated multiple times:               
                    #quest_owner=quests.loc[quests['quest_number'] == quest_number,'quest_owner'].values[0]
            
            else:
                    pitty_points = 0
                    
                    #Only update the quest owner when the quest is done for the first time, similar way as the event points
                    quests.loc[quests['quest_number'] == quest_number, "quest_owner"] = quest_owner+","
                    quests.to_csv("quest_list.csv", header=True, index=False, sep=";")
                    new_score = {"time":datetime.datetime.now(),
                       "quest_number":quest_number,
                       "quest_value":quest_value,
                       "bonus":bonus_points,
                       "pitty_points":pitty_points,
                       "glufs":0,
                       "bug":0,
                       "lemur":0,
                       "snys":0}
    
                    new_score[quest_owner]=quest_value+bonus_points+pitty_points
                    data = data._append(new_score, ignore_index=True)
                    data.to_csv("data.csv", header=True, index=False, sep=";")
                    print("Points Added")
        
        elif self.toggle_mode == 0:
            if quest_owner not in ("lemur","snys","glufs","bug"):
                    raise TypeError("Wrong teamname")
            elif(quest_owner_onfile != "none" and quest_repeat_onfile == "single"):
                print("This quest has been taken")
                self.pitty_box()
            else:
                pitty_points = 0
                quests.loc[quests['quest_number'] == quest_number, "quest_owner"] = quest_owner
                quests.to_csv("quest_list.csv", header=True, index=False, sep=";")
                new_score = {"time":datetime.datetime.now(),
                       "quest_number":quest_number,
                       "quest_value":quest_value,
                       "bonus":bonus_points,
                       "pitty_points":pitty_points,
                       "glufs":0,
                       "bug":0,
                       "lemur":0,
                       "snys":0}
    
                new_score[quest_owner]=quest_value+bonus_points+pitty_points
                data = data._append(new_score, ignore_index=True)
                data.to_csv("data.csv", header=True, index=False, sep=";")
                print("Points Added")
        else:
            tk.messagebox.showwarning(title = "Warning", message = "Please choose a mode")
            self.quest_win.destroy()                
        
    #This is for the moment useless as all teams can perform each quest once. Should this change then this is used to give pitty points to quests already taken    
    def pitty_box(self, event = None):
        #Allows for inputs to pitty points
        win2 = self.pitty_win = tk.Toplevel()        
        
        label = tk.Label(win2, text = "This quest has been taken, \n please enter pitty points", width = 20)
        label.grid(row = 0, column = 0)
                
        pittylabel = tk.Label(win2, text = "Pitty point: ", width = 20)
        pittylabel.grid(row = 1, column = 0)
            
        pittypoints = self.pittypoints = tk.Entry(win2)
        pittypoints.grid(row = 1, column = 1)
        pittypoints.focus()
              
        pittybutton = tk.Button(win2, text = "Add pitty points", command = self.pitty_adder, width = 20)
        pittybutton.grid(row = 2, column = 0)
        
        button = tk.Button(win2, text = "Cancel", command = win2.destroy, width = 20)
        button.grid(row = 2, column = 1)
        
        win2.bind("<Return>",self.pitty_adder)
    
    def pitty_adder(self, event = None):
        #Adds the pitty points, same method as adding quests
        da_types = {"time":str, "quest_number":int, "quest_value":int, "bonus":int, "pitty_points":int, "glufs":int, "bug":int, "lemur":int, "snys":int}
        data = pd.read_csv("data.csv", encoding="utf8", delimiter=";", header=0, dtype=da_types)
        quest_number = int(self.number_entry.get())
        quest_owner = self.teamname.get()
        quest_value = 0
        bonus_points = int(self.bonuspoints.get())
        pitty_points = int(self.pittypoints.get())
        
        new_score = {"time":datetime.datetime.now(),
                   "quest_number":quest_number,
                   "quest_value":quest_value,
                   "bonus":bonus_points,
                   "pitty_points":pitty_points,
                   "glufs":0,
                   "bug":0,
                   "lemur":0,
                   "snys":0}
       
        new_score[quest_owner]=quest_value+bonus_points+pitty_points
        data = data._append(new_score, ignore_index=True)
        data.to_csv("data.csv", header=True, index=False, sep=";")
        print("Points Added")
        self.pitty_win.destroy()
    
    def upload_window(self, event = None):#Window for password when uploading
        
        upload_win = self.upload_window = tk.Toplevel()
        
        pw = self.pw = tk.Label(upload_win, text = "Password:")
        pw.grid(row = 0, column = 0)
        
        password_entry = self.password = tk.Entry(upload_win, show = "*", width = 15)
        password_entry.grid(row = 0, column = 1)
        password_entry.focus()
        
        ok = tk.Button(upload_win, text = "Enter Password", width = 20, command = self.upload)
        ok.grid(row = 1, column = 0)
        
        cancel = tk.Button(upload_win, text = "Cancel", width = 20, command = upload_win.destroy)
        cancel.grid(row = 1, column = 1)
        upload_win.bind("<Return>", self.upload)
        
    def upload(self,event = None):
        #Makes plot and updates html-list and uploads them
        self.generate_html()
        self.make_plot()
        ssh = paramiko.SSHClient() 
        ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
        #password=getpass.getpass("Password: ")
        ssh.connect("lundsnaturvetarkar.se", username="root", password="Ue7$a4F[uLWbTEL9")
        sftp = ssh.open_sftp()
        #the url the list and plot is stored as the following
        sftp.put("list.html", "/var/www/lundsnaturvetarkar.se/quest_list.html")
        sftp.put("Points_plot.png", "/var/www/lundsnaturvetarkar.se/novisch_standings.png")
        sftp.close()
        ssh.close()
        self.confirm()
        self.upload_window.destroy()
     
    def confirm(self):
        
        tk.messagebox.showinfo("Uploaded", "Uploaded")
       
    def generate_html(self):
        #Reads quest list and html file
        if self.toggle_mode == 1:
            with open("quest_list.csv",'r', encoding="utf8") as f,open("list.html",'a', encoding="utf8") as html_file:
                    
                open("list.html", 'w', encoding="utf8").close()
                f.readline()
                for row in f:
                    split_row=row.split(";")#Divides quest list by ;
                    quest_owner=split_row[4][:-1] #Picks out quest owner
                    colors = {"lemur":"red","glufs":"turquoise","snys":"yellow","bug":"purple"}          
                    repetition=""
                    check_list = ["lemur","bug","glufs","snys"]
                    if(split_row[3]=="multiple"):#Sets the multiple times sign on the quests that can be repeated
                        repetition= "  ∞"
                    if(all(team in quest_owner for team in check_list) and split_row[3]!="multiple"):#Defines the colours for the teams
                        color="Black"
                        #if(quest_owner=="glufs"):
                        #    color="Turquoise"
                        #elif(quest_owner=="bug"):
                        #    color="Purple"
                        #elif(quest_owner=="snys"):
                        #    color="Orange"
                        #elif(quest_owner=="lemur"):
                        #    color="red"
                        line = '<p style="color: ' + color + ';"><strike>' +  split_row[0]+": "+split_row[1] + " " + split_row[2] + "p" + repetition +'</strike></p>'
                    elif(any(team in quest_owner.split(",")[:-1] for team in check_list) and split_row[3]!= "multiple"):
                            line = '<p>' + split_row[0] +": "+split_row[1] + " " + split_row[2] + "p "+ repetition + "Performed by "
                            for team_check in quest_owner.split(",")[:-1]:
                                if team_check == "lemur":
                                    name = "Lemur"
                                elif team_check == "bug":
                                    name = "BUG"
                                elif team_check == "glufs":
                                    name = "GLuFS"
                                elif team_check == "snys":
                                    name = "SNYS"
                                line=line+'<span style="color: ' + colors[team_check] + ';">'+" "+ name
                            line = line + "</p>"
                    else:
                        line = '<p>' + split_row[0]+": "+split_row[1] + " " + split_row[2] + "p"+ repetition + '</p>'
                    html_file.write(line)#Writes the line 
        elif self.toggle_mode == 0:
            with open("quest_list.csv",'r', encoding="utf8") as f,open("list.html",'a', encoding="utf8") as html_file:
                    
                open("list.html", 'w', encoding="utf8").close()
                f.readline()
                for row in f:
                    split_row=row.split(";")#Divides quest list by ;
                    quest_owner=split_row[4][:-1] #Picks out quest owner
                    #colors = {"lemur":"red","glufs":"turquoise","snys":"yellow","bug":"purple"}          
                    color="Black"
                    repetition=""
                    check_list = ["lemur","bug","glufs","snys"]
                    if(split_row[3]=="multiple"):#Sets the multiple times sign on the quests that can be repeated
                        repetition=" (Can be done by all teams!)"
                    if(quest_owner != "none" and split_row[3]!="multiple"):#Defines the colours for the teams
                        if(quest_owner=="glufs"):
                            color="Turquoise"
                        elif(quest_owner=="bug"):
                            color="Purple"
                        elif(quest_owner=="snys"):
                            color="Orange"
                        elif(quest_owner=="lemur"):
                            color="red"
                        line = '<p style="color: ' + color + ';"><strike>' +  split_row[0]+": "+split_row[1] + " " + split_row[2] + "p" + repetition +'</strike></p>'
                    else:
                        line = '<p>' + split_row[0]+": "+split_row[1] + " " + split_row[2] + "p"+ repetition + '</p>'
                    html_file.write(line)#Writes the line 
        else:
            tk.messagebox.showwarning(title = "Warning", message = "Please choose a mode")
    
    def make_plot(self, event = None):#Makes the plot
        with open("data.csv",'r', encoding="utf8") as f:
                f.readline()
                sum_list=[[],[],[],[]]
                time_list=[]
                i=0
                for row in f:
                        row_split = row.split(";")

                        glufs_entry = int(row_split[5])#Picks out the entries from the teams and sums them, could be done using sum command (don't know if faster)
                        bug_entry = int(row_split[6])
                        lemur_entry = int(row_split[7])
                        snys_entry = int(row_split[8])
                        time_entry = row_split[0]

                        if i==0:
                                sum_list[0].append(glufs_entry)
                                sum_list[1].append(bug_entry)
                                sum_list[2].append(lemur_entry)
                                sum_list[3].append(snys_entry)
                        else:
                                sum_list[0].append(glufs_entry+sum_list[0][i-1])
                                sum_list[1].append(bug_entry+sum_list[1][i-1])
                                sum_list[2].append(lemur_entry+sum_list[2][i-1])
                                sum_list[3].append(snys_entry+sum_list[3][i-1])

                        time_list.append(time_entry)
                        i=i+1
        
        day0=int(time_list[0].split(" ")[0].split("-")[1])*31+int(time_list[1].split(" ")[0].split("-")[2])#Sets the first day to be the first entry
        print(day0)

        time_list_fake=[]
        for entry in time_list:
                #If you want to plot using hours, takes (month number*31+day number)*24 to get hours and subtracts amount of hours at day0 and adds 12 hours 
                time_list_fake.append((int(entry.split(" ")[0].split("-")[1])*31+int(entry.split(" ")[0].split("-")[2]))*24+int(entry.split(" ")[1].split(":")[0])-day0*24+12)
                #Or days
                #time_list_fake.append((int(entry.split(" ")[0].split("-")[1])*31+int(entry.split(" ")[0].split("-")[2]))-day0)

        with plt.xkcd():#Simple plotting
                fig = plt.figure()
                plt.plot(time_list_fake,sum_list[0],color='xkcd:sky blue',label="GLuFS: "+str(sum_list[0][-1])+"p")
                plt.plot(time_list_fake,sum_list[1],color='xkcd:violet',label="BUG: "+str(sum_list[1][-1])+"p")
                plt.plot(time_list_fake,sum_list[2],color='xkcd:red',label="LEMUR: "+str(sum_list[2][-1])+"p")
                plt.plot(time_list_fake,sum_list[3],color='xkcd:yellow',label="SNYS: "+str(sum_list[3][-1])+"p")

                plt.legend()
                plt.xlabel('Time (hours after introductory meeting)')
                plt.ylabel('Points')
 
                fig.text(0.5, 0.95,'Points vs Time',ha='center')
                fig.set_figheight(9)
                fig.set_figwidth(16)
                fig.savefig("Points_plot.png")
        print("Plot Made")                
                
    def score(self, event = None):
        #Creates a window which displays the score
        with open("data.csv", "r", encoding="utf8") as f:
            f.readline()
            points=[[],[],[],[]]
            for row in f:
                row_split = row.split(";")
            
                glufs_entries = int(row_split[5])
                bug_entries = int(row_split[6])
                lemur_entries = int(row_split[7])
                snys_entries = int(row_split[8])
            
                points[0].append(glufs_entries)
                points[1].append(bug_entries)
                points[2].append(lemur_entries)
                points[3].append(snys_entries)

        glufs_points = sum(points[0])
        bug_points = sum(points[1])
        lemur_points = sum(points[2])
        snys_points = sum(points[3])
        
        
        win = self.score_win = tk.Toplevel()
        glufs = tk.Label(win, text = "GLuFS: ")
        glufs.grid(row = 0,column = 0)
        g_points = tk.Label(win, text = glufs_points)
        g_points.grid(row = 0, column = 1)
        
        bug = tk.Label(win, text = "BUG: ")
        bug.grid(row = 1,column = 0)
        b_points = tk.Label(win, text = bug_points)
        b_points.grid(row = 1, column = 1)
        
        lemur = tk.Label(win, text = "LEMUR: ")
        lemur.grid(row = 2,column = 0)
        l_points = tk.Label(win, text = lemur_points)
        l_points.grid(row = 2, column = 1)
        
        snys = tk.Label(win, text = "SNYS: ")
        snys.grid(row = 3,column = 0)
        s_points = tk.Label(win, text = snys_points)
        s_points.grid(row = 3, column = 1)
    
    def reset_window(self, event = None):
        #Creates a window which asks you if you really want to reset the data
        win = self.reset_window = tk.Toplevel()
        
        label = tk.Label(win, text = "Do you really want to reset?")
        label.pack(side = tk.TOP)
        
        yes = tk.Button(win, text = "Yes",width = 10, command = self.reset)
        yes.pack(side = tk.LEFT)
        
        no = tk.Button(win, text = "No", width = 10, command = win.destroy)
        no.pack(side = tk.LEFT)
    
    
    def reset(self, event = None):#Resets all data and clears the quest list
        open("data.csv", 'w', encoding="utf8").write("time;quest_number;quest_value;bonus;pitty_points;glufs;bug;lemur;snys")
        with open("quest_list.csv",'r', encoding="utf8") as f:
                temp_list=[]
                header = f.readline()
                temp_list.append(header)
                for row in f:
                        string = row.split(";")[:-1][0]+";"+row.split(";")[:-1][1]+";"+row.split(";")[:-1][2]+";"+row.split(";")[:-1][3]+";none\n"
                        temp_list.append(string)
        open("quest_list.csv",'w', encoding="utf8").close()
        write_quest_list = open("quest_list.csv",'a', encoding="utf8")
        for element in temp_list:
                write_quest_list.write(str(element))
        write_quest_list.close()
        self.reset_confirm()
        self.reset_window.destroy()
        
    def reset_confirm(self):
        
        tk.messagebox.showinfo("Reset", "Data Reset")
        
if __name__ == '__main__':#Used to run the program when executed and start the loop that runs the user interface
        PM()
