import turtle

t = turtle.Turtle()
t.speed(0)
t.pencolor("#780000")
t.pensize(2)

def square(side_length):
    for _ in range(4):
        t.forward(side_length)
        t.left(90)
i = 10
while i <=80:
    square(i)
    t.left(10)
    i += 2
turtle.done()