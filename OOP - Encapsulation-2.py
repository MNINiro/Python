class C:
       def accessible(self): # Define public function
              print('You can see me')

       def __inaccesssible(self): # Define private function
              print ('you can not see me')


C().accessible()     # Access public function
# C().inaccessible()   # Can’t access private function


C()._C__inaccesssible() # Access private function via changed name



## Its fact is to change name of private name like __variable or
## __function() to _ClassName__variable or _ClassName__function().
## So we can’t access them because of wrong names.

