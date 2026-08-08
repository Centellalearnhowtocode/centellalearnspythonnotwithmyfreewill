import turtle
import time

t = turtle.Turtle()
t.pensize(4)
t.color("pink")

time.sleep(1)


turtle.goto(0,90)
print(turtle.pos())

turtle.goto(90,0)
print(turtle.pos())


turtle.done()