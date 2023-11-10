

class Food():
      
    def __init__(self,name, calories, protein, fat, carbs):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carbs = carbs


    def toString(self):
        return self.name.upper() + "    Calories: " + str(self.calories) + " cals    Protein: " + str(self.protein) + "g    Fat: " + str(self.fat) + "g    Carbohydrates: " + str(self.carbs) +"g"
     




