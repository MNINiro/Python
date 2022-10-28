class Girl:
    gender = 'female' # it's a class variable and gender is common for Girl class

    def __init__(self, name):
        self.name = name    # Each Girl has unique name that will be passed through this function


r = Girl('Rachel') # r and s are Objects of Girl class
s = Girl('Stanky')

print(r.name)
print(r.gender)


print(s.name)
print(s.gender)
