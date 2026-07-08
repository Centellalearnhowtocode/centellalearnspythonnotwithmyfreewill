import turtle
#1.Set up the screen
screen = turtle.Screen()
screen.bgcolor("#ffafcc")
screen.title("Color")
#2. Create turtle 
t= turtle.Turtle()
t.color("#a2d2ff","#cdb4db")

#3.Drawt
t.begin_fill()
t.left(50)
t.forward(133)
t.circle(50, 200)       # right lobe
t.right(140)
t.circle(50, 200)       # left lobe
t.forward(133)
t.end_fill()

screen.exitonclick()
turtle.done