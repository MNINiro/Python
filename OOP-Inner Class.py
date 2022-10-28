class Outer:
    """Outer Class"""

    def __init__(self):
        ## Instantiating the 'Inner' class
        self.inner = self.Inner()
        ## Instantiating the '_Inner' class
        self._inner = self._Inner()

    def show_classes(self):
        print("This is Outer class")
        # print(inner)
        # print(_inner)

    class Inner:
        def inner_display(self, msg):
            print("This is Inner class")
            print(msg)

    # class _Inner:
    #     def inner_display(self, name, msg):
    #         self.name = name
    #         print("This is _Inner class")
    #         print(self.name, msg)


## instantiating the classes

## 'Outer' class
outer = Outer()

## 'Inner' class
inner = outer.Inner()  ## inner = outer.inner or inner = Outer().Inner()
_inner = outer._Inner()  ## _inner = outer._outer or _inner = Outer()._Inner()

## calling the methods
outer.show_classes()
print()

## 'Inner' class
inner.inner_display("Just Print It!")
print()

## '_Inner' class
name = input('Enter a name:')
message = input('Enter your message:')
_inner.inner_display(name, message)
