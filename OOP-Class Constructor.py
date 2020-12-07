class person:
##       def __init__(self,name):
##              self.name = name
##              print(self.name)
              

       def __init__(self,age):
              self.age = age
              print(self.age)


## From the code , we can see that
## after instantiate object, it
## automatically invokes __init__()
              
A = person('Abdullah')
##A.name
print(A.name)
print(A.age)

B = person(19)
##B.age
print(B.age)
