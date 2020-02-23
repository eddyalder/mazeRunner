#import mainEdward
import pygame
import os
import tkinter as tk
from tkinter import *
import tkinter.font as font
from tkinter import ttk

directory = os.getcwd()
print(directory)
def main():
    root = Tk()
    app = Title_Screen(root)

class Title_Screen:
    def __init__(self, master):
        self.master = master
        self.master.title("Maze Runner")
        self.master.geometry('1920x1080')

        self.titleFont = font.Font(size = 30)

        self.image = PhotoImage(file = directory + r'\maze.png')
        self.background = Label(self.master, image = self.image)
        self.background.pack()
        self.title = Label(self.master, text = "Maze Runner", bg = '#3366cc')
        self.title.place(relx = 0.25, rely = 0, relwidth = 0.5, relheight = 0.15)
        self.title['font'] = self.titleFont

        self.play = Button(self.master, text = "Play", bg = '#3366cc', command  = self.play_select_system)
        self.play.place(relx = 0.45, rely = 0.5, relwidth = 0.1, relheight = 0.05)

        self.scoreboard = Button(self.master, text = "Scoreboard", bg = '#3366cc')
        self.scoreboard.place(relx = 0.45, rely = 0.55, relwidth = 0.1, relheight = 0.05)

        self.credit = Button(self.master, text = "Credits", bg = '#3366cc',)
        self.credit.place(relx = 0.45, rely = 0.6, relwidth = 0.1, relheight = 0.05)

    def play_select_system(self):
        self.master.destroy()
        self.master = Tk()
        self.app = difficulty_select(self.master)
        self.master.mainloop()

class difficulty_select:
    def callGame(self):
        import mainEdward
        #call = 'C:\\Users\\eddya\\Documents\\Code Workspace\\mazeRunner\\mainEdward.py'
        #exec(open(call).read())
        #exec(r'C:\Users\eddya\Documents\Code Workspace\mazeRunner\mainEdward.py')

    def __init__(self, master):
        self.master = master
        self.master.title("Difficulty Selecter")
        self.master.geometry('1920x1080')

        self.titleFont = font.Font(size = 30)

        self.image = PhotoImage(file = directory + r'\maze.png')
        self.background = Label(self.master, image = self.image)
        self.background.pack()
        self.title = Label(self.master, text = "Select A Difficulty", bg = '#3366cc')
        self.title.place(relx = 0.25, rely = 0, relwidth = 0.5, relheight = 0.15)
        self.title['font'] = self.titleFont

        self.easy = Button(self.master, text = "Easy", bg = '#3366cc', command = self.easy_select_system)
        self.easy.place(relx = 0.45, rely = 0.5, relwidth = 0.1, relheight = 0.05)

        self.medium = Button(self.master, text = "Medium", bg = '#3366cc', command = self.medium_select_system)
        self.medium.place(relx = 0.45, rely = 0.55, relwidth = 0.1, relheight = 0.05)

        self.hard = Button(self.master, text = "Hard", bg = '#3366cc', command = self.hard_select_system)
        self.hard.place(relx = 0.45, rely = 0.6, relwidth = 0.1, relheight = 0.05)
    
    def easy_select_system(self):
        self.master.destroy()
        with open("diffOut.txt", "w") as outFile:
            outNum = "1"
            outFile.write(outNum)
        self.callGame()
    
    def medium_select_system(self):
        self.master.destroy()
        with open("diffOut.txt", "w") as outFile:
            outNum = "2"
            outFile.write(outNum)
        self.callGame()

    def hard_select_system(self):
        self.master.destroy()
        with open("diffOut.txt", "w") as outFile:
            outNum = "3"
            outFile.write(outNum)
        self.callGame()

if __name__=='__main__':
    root = Tk()
    application = Title_Screen(root)
    root.mainloop()