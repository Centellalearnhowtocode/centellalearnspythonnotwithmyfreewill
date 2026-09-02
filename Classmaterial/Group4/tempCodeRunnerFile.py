import turtle
screen = turtle.Screen()
screen.title("Car Assignment")
screen.bgcolor("#ffafcc")

t = turtle.Turtle()
t.pensize(3)
t.speed(0)

#wheel
t.color("#606c38")
t.penup()
t.goto(0,-30)
t.pendown()
t.circle(50)

t.penup()
t.goto(0,-20)
t.pendown()
t.circle(40)

t.penup()
t.goto(-200,-30)
t.pendown()
t.circle(50)

t.penup()
t.goto(-200,-20)
t.pendown()
t.circle(40)

#Car Body
t.penup()
t.goto(-150,20)
t.pendown()
t.forward(100)

t.penup()
t.goto(-225,100)
t.pendown()
t.forward(275)

#Car roof
t.penup()
t.goto(-150,150)
t.pendown()
t.forward(100)

#Car Door
t.color("#606c38")
t.goto(-150,-20)
t.pendown()







t.penup()
t.goto(-75, -200)
t.write("Let us pass, please. TT", font=("Arial", 12, "italic"))
t.hideturtle()
turtle.done()