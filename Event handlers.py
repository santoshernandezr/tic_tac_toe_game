import turtle
import math
wn = turtle.Screen()
wn.bgcolor("black")

martin = turtle.Turtle()
martha = turtle.Turtle()

martin.color("black")
martha.color("white")


def the_x(x, y):
    martha.pensize(10)
    martha.penup()
    martha.goto(x - 25, y - 25)
    martha.pendown()
    martha.left(45)
    martha.forward(math.sqrt(5000))
    martha.penup()
    martha.goto(x - 25, y + 25)
    martha.right(90)
    martha.pendown()
    martha.forward(math.sqrt(5000))
    martha.setheading(0)


def the_o(x, y):
    martin.setheading(180)
    martin.goto(x, y)
    martin.begin_fill()
    martin.circle(25)
    martin.end_fill()
    martin.begin_fill()
    martin.circle(20)
    martin.end_fill()

