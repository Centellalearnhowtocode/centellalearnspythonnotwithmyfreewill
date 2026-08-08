#Hexagon
import turtle 
screen = turtle.Screen()
screen.title("Hexagon")
t = turtle.Turtle()
t.speed(5)
screen.bgcolor("#bde0fe")

t.pensize(10)

#define the color for hexagon
color = ["#ffc8dd","#880d1e","#18380d","#e500a4","purple","orange"]

#draw the hexagone with different colors
for color in color:
  t.color(color)
  t.forward(100)
  t.left(60)
  t.end_fill()


#Keep window open until user clicks on it
t.hideturtle()
screen.exitonclick()

