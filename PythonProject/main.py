#This is the main module
# import calc

# print("Calc module variable:",calc.a)
#
# print("Addition :", calc.add(10,15))
# print("Addition :", calc.add(calc.a,15))
#
# ma = calc.a
# print("Addition :",calc.add(ma,25))
#
# mb = calc.a + 20
# print("Addition :",calc.add(mb,15))

# #==================================
# print("subtraction :",calc.sub(15,5))
# b = calc.sub(20,15)
# print("Subtraction",b)
#
# print("Multiplication :",calc.mult(10,15))
# print("Real Division :",calc.div(20,10))
# print("Integer Division :",calc.intDiv(20,15))

#====================================
# from calc import a, name, add #importing specific functions
#
# name()
# print(a)
#
# x = int(input("Enter 1st value:"))
# y = int(input("Enter 2nd value:"))
#
# a = add(x,y)
# print(a)

#====================================
# import calc as c #alias
# from calc import add as s, name as n
#
# print(c.a)
# print(s(10,10))
# print(n())
# #
# #====================================
# from calc import *
#
# print(add(10,10))
# add(10,10)
# print(name())

#====================================
# import first as f, second as s
#
# print(f.a)
# print(s.a)
#
# print(f.name())
# print(s.name())

# #====================================
# from first import a,name
# from second import a,name
# print(a) #in this case, it will print only second module's a since it is the recent one that was called.
# name();
#
# #====================================
# from first import a,name,tup
# print(a) #in this case, it will print first module's a since it is the recent one that was called.
# name()
#
# from second import a,name
# print(a) #in this case, it will print only second module's a since it is the recent one that was called.
# name();

#====================================
# import classes as cl
#
# c = cl.MyClass()
# c.name()
# # c.maths()
#
# s = cl.MySchool()
# s.show()
#
# #====================================
# from classes import MyClass as mc, MySchool as ms
#
# c = mc()
# c.name()
#
# s = ms()
# s.show()

# #====================================
# from classes import *
#
# mc = MyClass()
# ms = MySchool()
#
# mc.name()
# ms.show()
#
# #====================================
# import first, second, classes as cl
#
# c = second.MyCollege()  #creating instance then
# c.display()             #calling method
# second.name()           #here, calling a method that is not in a class
#
# first.name()            #calling a method from first module
#
# x = cl.MyClass()        #creating instance then
# x.name()                #calling method
# y = cl.MySchool()
# y.show()

#====================================
# from second import MyCollege,MyClass as mc
# from classes import MySchool,MyClass
#
# c = MyCollege()         #creating instance then
# c.display()             #calling a method
# #second.name()          #It will show an error since it has not been imported
#
# d = MyClass()
# d.name()
#
# e = MyClass()           #both d and e instances will display output from classes module
# e.name()
#
# f = mc()                #to solve above replacement problem, an alias mc has been used for second module
# f.name()
#
# x = MyClass()
# x.name()
#
# y = MySchool()
# y.show()

