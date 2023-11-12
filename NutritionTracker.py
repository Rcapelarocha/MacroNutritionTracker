from Manager import Manager
from Food import Food
from Day import Day
from datetime import date
from tkinter import *
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


def printCurrentNuts():
    print("Calories: " + str(day.currentCalories) + "/" + str(day.maxCalories))
    print("Protein: " + str(day.currentProtein) + "/" + str(day.maxProtein))
    print("Fat: " + str(day.currentFat) + "/" + str(day.maxFat))
    print("Carbohydrates: " + str(day.currentCarbs) + "/" + str(day.maxCarbs))
    


manager.readFoods()
day.readMaxNuts()
day.readCurrentNuts

if day.maxCalories == 0 or day.maxCarbs == 0 or day.maxProtein == 0 or day.maxFat == 0 or day.maxCarbs == 0:   
    print("Welcome to the Macro tracker. To start enter your macro goals/limits")
    day.changeGoal()

#Button Commands------------------

def switchToEatFood():
    frameMain.pack_forget()
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

def eat():
    pass

def backFromEat():
    frameEatFood.pack_forget()
    frameMain.pack()

def backFromAdd():
    frameAddFood.pack_forget()
    frameMain.pack()

#GUI---------------------------------

window = Tk()
window.geometry("420x420")

frameMain = Frame(window)
frameAddFood = Frame(window)
frameEatFood = Frame(window)

frameMain.pack()
frameAddFood.pack_forget()
frameEatFood.pack_forget()

#main

eatFoodButton = Button(frameMain,text = 'Eat Food', command = switchToEatFood).pack()
addFoodButton = Button(frameMain,text = 'Add Food', command = switchToAddFood).pack()

#Eat Food
roww = 0
coll = 0
for food in manager.foods:
    foodLabel = Label(frameEatFood, text = food.name)
    foodLabel.grid(row = roww, column = coll)
    eatButton = Button(frameEatFood, text = 'Eat', command = eat)
    eatButton.grid(row = roww, column = coll+1)
    roww = roww + 1
    
eatToMain = Button(frameEatFood, text = 'Back', command = backFromEat)
eatToMain.grid(row = roww+1, column = 0)

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

