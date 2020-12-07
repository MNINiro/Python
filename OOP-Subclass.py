# #=== Ex-1 ===
# class Child():
# 	def __init__(self,name):
# 		self.name = name
#
# class Student(Child):
# 	def __init__(self,name,roll):
# 		self.roll = roll
# 		Child.__init__(self,name)
#
# a = Child("xyz")
# print(a.name)
# b = Student("abc",12)
# print(b.name)
# print(b.roll)

# #=== Ex-2 ===
# class Child():
# 	def __init__(self,name):
# 		self.name = name
# class Student(Child):
# 	pass
# a = Child("xyz")
# print(a.name)
# b = Student("abc")
# print(b.name)

#=== Ex-3 ===
class Rectangle():
	def __init__(self,leng,br):
		self.length = leng
		self.breadth = br
	'''while calling a method in a class python	automatically passes an instance( object ) of it.
	   so we have to pass sef in area i.e. area(self)'''

	def area(self):
		'''length and breadth are not globally defined.
		So, we have to access them as self.length'''
		return self.length * self.breadth

class Square(Rectangle):
	def __init__(self,side):
		Rectangle.__init__(self,side,side)
		self.side = side

s = Square(4)
print(s.length)
print(s.breadth)
print(s.side)
print(s.area())# It appears as nothing is passed but python will pass an instance of class.

