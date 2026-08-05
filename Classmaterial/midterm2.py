import turtle
import math
screen = turtle.Screen()
screen.title("Spiral Of Squares")
t = turtle.Turtle()
t.speed(0)
screen.bgcolor("#b9fbc0")

#Excercise 2
t.color("#ffa5ab")
t.width(3)
t.penup()
t.goto(0,50)
t.pendown()

R = 150     
N = 30      
skip = 5    

points = []
for i in range(N):
    angle = 2 * math.pi * i / N
    x = R * math.cos(angle)
    y = R * math.sin(angle)
    points.append((x, y))


for x, y in points:
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.goto(x, y)

#star
for i in range(N):
    t.color("#da627d")
    x1, y1 = points[i]
    x2, y2 = points[(i + skip) % N]
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)

screen.exitonclick()
turtle.done()

