#Create Taffic screen
import turtle 
screen = turtle.Screen()
screen.title("Traffic Light")
t = turtle.Turtle()
#Background color
screen.bgcolor("#ffc2d1")

#Create turtle name t
t = turtle.Turtle()
t.speed(3)

#Draw the traffic light house (Regtangle)
t.penup()
t.goto(-59,150)
t.pendown()
t.color("#fb6f92")
t.begin_fill()
for _ in range(2):
    t.forward(100)
    t.right(90)
    t.forward(250)
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
t.goto(0,0)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(25)
t.end_fill()

#draw green light
t.penup()
t.goto(0,-100)
t.pendown()
t.color("green")
t.begin_fill()
t.circle(25)
t.end_fill()

#Exit
screen.exitonclick()