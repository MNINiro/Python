# #=== Ex-1 ===
# class Mobile:
#     fp = "yes"
#
# x = Mobile()    #Instance created
# y = Mobile()
# print(x.fp)     #Accessing to class variable and print
# print(y.fp)
#
# Mobile.fp = "No"    #changed class variable
# print(x.fp)         #all instances have been changed
# print(y.fp)
#
# x.fp = "Not working"    #only x instance value has been changed
# print(x.fp)             # it will show new output
# print(y.fp)             #but it will show previously modified output, No

#=== Ex-2 ===
class Mobile:
    fp = "Yes"      #It's a class variable

    # @classmethod    #It's a classmethod
    # def isfp(cls):  # classmethod must use cls to access class variable
    #     print("Finger print:",cls.fp)

iPhone = Mobile()         # creating instance
Galaxy = Mobile()
Nokia = Mobile()
#
# #original class variable will be printed, Yes
print("Class FP:", Mobile.fp)
print("Class FP:", iPhone.fp)
print("Class FP:", Galaxy.fp)
print("Class FP:", Nokia.fp)
print()

#Modified class variable will be displayed, No
Mobile.fp = "No"            #class namespace variable changed
print("Class FP:", Mobile.fp)
print("Class FP:", iPhone.fp)
print("Class FP:", Galaxy.fp)
print("Class FP:", Nokia.fp)
print()
#
#Only one instance has been modified. Rest of them remain as it was
iPhone.fp = "Not working"   #Object namespace variable has been changed
print("Class FP:", Mobile.fp)
print("Class FP:", iPhone.fp)
print("Class FP:", Galaxy.fp)
print("Class FP:", Nokia.fp)

