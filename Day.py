

class Day():
    
    maxCalories = 0
    maxProtein = 0
    maxFat = 0
    maxCarbs = 0
    eatenFoods = []
        
    def __init__(self):
        
        self.currentCalories = 0
        self.currentProtein = 0
        self.currentFat = 0
        self.currentCarbs = 0

    
    def eatFood(self, food):
        self.currentCalories += int(food.calories)
        self.currentProtein += int(food.protein)
        self.currentFat += int(food.fat)
        self.currentCarbs += int(food.carbs)
        self.eatenFoods.append(food.name)
        with open("currentNuts.txt", "w") as file:
            file.write(str(self.currentCalories) + " " + str(self.currentProtein) + " " + str(self.currentFat) + " " + str(self.currentCarbs))
    


    def changeGoal(self, mCal, mProt, mFat, mCarb):
        self.maxCalories = int(mCal)
        self.maxProtein = int(mProt)
        self.maxFat = int(mFat)
        self.maxCarbs = int(mCarb)
        with open("maxNuts.txt", "w") as file:
            file.write(str(self.maxCalories) + " " + str(self.maxProtein) + " " + str(self.maxFat) + " " + str(self.maxCarbs))
    
    def showEatenFoods(self):
        for food in self.eatenFoods:
            print(food)
            

    def readCurrentNuts(self):
        with open("currentNuts.txt", "r") as file:
            line = file.readline()
            
        if line:
            values = line.split()
            if len(values) == 4:
                self.currentCalories = int(values[0])
                self.currentProtein = int(values[1])
                self.currentFat = int(values[2])
                self.currentCarbs = int(values[3])
            else:
                print("Invalid number of values")
            
    def clearCurrentNuts(self):
        with open("currentNuts.txt", "w") as file:
            file.write("")
                
    def readMaxNuts(self):
        with open("maxNuts.txt", "r") as file:
            line = file.readline()
            
        if line:
            values = line.split()
            if len(values) == 4:
                self.maxCalories = int(values[0])
                self.maxProtein = int(values[1])
                self.maxFat = int(values[2])
                self.maxCarbs = int(values[3])
            else:
                print("Invalid number of values")
            
