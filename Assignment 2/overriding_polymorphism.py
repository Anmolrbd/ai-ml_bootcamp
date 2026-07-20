class Animal:
    def __init__(self,name):
        self.name = name
    
    def make_sound(self):
        print("Some generic animal sound!!")

    
class Dog(Animal):

    def __init__(self, name,breed):
        super().__init__(name)
        self.breed = breed
    
    def make_sound(self):
        print(f"{self.name} says: WOOF!!")
    
class Cat(Animal):
    def __init__(self,name,color):
        super().__init__(name)
        self.color = color
    
    def make_sound(self):
        print(f"{self.name} says: MEOW!!")
 
class Cow(Animal):
    def __init__(self,name,weight):
        super().__init__(name)
        self.weight = weight
    
    def make_sound(self):
        print(f"{self.name} says: MOOOO!!")
 
dog = Dog("Buddy","German Shephard")
cat = Cat("Lilly","Brown")
cow = Cow("Bella",120)

animals = [dog,cat,cow]

for animal in animals:
    animal.make_sound()