class A:
       i = 123
       def __init__(self):
              self.i = 12345


## Invoke form: just invoke data or method in the class, so i=123

print (A.i)

## Invoke object: instantialize object firstly, and then invoke
## data or Methods.
## Here it experienced __init__(),
## i=12345

print (A().i) # A(self).i
