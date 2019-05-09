import turtle


def make_board(turt):
    """
    Creates a board for the tic-tac-toe game.
    :param turt: instance of a turtle
    :return: None
    """
    turt.speed(0)
    turt.hideturtle()
    turt.penup()
    turt.goto(-200, 75)
    turt.pensize(10)
    turt.pendown()
    turt.forward(400)
    turt.penup()
    turt.goto(-200, -75)
    turt.pendown()
    turt.forward(400)
    turt.penup()
    turt.goto(-75, 200)
    turt.right(90)
    turt.pendown()
    turt.forward(400)
    turt.penup()
    turt.goto(75, 200)
    turt.pendown()
    turt.forward(400)


def main():
    alex = turtle.Turtle()
    make_board(alex)
    wn = turtle.Screen()
    wn.setup(500, 500, 0, 0)
    wn.exitonclick()


main()
