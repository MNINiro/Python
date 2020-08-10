def maker(n):
    def action(x):
        return x ** n
    return action

f = maker(2) # f is action(x, k=2)


#f(3,3) # returns 3^3 = 27


##print(f)
print(f(3)) # returns 3^2 = 9

print(f(4))

g = maker(3)
print(g(3))

print(f(3)) # still remembers 2

