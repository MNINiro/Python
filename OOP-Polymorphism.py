class Animal:
    def Name(self):
        print('animal')

    def Sleep(self):
        print("Sleep")

    def MakeNoise(self):
        pass


class Dog(Animal):
    def Name(self):  # Method overriding
        print("It's a dog")

    def MakeNoise(self):  # it's an overwritten method of MakeNoise method of Animal class
        print("Woof!")


class Cat(Animal):
    def Name(self):
        print("It's a cat")

    def Sleep(self):
        print("it is Sleeping")

    def MakeNoise(self):
        print("Meaw!")


class Lion(Animal):
    def Name(self):
        print("It's a Lion")

    def MakeNoise(self):
        print("Roar!")


class TestAnimals:
    def PrintName(self, animal):
        animal.Name()

    def GoToSleep(self, animal):
        animal.Sleep()  # Sleep method has not been overwritten. So, it will write "Sleep"

    def MakeNoise(self, animal):
        animal.MakeNoise()


# Instances
TA = TestAnimals()
dog = Dog()
cat = Cat()
lion = Lion()

TA.PrintName(dog)
TA.GoToSleep(dog)
# TA.MakeNoise(dog)

TA.PrintName(cat)
# TA.GoToSleep(cat)
# TA.MakeNoise(cat)
#
TA.PrintName(lion)
# TA.GoToSleep(lion)
# TA.MakeNoise(lion)
