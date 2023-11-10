from Manager import Manager
from Food import Food
from Day import Day
from datetime import date
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






