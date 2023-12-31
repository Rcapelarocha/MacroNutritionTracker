#manages the list of foods that can be eaten in a day

from Food import Food


class Manager():
    

    def __init__(self):
        self.foods = []
    
    def addFood(self, newName, calories, prot, fat, carb):
        if not(newName.isalpha()) or not(calories.isdigit()) or not(prot.isdigit()) or not(fat.isdigit()) or not(carb.isdigit()):
            print("Incorrect Arguments")
            return
        for food in self.foods:
            if food.name == newName:
                print("food already exists")
                return 
            
        self.foods.append(Food(newName, calories, prot, fat, carb))
        with open("foods.txt", "a") as file:
            file.write(newName + " " + str(calories) + " " + str(prot) + " " + str(fat) + " " + str(carb) + "\n")     #save foods in foods.txt



    def removeFood(self, food):
        self.foods.remove(food)

        with open("foods.txt", "w") as file:
            for food in self.foods:
                file.write(food.name + " " + str(food.calories) + " " + str(food.protein) + " " + str(food.fat) + " " + str(food.carbs) + "\n")     #save foods in foods.txt


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