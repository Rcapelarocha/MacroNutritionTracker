from math import fabs
from Manager import Manager
from Food import Food
from Day import Day
from datetime import date
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
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

#Button Commands------------------

def switchToEatFood():
    frameMain.pack_forget()
    for widget in frameEatFood.winfo_children():
        widget.destroy()
    roww = 0
    coll = 0
    for food in manager.foods:
        foodLabel = Label(frameEatFood, text = food.name)
        foodLabel.grid(row = roww, column = coll)
        eatButton = Button(frameEatFood, text = 'Eat',command=lambda f=food, r=roww: eat(f, r))
        eatButton.grid(row = roww, column = coll+1)
        roww = roww + 1
        
    eatToMain = Button(frameEatFood, text = 'Back', command = backFromEat)
    eatToMain.grid(row = roww+1, column = 0)
    frameEatFood.pack()

def switchToAddFood():
    frameMain.pack_forget()
    frameAddFood.pack()

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
    frameMain.pack()
    updateBars()
    

def backFromAdd():
    frameAddFood.pack_forget()
    frameMain.pack()
    updateBars()
    

#GUI---------------------------------

window = Tk()
window.geometry("500x500")

frameMain = Frame(window)
frameAddFood = Frame(window)
frameEatFood = Frame(window)

frameMain.pack()
frameAddFood.pack_forget()
frameEatFood.pack_forget()

#main

caloriLabl = Label(frameMain, text = 'Calories')
caloriLabl.grid(row = 0, column = 0)
protLabl = Label(frameMain, text = 'Protein')
protLabl.grid(row = 1, column = 0)
fatLabl = Label(frameMain, text = 'Fat')
fatLabl.grid(row = 2, column = 0)
carbLabl = Label(frameMain, text = 'Carbohydrates')
carbLabl.grid(row = 3, column = 0)


caloriesBar = Progressbar(frameMain, orient=HORIZONTAL, length = 300)
caloriesBar.grid(row = 0, column = 1)
proteinBar = Progressbar(frameMain, orient=HORIZONTAL, length = 300)
proteinBar.grid(row = 1, column = 1)
fatBar = Progressbar(frameMain, orient=HORIZONTAL, length = 300)
fatBar.grid(row = 2, column = 1)
carbsBar = Progressbar(frameMain, orient=HORIZONTAL, length = 300)
carbsBar.grid(row = 3, column = 1)

calCurLabl = Label(frameMain, text = str(day.currentCalories) + "/" + str(day.maxCalories))
calCurLabl.grid(row = 0, column = 2)
protCurLabl = Label(frameMain, text = str(day.currentProtein) + "/" + str(day.maxProtein))
protCurLabl.grid(row = 1, column = 2)
fatCurLabl = Label(frameMain, text = str(day.currentFat) + "/" + str(day.maxFat))
fatCurLabl.grid(row = 2, column = 2)
carbCurLabl = Label(frameMain, text = str(day.currentCarbs) + "/" + str(day.maxCarbs))
carbCurLabl.grid(row = 3, column = 2)

eatFoodButton = Button(frameMain,text = 'Eat Food', command = switchToEatFood).grid(row = 4, column = 0)
addFoodButton = Button(frameMain,text = 'Add Food', command = switchToAddFood).grid(row = 4, column = 1)
updateBars()

#Add Food

nameLabel = Label(frameAddFood, text = 'Name')
nameLabel.grid(row = 0, column = 0)
nameEntry = Entry(frameAddFood)
nameEntry.grid(row = 0, column = 1)
caloriesLabel = Label(frameAddFood, text = 'Calories')
caloriesLabel.grid(row = 1, column = 0)
caloriesEntry = Entry(frameAddFood)
caloriesEntry.grid(row = 1, column = 1)
proteinLabel = Label(frameAddFood, text = 'Protein')
proteinLabel.grid(row = 2, column = 0)
proteinEntry = Entry(frameAddFood)
proteinEntry.grid(row = 2, column = 1)
fatLabel = Label(frameAddFood, text = 'Fat')
fatLabel.grid(row = 3, column = 0)
fatEntry = Entry(frameAddFood)
fatEntry.grid(row = 3, column = 1)
carbLabel = Label(frameAddFood, text = 'Carbohydrates')
carbLabel.grid(row = 4, column = 0)
carbEntry = Entry(frameAddFood)
carbEntry.grid(row = 4, column = 1)

submit = Button(frameAddFood, text = 'Submit', command = submitAddFood)
submit.grid(row = 5, column = 1)

addToMain = Button(frameAddFood, text = 'Back', command = backFromAdd)
addToMain.grid(row = 5, column = 0)
#---------------------------


window.mainloop()

