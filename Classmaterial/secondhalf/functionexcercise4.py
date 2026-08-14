import turtle

screen = turtle.Screen()
screen.title("Excercise 2")
screen.bgcolor("#a7c957")

t = turtle.Turtle()
t.pensize()
t.speed(0)

for _ in range(3):
    t.left(30)
    t.forward(30)



      



t.penup()
t.goto(-75, -200)
t.write("Let me pass, please. TT", font=("Arial", 12, "italic"))
t.hideturtle()


turtle.done()
