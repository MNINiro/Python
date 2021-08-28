# class Enemy:
#     life = 3
#
#     def attack(self):
#         print("ouch!")
#         self.life -= 1
#
#     def checkLife(self):
#         if self.life <= 0:
#             print("I am dead")
#         else:
#             print(str(self.life) + " life left")
#
# enemy1 = Enemy()
# enemy2 = Enemy()
#
# enemy1.attack()
# enemy1.attack()
#
# enemy1.checkLife()
#
# enemy2.attack()
# enemy2.checkLife()


class Mobile:
    def __init__(self, m):
        self.model = m

    def show_model(self, p):
        self.price = p
        print("Model:", self.model, "Price", self.price)

rm = Mobile('RealMe X')
rm.show_model(10000)
print(id(rm)) #it will show memory address
print()

red = Mobile('Redmi 7s')
red.show_model(20000)
print(id(red))
print()

geek = Mobile('Python')
geek.show_model(49)
print(id(geek))















