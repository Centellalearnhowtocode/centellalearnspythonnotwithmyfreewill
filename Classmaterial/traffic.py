#Create Taffic screen
import turtle 
screen = turtle.Screen()
screen.title("Traffic Light")
t = turtle.Turtle()
#Background color
screen.bgcolor("purple")

#Create turtle name t
t = turtle.Turtle()
t.speed(3)

#Draw the traffic light house (Regtangle)
t.penup()
t.goto(-59,150)
t.pendown()
t.color("silver")
t.begin_fill()
for _ in range(2):
    t.forward(100)
    t.right(90)
    t.forward(300)
    t.right(90)
t.end_fill()

#draw red light
t.penup()
t.goto(0,100)
t.pendown()
t.color("red")
t.begin_fill()
t.circle(25)
t.end_fill()

#draw yellow light
t.penup()
t.go