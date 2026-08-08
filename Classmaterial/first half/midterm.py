#candle
import turtle 
screen = turtle.Screen()
screen.title("Candle Drawing")
t = turtle.Turtle()
t.speed(3)
screen.bgcolor("#721321")


t.width(3)
t.penup()
t.goto(-145,-120)
t.pendown()

#Square frame
for _ in range(2):
  
    t.color("#b5c9c3")
    t.forward(300)
    t.left(90)
    t.forward(300)
    t.left(90)
   
t.width(3)
t.penup()
t.goto(-150,-120)
t.pendown()
for _ in range(2):
    t.color("#b5c9c3")
    t.forward(320)
    t.left(90)
    t.forward(320)
    t.left(90)

#Circle
t.color("#b5c9c3")
t.penup()
t.goto(0,-20)
t.pendown()
t.circle(50)

t.color("#b5c9c3")
t.penup()
t.goto(0,-10)
t.pendown()
t.circle(40)

#Diamond
t.color("#b5c9c3")
t.goto(0, -212)
t.pendown()
for _ in range(4):
    t.right(-45)
    t.forward(300)
    t.left(45)
t.pendown() 


#Hide the turtle and finish
t.hideturtle()
screen.exitonclick()



