import turtle

screen = turtle.Screen()
screen.title("Excercise 2")
screen.bgcolor("#a7c957")

t = turtle.Turtle()
t.pensize(4)
t.speed(0)


def diamond_square(side_lenght):
    t.left(45)
    t.forward(side_lenght)
    t.right(90)
    t.forward(side_lenght)
    t.right(90)
    t.forward(side_lenght)
    t.right(90)
    t.forward(side_lenght)
    t.setheading(0)


    t.penup()
    t.forward(80)
    t.pendown()

def diamond_square_pattern(side_lenght,number_of_square):
   for i in range(number_of_square):
    diamond_square(side_lenght)
      


t.color("pink")
diamond_square_pattern(-100,1)


t.color("#606c38","#606c38")
diamond_square_pattern(-100,1)
t.color("#cdb4db","#cdb4db")
diamond_square_pattern(-100,1)
t.color("#780000","#780000")
diamond_square_pattern(-100,1)




t.penup()
t.goto(-75, -200)
t.write("Let me pass, please. TT", font=("Arial", 12, "italic"))
t.hideturtle()


turtle.done()
