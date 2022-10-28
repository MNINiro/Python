class greeting:
    def hello(self, name = None):
        if name is not None:
            print ("Hello " + name)
        else:
            print ("Hello")

myGreeting = greeting()
myGreeting.hello()
myGreeting.hello("Christopher")