import turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.title("Car Assignment")
screen.bgcolor("#ffafcc")
t.pencolor("#606c38")
t.pensize(3)
def draw_spiral(length):
    if length > 5:
        turtle.forward(length)
        turtle.right(30)
        draw_spiral(length - 5)

turtle.speed('fastest')
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

draw_spiral(100)








turtle.hideturtle()
turtle.done()