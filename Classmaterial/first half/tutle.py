import turtle
screen = turtle.Screen()
screen.title("Turtle Graphics")
screen.bgcolor("black")

#creature cursor
t = turtle.Turtle() #shape, visible

t.speed(10) #the higher the number the faster the turtle moves

t.color("pink","blue") #pen color, fill color
#move it forward by pixel
t.begin_fill()
t.forward(100)
t.right(90) #turn by degree
t.forward(200)
t.right(90) #turn by degree
t.forward(100)
t.right(90) #turn by degree
t.forward(200)
t.end_fill()

screen.exitonclick()