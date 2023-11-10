#manages the list of foods that can be eaten in a day

from Food import Food


class Manager():
    

    def __init__(self):
        self.foods = []
    
    def addFood(self, newName, calories, fat, prot, carb):
        for food in self.foods:
            if food.name == newName:
                print("food already exists")
                return 
            
        self.foods.append(Food(newName, calories, fat, prot, carb))
        with open("foods.txt", "a") as file:
            file.write(newName + " " + str(calories) + " " + str(fat) + " " + str(prot) + " " + str(carb) + "\n")     #save foods in foods.txt



    def removeFood(self, food):
        self.foods.remove(food)


    def readFoods(self):
        with open("foods.txt", "r") as file:
             lines = file.readlines()
             for line in lines:
                data = line.strip().split()  # Split the line into separate values
                if len(data) == 5:
                    name, calories, prot, fat, carb = data
                    # Convert the relevant fields to appropriate data types (e.g., int or float)
                    calories, prot, fat, carb = int(calories),int(prot) ,int(fat) , int(carb)
                    # Create a Food object and add it to the list
                    self.foods.append(Food(name, calories, fat, prot, carb))
                    

    def printFoods(self):
        print()
        for food in self.foods:
            print(food.toString())