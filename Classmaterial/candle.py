#candle
import turtle 
screen = turtle.Screen()
screen.title("Candle Drawing")
t = turtle.Turtle()
t.speed(3)
screen.bgcolor("#bde0fe")

#Draw pink candle body
t.color("pink")
t.penup()
t.goto(-25,-100)
t.pendown()
t.begin_fill()


#Draw a rectangle for the candle body
for _ in range(2):
    t.forward(50)
    t.left(90)
    t.forward(150)
    t.left(90)

t.end_fill()

  #Draw the yellow flame
t.color("yellow")
t.begin_fill()
t.penup()
t.goto(0,50)
t.pendown()
t.circle(25)
t.end_fill()

#Draw brown wick
t.color("brown")
t.width(3)
t.penup()
t.goto(0,50)
t.pendown()
t.goto(0,80)

#Hide the turtle and finish
t.hideturtle()
screen.exitonclick()


