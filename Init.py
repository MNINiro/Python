class Enemy:

    def __init__(self, x): # Initial function. It will run first.
        self.energy = x


    def get_energy(self):
        print(self.energy)

jason = Enemy(5) # jason is an Object
sandy = Enemy(18)

jason.get_energy()
sandy.get_energy()