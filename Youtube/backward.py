import turtle
import time

t = turtle.Turtle()
t.pensize(4)
t.color("pink")

time.sleep(1)

for _ in range(6):
    t.backward(40)
    time.sleep(1)
    t.right(60)
    time.sleep(1)
    t.backward(40)

turtle.done()
