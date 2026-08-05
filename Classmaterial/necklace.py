import turtle

screen = turtle.Screen()
screen.turtle("Turtle Lab Sessiion")
screen.bgcolor("pink")

t = turtle.Turtle("turtle")
t.speed(5)
t.color("yellow")

t.penup()
t.goto(0,-100)
t.pendown()
t.goto(100)
t.circle(180)


for _ in range(80):
    t.penup()
    t.goto(0,0)
    t.forward(100)
    t.pendown()
    t.dot(10)
    t.penup()
    t.goto(0,0)
    t.right(25)

    t.hideturtle()
    turtle.done()