import turtle as t
from itertools import cycle

colors = cycle(['red', 'orange', 'white', 'yellow',
                'green', 'blue', 'purple'])

def draw_circle(size, angle, shift):
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(shift)

    draw_circle(size + 5, angle + 1, shift + 1) # recursive function

#     ==================================
t.bgcolor('black')
t.speed('fast')
t.pensize(1)
draw_circle(30, 0, 1)
