from random import random


class Spam:
    def __init__(self):
        self.word = None

    def oneFunction(self, lst):
        category = random.choice(list(lst.keys()))
        self.word = random.choice(lists[category])

    def anotherFunction(self):
        for letter in self.word:
            print("_", end=" ")


s = Spam()
lists = [5, 67, 3, 56, 87, 3]
s.oneFunction(lists)
s.anotherFunction()
