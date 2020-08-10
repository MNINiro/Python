# https://www.geeksforgeeks.org/numpy-in-python-set-1-introduction/

import numpy as np 

#======= numpy.ndarray.__floordiv__() ==================

#Example-1   
# make an array with numpy 

gfg = np.array([1, 2.5, 3, 4.8, 5]) 
   
# applying ndarray.__floordiv__() method 
print(gfg.__floordiv__(2)) 

#Example-2

gfg = np.array([[1, 2, 3, 4.45, 5], 
                [6, 5.5, 4, 3, 2.62]]) 
   
# applying ndarray.__floordiv__() method 
print(gfg.__floordiv__(3))


#======= numpy.ndarray.__mod__() ===============
#Example-1  
# make an array with numpy 

gfg = np.array([1, 2.5, 3, 4.8, 5]) 
    
# applying ndarray.__mod__() method 
print(gfg.__mod__(2))

#Example-2

gfg = np.array([[1, 2, 3, 4.45, 5], 
                [6, 5.5, 4, 3, 2.62]]) 
    
# applying ndarray.__mod__() method 
print(gfg.__mod__(3)) 


#=============== numpy.ndarray.__divmod__() =================

gfg = np.array([1, 2, 3, 4, 5]) 
    
# applying ndarray.__divmod__() method 
print(gfg.__divmod__(3))

#Example-2

gfg = np.array([[1, 2, 3, 4, 5], 
                [6, 5, 4, 3, 2]]) 
    
# applying ndarray.__divmod__() method 
print(gfg.__divmod__(3))


#============== numpy.ndarray.__add__() =================

gfg = np.array([1, 2, 3, 4, 5]) 
   
# applying ndarray.__add__() method 
print(gfg.__add__(5))

#Example-2

gfg = np.array([[1, 2, 3, 4, 5], 
                [6, 5, 4, 3, 2]]) 
   
# applying ndarray.__add__() method 
print(gfg.__add__(5))


#============== numpy.ndarray.__invert__() =================

gfg = np.array([1, 2, 3, 4, 5]) 
    
# applying ndarray.__invert__() method 
print(gfg.__invert__())

#Example-2

gfg = np.array([[1, 2, 3, 4, 5], 
                [6, 5, 4, 3, 2]]) 
    
# applying ndarray.__invert__() method 
print(gfg.__invert__())


#============== numpy.ndarray.__mul__() =================

gfg = np.array([1, 2.5, 3, 4.8, 5]) 
   
# applying ndarray.__mul__() method 
print(gfg.__mul__(5))

#Example-2

gfg = np.array([[1, 2, 3, 4.45, 5], 
                [6, 5.5, 4, 3, 2.62]]) 
   
# applying ndarray.__mul__() method 
print(gfg.__mul__(5))


#============== numpy.ndarray.__sub__() =================
gfg = np.array([1, 2, 3, 4, 5]) 
   
# applying ndarray.__sub__() method 
print(gfg.__sub__(5))

#Example-2

gfg = np.array([[1, 2, 3, 4, 5], 
                [6, 5, 4, 3, 2]]) 
   
# applying ndarray.__sub__() method 
print(gfg.__sub__(5))


#============== numpy.ndarray.__lshift__() =================
gfg = np.array([1, 2, 3, 4, 5]) 
     
# applying ndarray.__lshift__() method 
print(gfg.__lshift__(2))

#Example-2

gfg = np.array([[1, 2, 3, 4, 5], 
                [6, 5, 4, 3, 2]]) 
     
# applying ndarray.__lshift__() method 
print(gfg.__lshift__(1))


#============== numpy.ndarray.__ne__() =================
gfg = np.array([1, 2, 3, 4, 5, 6]) 
  
# applying numpy.__ne__() method 
print(gfg.__ne__(4))

#Example-2

gfg = np.array([[1, 2, 3, 4, 5, 6], 
                [6, 5, 4, 3, 2, 1]]) 
  
# applying numpy.__ne__() method 
print(gfg.__ne__(4)) 

#============== numpy.ndarray.__xor__() =================
gfg = np.array([1, 2, 3, 4, 5]) 
     
# applying ndarray.__xor__() method 
print(gfg.__xor__(2))

#Example-2

gfg = np.array([[1, 2, 3, 4, 5], 
                [6, 5, 4, 3, 2]]) 
     
# applying ndarray.__xor__() method 
print(gfg.__xor__(1)) 

#============== numpy.ndarray.__and__() =================
gfg = np.array([1, 2, 3, 4, 5]) 
     
# applying ndarray.__and__() method 
print(gfg.__and__(2))

#Example-2

gfg = np.array([[1, 2, 3, 4, 5], 
                [6, 5, 4, 3, 2]]) 
     
# applying ndarray.__and__() method 
print(gfg.__and__(1)) 


#============== numpy.ndarray.__or__() =================

gfg = np.array([1, 2, 3, 4, 5]) 
     
# applying ndarray.__or__() method 
print(gfg.__or__(2))

#Example-2

gfg = np.array([[1, 2, 3, 4, 5], 
                [6, 5, 4, 3, 2]]) 
     
# applying ndarray.__or__() method 
print(gfg.__or__(1)) 

#============== numpy.ndarray.__iadd__() =================
gfg = np.array([1.2, 2.6, 3, 4.5, 5]) 
    
# applying ndarray.__iadd__() method 
print(gfg.__iadd__(5))

#Example-2

gfg = np.array([[1, 2.2, 3, 4, 5.01], 
                [6.1, 5, 4.8, 3, 2]]) 
    
# applying ndarray.__iadd__() method 
print(gfg.__iadd__(3)) 

#============== numpy.ndarray.__pow__() =================
gfg = np.array([1, 2, 3, 4, 5]) 
     
# applying ndarray.__pow__() method 
print(gfg.__pow__(3))

#Example-2

gfg = np.array([[1, 2, 3, 4, 5], 
                [6, 5, 4, 3, 2]]) 
     
# applying ndarray.__pow__() method 
print(gfg.__pow__(2))

#============== numpy.ndarray.__rshift__() =================

gfg = np.array([1, 2, 3, 4, 5]) 
     
# applying ndarray.__rshift__() method 
print(gfg.__rshift__(2))

#Example-2

gfg = np.array([[1, 2, 3, 4, 5], 
                [6, 5, 4, 3, 2]]) 
     
# applying ndarray.__rshift__() method 
print(gfg.__rshift__(1))





































