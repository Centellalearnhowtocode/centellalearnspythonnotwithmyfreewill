#Hexagon
import turtle 
screen = turtle.Screen()
screen.title("Hexagon")

#Create turtle name "t"
t = turtle.Turtle("turtle")
t.pensize(5)
t.speed(3)

#define the color for hexagon
colors = ["red","green","blue","yellow","orange","purple"]

#draw the hexagone with different colors
for color in colors:
  t.color(colors)
  t.forward(100)
  t.left(60)


#Keep window oep
screen.exitonclick()


