from math import fabs
import tkinter
from turtle import bgcolor
from Manager import Manager
from Food import Food
from Day import Day
from datetime import date
from tkinter import *
from tkinter.ttk import *

import os

manager = Manager()     
                               
currentDate = date.today()                              #Checking the Day
with open("date.txt", "r") as file:
    fileDateStr = file.read()
    fileDate = date.fromisoformat(fileDateStr)

if fileDate == currentDate:    
    day = Day()
    day.readCurrentNuts()
else:
    day = Day()
    with open("date.txt", "w") as file:
        file.write(currentDate.isoformat())
    day.clearCurrentNuts()


def updateBars():
    caloriesBar['value'] = (day.currentCalories/day.maxCalories)*100
    proteinBar['value'] = (day.currentProtein/day.maxProtein)*100
    fatBar['value'] = (day.currentFat/day.maxFat)*100
    carbsBar['value'] = (day.currentCarbs/day.maxCarbs)*100
    
    calCurLabl.config(text=str(day.currentCalories) + "/" + str(day.maxCalories))
    protCurLabl.config(text=str(day.currentProtein) + "/" + str(day.maxProtein))
    fatCurLabl.config(text=str(day.currentFat) + "/" + str(day.maxFat))
    carbCurLabl.config(text=str(day.currentCarbs) + "/" + str(day.maxCarbs))
    
    window.update_idletasks()
    
manager.readFoods()
day.readMaxNuts()
day.readCurrentNuts


if day.maxCalories == 0 or day.maxCarbs == 0 or day.maxProtein == 0 or day.maxFat == 0 or day.maxCarbs == 0:   
    print("Welcome to the Macro tracker. To start enter your macro goals/limits")
    day.changeGoal()

#BUTTON COMMANDS-------------------------------------------

def switchToEatFood():
    frameMainTop.pack_forget()
    frameMainBottom.pack_forget()
    for widget in frameEatFood.winfo_children():
        widget.destroy()
    roww = 0
    coll = 0
    for food in manager.foods:
        foodLabel = tkinter.Label(frameEatFood, text = food.name, bg = '#191b3e', fg = 'white', padx = 10, pady = 10)
        foodLabel.grid(row = roww, column = coll)
        eatButton = tkinter.Button(frameEatFood, text = 'Eat', bg = '#671ea0', fg = 'white', padx = 10, command=lambda f=food, r=roww: eat(f, r))
        eatButton.grid(row = roww, column = coll+1)
        roww = roww + 1
        
    eatToMain = tkinter.Button(frameEatFood, text = 'Back', command = backFromEat, bg = '#191b3e', fg = 'white', padx = 10, pady = 5)
    eatToMain.grid(row = roww+1, column = 0)
    frameEatFood.pack()

def switchToAddFood():
    frameMainTop.pack_forget()
    frameMainBottom.pack_forget()
    frameAddFood.pack()

def switchToChangeMaxNuts():
    frameMainTop.pack_forget()
    frameMainBottom.pack_forget()
    frameChangeGoal.pack()

def changeMaxNuts():
    mCal = caloriesMaxEntry.get()
    mProtein = proteinMaxEntry.get()
    mFat = fatMaxEntry.get()
    mCarb = carbMaxEntry.get()
    day.changeGoal(mCal, mProtein, mFat, mCarb)
 

def submitAddFood():
    name = nameEntry.get()
    cal = caloriesEntry.get()
    protein = proteinEntry.get()
    fat = fatEntry.get()
    carb = carbEntry.get()
    manager.addFood(name, cal, protein, fat, carb)
    

def eat(food, row):
    day.eatFood(food)
    print("Eating from row" + str(row))
    print(day.currentCalories)
    print(day.currentProtein)
    print(day.currentFat)
    print(day.currentCarbs)

def backFromEat():
    frameEatFood.pack_forget()
    frameMainTop.pack()
    frameMainBottom.pack()
    updateBars()
    
def backFromChangeGoals():
    frameChangeGoal.pack_forget()
    frameMainTop.pack()
    frameMainBottom.pack()
    updateBars()

def backFromAdd():
    frameAddFood.pack_forget()
    frameMainTop.pack()
    frameMainBottom.pack()
    updateBars()

def exitWindow():
    window.destroy()

#GUI---------------------------------

window = Tk()
window.geometry("500x500")
window.config(background = '#191b3e')

frameMainTop = tkinter.Frame(window, bg = '#191b3e')
frameMainBottom = tkinter.Frame(window, bg = '#191b3e')
frameAddFood = tkinter.Frame(window, bg = '#191b3e')
frameEatFood = tkinter.Frame(window, bg = '#191b3e')
frameChangeGoal = tkinter.Frame(window, bg = '#191b3e')

frameMainTop.pack()
frameMainBottom.pack()
frameAddFood.pack_forget()
frameEatFood.pack_forget()

#MAIN -----------------------------------------------------

#Labels 
caloriLabl = tkinter.Label(frameMainTop, text = 'Calories', bg = '#191b3e', fg = 'white', padx = 5)
caloriLabl.grid(row = 0, column = 0)
protLabl = tkinter.Label(frameMainTop, text = 'Protein', bg = '#191b3e', fg = 'white', padx = 5)
protLabl.grid(row = 1, column = 0)
fatLabl = tkinter.Label(frameMainTop, text = 'Fat', bg = '#191b3e', fg = 'white', padx = 5)
fatLabl.grid(row = 2, column = 0)
carbLabl = tkinter.Label(frameMainTop, text = 'Carbohydrates', bg = '#191b3e', fg = 'white', padx = 5)
carbLabl.grid(row = 3, column = 0)

#Bars
caloriesBar = Progressbar(frameMainTop, orient=HORIZONTAL, length = 300)
caloriesBar.grid(row = 0, column = 1)
proteinBar = Progressbar(frameMainTop, orient=HORIZONTAL, length = 300)
proteinBar.grid(row = 1, column = 1)
fatBar = Progressbar(frameMainTop, orient=HORIZONTAL, length = 300)
fatBar.grid(row = 2, column = 1)
carbsBar = Progressbar(frameMainTop, orient=HORIZONTAL, length = 300)
carbsBar.grid(row = 3, column = 1)

#Numbers
calCurLabl = tkinter.Label(frameMainTop, text = str(day.currentCalories) + "/" + str(day.maxCalories), bg = '#191b3e', fg = 'white', padx = 5)
calCurLabl.grid(row = 0, column = 2)
protCurLabl = tkinter.Label(frameMainTop, text = str(day.currentProtein) + "/" + str(day.maxProtein), bg = '#191b3e', fg = 'white', padx = 5)
protCurLabl.grid(row = 1, column = 2)
fatCurLabl = tkinter.Label(frameMainTop, text = str(day.currentFat) + "/" + str(day.maxFat), bg = '#191b3e', fg = 'white', padx = 5)
fatCurLabl.grid(row = 2, column = 2)
carbCurLabl = tkinter.Label(frameMainTop, text = str(day.currentCarbs) + "/" + str(day.maxCarbs), bg = '#191b3e', fg = 'white', padx = 5)
carbCurLabl.grid(row = 3, column = 2)

#Buttons
eatFoodButton = tkinter.Button(frameMainBottom,text = 'Eat Food', bg = '#191b3e', fg = 'white', command = switchToEatFood).grid(row = 5, column = 0, padx = 10, pady = 10)
addFoodButton = tkinter.Button(frameMainBottom,text = 'Add Food', bg = '#191b3e', fg = 'white', command = switchToAddFood).grid(row = 5, column = 1, padx = 10, pady = 10)
changeMaxNutsButton = tkinter.Button(frameMainBottom, text = 'Change Macro Goals', fg = 'white', bg = '#191b3e', command = switchToChangeMaxNuts).grid(row = 5, column = 2, padx = 10, pady = 10)
exitButton = tkinter.Button(frameMainBottom, text = 'Exit', bg = '#191b3e', fg = 'white', command = exitWindow).grid(row = 5, column = 3, padx = 10, pady = 10)
updateBars()

#ADD FOOD ----------------------------------------------

nameLabel = tkinter.Label(frameAddFood, text = 'Name', bg = '#191b3e', fg = 'white')
nameLabel.grid(row = 0, column = 0)
nameEntry = tkinter.Entry(frameAddFood)
nameEntry.grid(row = 0, column = 1)
caloriesLabel = tkinter.Label(frameAddFood, text = 'Calories', bg = '#191b3e', fg = 'white')
caloriesLabel.grid(row = 1, column = 0)
caloriesEntry = tkinter.Entry(frameAddFood)
caloriesEntry.grid(row = 1, column = 1)
proteinLabel = tkinter.Label(frameAddFood, text = 'Protein', bg = '#191b3e', fg = 'white')
proteinLabel.grid(row = 2, column = 0)
proteinEntry = tkinter.Entry(frameAddFood)
proteinEntry.grid(row = 2, column = 1)
fatLabel = tkinter.Label(frameAddFood, text = 'Fat', bg = '#191b3e', fg = 'white')
fatLabel.grid(row = 3, column = 0)
fatEntry = tkinter.Entry(frameAddFood)
fatEntry.grid(row = 3, column = 1)
carbLabel = tkinter.Label(frameAddFood, text = 'Carbohydrates', bg = '#191b3e', fg = 'white')
carbLabel.grid(row = 4, column = 0)
carbEntry = tkinter.Entry(frameAddFood)
carbEntry.grid(row = 4, column = 1)

submit = tkinter.Button(frameAddFood, text = 'Submit', command = submitAddFood, bg = '#191b3e', fg = 'white', padx = 10, pady = 5)
submit.grid(row = 5, column = 1)

addToMain = tkinter.Button(frameAddFood, text = 'Back', command = backFromAdd, bg = '#191b3e', fg = 'white', padx = 10, pady = 5)
addToMain.grid(row = 5, column = 0)

#CHANGE GOALS -------------------------------------------------------------

caloriesMaxLabel = tkinter.Label(frameChangeGoal, text = 'Max Calories', bg = '#191b3e', fg = 'white', padx = 10, pady = 5)
caloriesMaxLabel.grid(row = 1, column = 0)
caloriesMaxEntry = tkinter.Entry(frameChangeGoal)
caloriesMaxEntry.grid(row = 1, column = 1, padx = 10, pady = 5)
proteinMaxLabel = tkinter.Label(frameChangeGoal, text = 'Max Protein', bg = '#191b3e', fg = 'white')
proteinMaxLabel.grid(row = 2, column = 0)
proteinMaxEntry = tkinter.Entry(frameChangeGoal)
proteinMaxEntry.grid(row = 2, column = 1, padx = 10, pady = 5)
fatMaxLabel = tkinter.Label(frameChangeGoal, text = 'Max Fat', bg = '#191b3e', fg = 'white')
fatMaxLabel.grid(row = 3, column = 0)
fatMaxEntry = tkinter.Entry(frameChangeGoal)
fatMaxEntry.grid(row = 3, column = 1, padx = 10, pady = 5)
carbMaxLabel = tkinter.Label(frameChangeGoal, text = 'Max Carbohydrates', bg = '#191b3e', fg = 'white')
carbMaxLabel.grid(row = 4, column = 0)
carbMaxEntry = tkinter.Entry(frameChangeGoal)
carbMaxEntry.grid(row = 4, column = 1, padx = 10, pady = 5)

ChangeGoalsButton = tkinter.Button(frameChangeGoal, text = 'Change Goals', command = changeMaxNuts, bg = '#191b3e', fg = 'white', padx = 10, pady = 5)
ChangeGoalsButton.grid(row = 5, column = 1)

changeGoalsToMain = tkinter.Button(frameChangeGoal, text = 'Back', command = backFromChangeGoals, bg = '#191b3e', fg = 'white', padx = 10, pady = 5)
changeGoalsToMain.grid(row = 5, column = 0)

#---------------------------------------------------------------


window.mainloop()

