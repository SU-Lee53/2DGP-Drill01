import turtle
def reset():
    turtle.reset()
    turtle.stamp()
    turtle.penup()
    turtle.setheading(90)


def move_left():
    turtle.left(90)
    turtle.pendown()
    turtle.forward(50)
    turtle.stamp()
    turtle.penup()
    turtle.right(90)

def move_right():
    turtle.right(90)
    turtle.pendown()
    turtle.forward(50)
    turtle.stamp()
    turtle.penup()
    turtle.left(90)

def move_forward():
    turtle.pendown()
    turtle.forward(50)
    turtle.stamp()
    turtle.penup()

def move_back():
    turtle.right(180)
    turtle.pendown()
    turtle.forward(50)
    turtle.stamp()
    turtle.penup()
    turtle.left(180)


turtle.shape('turtle')
reset()

turtle.onkey(move_forward, 'w')
turtle.onkey(move_back, 's')
turtle.onkey(move_left, 'a')
turtle.onkey(move_right, 'd')
turtle.onkey(reset, 'Escape')
turtle.listen()
