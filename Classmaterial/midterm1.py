import turtle
screen = turtle.Screen()
screen.title("Spiral Of Squares")
t = turtle.Turtle()
t.speed(0)
screen.bgcolor("#590d22")

#Excercise 1
t.color("#ffccd5")
t.width(0.99)
t.penup()
t.goto(0,0)
t.pendown()


size = 2
for i in range(100):
    t.forward(size)
    t.right(90)
    t.forward(size)
    t.right(90)
    t.forward(size)
    t.right(90)
    t.forward(size)
    t.right(95)
    size += 2

screen.exitonclick()
turtle.done
    



