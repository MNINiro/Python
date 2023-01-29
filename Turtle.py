import turtle

def draw_robot():
    #set up turtle
    robot = turtle.Turtle()
    robot.shape("turtle")
    robot.speed(10)

    #draw the head
    robot.penup()
    robot.goto(-50,50)
    robot.pendown()
    robot.begin_fill()
    robot.circle(50)
    robot.end_fill()

    #draw the body
    robot.penup()
    robot.goto(-50,0)
    robot.pendown()
    robot.begin_fill()
    robot.forward(100)
    robot.right(90)
    robot.forward(75)
    robot.right(90)
    robot.forward(100)
    robot.right(90)
    robot.forward(75)
    robot.end_fill()

    #draw the arms
    robot.penup()
    robot.goto(-75,-25)
    robot.pendown()
    robot.begin_fill()
    robot.right(90)
    robot.forward(50)
    robot.right(90)
    robot.forward(25)
    robot.right(90)
    robot.forward(50)
    robot.end_fill()

    robot.penup()
    robot.goto(25,-25)
    robot.pendown()
    robot.begin_fill()
    robot.right(90)
    robot.forward(50)
    robot.right(90)
    robot.forward(25)
    robot.right(90)
    robot.forward(50)
    robot.end_fill()

    #draw the legs
    robot.penup()
    robot.goto(-25,-75)
    robot.pendown()
    robot.begin_fill()
    robot.right(90)
    robot.forward(50)
    robot.right(90)
    robot.forward(25)
    robot.right(90)
    robot.forward(50)
    robot.end_fill()

    robot.penup()
    robot.goto(75,-75)
    robot.pendown()
    robot.begin_fill()
    robot.right(90)
    robot.forward(50)
    robot.right(90)
    robot.forward(25)
    robot.right(90)
    robot.forward(50)
    robot.end_fill()

    #draw the eyes
    robot.penup()
    robot.goto(-25,65)
    robot.pendown()
    robot.begin_fill()
    robot.circle(10)
    robot.end_fill()

    robot.penup()
    robot.goto(25,65)
    robot.pendown()
    robot.begin_fill()
    robot.circle(10)
    robot.end_fill()


draw_robot()
turtle.done()