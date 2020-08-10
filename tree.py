import turtle as t

def bark(horizontal, vertical, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()

    for counter in range(1,3):
        t.forward(horizontal)
        t.left(90)
        t.forward(vertical)
        t.left(90)

    t.end_fill()
    t.penup()


def leaves(horizontal, vertical, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()

    t.forward(horizontal)
    t.left(90)
    t.forward(vertical)
    t.right(90)
    t.forward(horizontal)
    t.left(90)
    t.forward(vertical)
    t.right(90)
    t.forward(horizontal)
    t.left(90)
    t.forward(vertical)
    t.left(90)
    t.forward(horizontal)
    t.right(90)
    t.forward(vertical)
    t.left(90)
    t.forward(horizontal)
    t.right(90)
    t.forward(vertical)
    t.left(90)
    t.forward(horizontal)
    t.right(90)
    t.forward(vertical)
    t.left(90)
    t.forward(horizontal)
    t.left(90)
    t.forward(vertical)
    t.right(90)
    t.forward(horizontal)
    t.left(90)
    t.forward(vertical)
    t.right(90)
    t.forward(horizontal)
    t.left(90)
    t.forward(vertical)
    t.right(90)
    t.forward(horizontal)
    t.left(90)
    t.forward(vertical)
    t.left(90)
    t.forward(horizontal)
    t.right(90)
    t.forward(vertical)
    t.left(90)
    t.forward(horizontal)
    t.right(90)
    t.forward(vertical)
    t.left(90)
    t.forward(horizontal)
    t.forward(horizontal)

    t.end_fill()
    t.penup()

t.penup()
t.speed('slow')
t.bgcolor('light blue')

##bark
t.goto(-10,-200)
bark(50, 200, 'brown')

##leaves
t.goto(40,0)
leaves(50, 50, 'green')

def apples(horizontal, vertical, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()

    for counter in range(1,3):
        t.forward(horizontal)
        t.left(90)
        t.forward(vertical)
        t.left(90)

    t.end_fill()
    t.penup()

##apples
t.goto(-10,50)
apples(10, 10, 'red')
t.goto(-60,100)
apples(10, 10, 'red')
t.goto(90,100)
apples(10, 10, 'red')
t.goto(40,150)
apples(10, 10, 'red')
t.goto(-15,175)
apples(10, 10, 'red')





















    
    


















    
    
