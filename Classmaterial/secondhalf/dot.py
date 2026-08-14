import turtle
screen = turtle.Screen()
screen.title("Excercise 3")
screen.bgcolor("#606c38")

t = turtle.Turtle()
t.speed(0)
t.penup()
t.pencolor("#780000")

i = -200
while i <= 200:
    t.goto(i, i)
    t.dot(20)
    i += 50

i = -200
while i <= 200:
    t.goto(i, -i)
    t.dot()
    i += 50

turtle.done()