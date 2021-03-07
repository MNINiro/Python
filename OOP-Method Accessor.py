#Accessor or getter method
# #=== Ex-1 === accessor method
# class Mobile:
#     def __init__(self):
#         self.model = 'RealMe X'
#
#     def getModel(self):     #accessor method
#         return self.model
#
# x = Mobile()
# print(x.getModel())
#
# m = x.getModel()
# print(m)

# #=== Ex-2 === Setter Method without parameter
# class Mobile1:
#     def __init__(self):
#         self.model = 'iPhone'
#
#     def setModel(self):     #mutator/setter method will replace original model
#         self.model = "Galaxy"
#
# x = Mobile1() #instance
#
# print("Before setting")
# print(x.model)
#
# print("After setting")
# x.setModel()
# print(x.model)

# #=== Ex-3 ===
class Mobile3:
    def __init__(self):
        self.model = 'iPhone'

    def setModel(self,m): #setter method with parameter
        self.model = m

x = Mobile3()
print(x.model)

x.setModel('Nokia')
print(x.model)
