import turtle
t = turtle.Turtle()

# square
for _ in range(4):
    t.forward(100)
    t.right(90)

t.penup()
t.goto(150, 0)
t.pendown()

# Triangle
for _ in range(3):
    t.forward(100)
    t.left(120)

turtle.done()