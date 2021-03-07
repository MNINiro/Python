# Instance Methods:
#     Accesor Methods
#     Mutator Methods
# Class Methods
# Static Methods

# #===Ex-1===
# Instance method without parameter
class Mobile:
    #instance method
    def showModel(self):
        print("RealMe X")

x = Mobile()
x.showModel()

#===Ex-2===
#Instance method with parameter
class Mobile1:
    def __init__(self):
        self.model = 'Xiaomi'

    # instance method
    def showModel(self,p):
        self.price = p
        print(f"Model {self.model} and it's price is {self.price}")

print('Before changing price')
x = Mobile1()
x.showModel(10000)
print()

print('After changing price')
y = Mobile1()
y.showModel(20000) #here, only price will be changed, not the model since we did not modify model anywhere

