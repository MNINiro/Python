import turtle as t

def rectangle(horizontal, vertical, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    
    for counter in range(1, 3):
        t.forward(horizontal)
        t.left(90)
        t.forward(vertical)
        t.left(90)

    t.end_fill()
    t.penup()

# ============= Main Body =================

t.penup()
t.speed('fast')
t.bgcolor('black')

t.goto(0, 0)
rectangle(170, 280, 'white') # outside box

t.goto(10, 15)
rectangle(150, 250, 'teal') # inside box

# for left-side windows
x = 0
for w in range(5):
    t.goto(30, x+25)
    rectangle(30, 20, 'white')
    x += 50

# for right-side windows
x = 0
for w in range(5):
    t.goto(100, x+25)
    rectangle(30, 20, 'white')
    x += 50

for i in range(9999999): # for time delay
    t.penup()
