class Mario():

    def move(self):
        print('I am moving!')

class Mashroom():

    def eat_Mashroom(self):
        print('Now I am big!')

class BigMario(Mario, Mashroom): # it inherits from both Mario and Mashroom classes
    pass

bm = BigMario()
bm.move()
bm.eat_Mashroom()
