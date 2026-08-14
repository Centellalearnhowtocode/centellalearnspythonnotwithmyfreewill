import turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(2)
t.pencolor("#780000")

i = 0
while i <80:
    t.forward(-300)
    t.right(150)
    t.forward(-300)
    t.right(150)
    t.right(5)
    i += 1
turtle.done()