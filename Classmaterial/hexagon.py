#Hexagon
import turtle 
screen = turtle.Screen()
screen.title("Hexagon")
t = turtle.Turtle()
t.speed(3)
screen.bgcolor("#bde0fe")

t.pensize(5)

#define the color for hexagon
color = ["#ffc8dd","#880d1e","#18380d","blue","yellow","#e500a4"]

#draw the hexagone with different colors
for color in color:
  t.begin_fill()
  t.color(color,color)
  t.forward(100)
  t.left(60)
  t.end_fill()


#Keep window open until user clicks on it
t.hideturtle()
screen.exitonclick()

