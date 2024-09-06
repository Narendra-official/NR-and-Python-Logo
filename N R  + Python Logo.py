import turtle

# turtle object
nr = turtle.Turtle()

#  bg color
turtle.bgcolor("red")

nr.penup()
nr.goto(-100, 0)
nr.pendown()
nr.setheading(90)

# letter N
nr.pensize(15)
nr.pencolor("black")
nr.forward(100)
nr.right(150)
nr.forward(120)
nr.left(150)
nr.forward(100)


# starting position and heading
nr.penup()
nr.goto(15, 0)
nr.pendown()
nr.setheading(90)

# letter R
nr.forward (100)
nr.right(80)
nr.circle(-30, 180)
nr.right(200)
nr.circle(-60, 60)
nr.right(0)
nr.forward(2)


# py Logo
py = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
py.speed(20)
py.pensize(2)
py.pencolor("white")


def s_curve():
    for i in range(90):
        py.left(1)
        py.forward(1)

def r_curve():
    for i in range(90):
        py.right(1)
        py.forward(1)

def l_curve():
    s_curve()
    py.forward(80)
    s_curve()

def l_curve1():
    s_curve()
    py.forward(90)
    s_curve()

def half():
    py.forward(50)
    s_curve()
    py.forward(90)
    l_curve()
    py.forward(40)
    py.left(90)
    py.forward(80)
    py.right(90)
    py.forward(10)
    py.right(90)
    py.forward(120)
    l_curve1()
    py.forward(30)
    py.left(90)
    py.forward(50)
    r_curve()
    py.forward(40)
    py.end_fill()

def get_pos():
    py.penup()
    py.forward(20)
    py.right(90)
    py.forward(10)
    py.right(90)
    py.pendown()

def eye():
    py.penup()
    py.right(90)
    py.forward(160)
    py.left(90)
    py.forward(70)
    py.pencolor("black")
    py.dot(35)

def sec_dot():
    py.left(90)
    py.penup()
    py.forward(310)
    py.left(90)
    py.forward(120)
    py.pendown()

    py.dot(35)


py.fillcolor("#306998")
py.begin_fill()
half()
py.end_fill()
get_pos()
py.fillcolor("#FFD43B")
py.begin_fill()
half()
py.end_fill()

eye()
sec_dot()

def pause():
    py.speed(20)
    for i in range(100):
        py.left(90)
pause()

py.hideturtle()

turtle.done()
