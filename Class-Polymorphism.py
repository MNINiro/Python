class Animal:
    def Name(self):
        print('animal')
    
    def Sleep(self):
        print("Sleep")

    def MakeNoise(self):
        pass

class Dog(Animal):
    def Name(self):
        print("It's a dog")

    def MakeNoise(self): # it's a overwritten method of MakeNoise method of Animal class 
        print("Woof!")

class Cat(Animal):
    def Name(self):
        print("It's a cat")

    def MakeNoise(self):
        print("Meaw!")

class Lion(Animal):
    def Name(self):
        print("It's a Lion")

    def MakeNoise(self):
        print("Roar!")

class TestAnimals:
    def PrintName(self,animal):
        animal.Name()
        
    def GoToSleep(self,animal):
        animal.Sleep() # Sleep mathod has not been overwritten. So, it will write "Sleep"
        
    def MakeNoise(self,animal):
        animal.MakeNoise()

TestAnimals = TestAnimals()
dog = Dog()
cat = Cat()
lion = Lion()

TestAnimals.PrintName(dog)
TestAnimals.GoToSleep(dog)
TestAnimals.MakeNoise(dog)

TestAnimals.PrintName(cat)
TestAnimals.GoToSleep(cat)
TestAnimals.MakeNoise(cat)

TestAnimals.PrintName(lion)
TestAnimals.GoToSleep(lion)
TestAnimals.MakeNoise(lion)
