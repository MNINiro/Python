class Person:
       def speak(self):
              print('I can speak')

class Man(Person):          # Man  is a subclass of Person class
       def wear(self):
              print('I wear shirt')

class Women(Person):        # Class Person is a super class
       def wear(self):
              print('I wear skirt')


m = Man()
m.wear()
m.speak()   ## Class Man inherits
              ## Class Person, and invoke speak() method
              ## In Class Person

Women().wear() #without creating instance
Women().speak()
