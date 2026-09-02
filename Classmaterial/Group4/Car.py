import turtle

screen = turtle.Screen()
screen.title("Car Assignment")
screen.bgcolor("#ffafcc")

t = turtle.Turtle()
t.pensize(3)
t.speed(0)

t.color("#606c38")
wheel_positions = [0, -200]
circle_sizes = [(-30, 50), (-20, 40)]

for x in wheel_positions:
    for y_offset, radius in circle_sizes:
        t.penup()
        t.goto(x, y_offset)
        t.pendown()
        t.circle(radius)

t.color("black")
body_lines = [
    (-150, 20, 0, 100),
    (-225, 100, 0, 275),
    (-150, 150, 0, 100),
]

for x, y, heading, length in body_lines:
    t.penup()
    t.goto(x, y)
    t.setheading(heading)
    t.pendown()
    t.forward(length)

t.color("#780000")
t.penup()
t.goto(-75, 150)
t.setheading(270)
t.pendown()
t.forward(130)

t.penup()
t.goto(-75, -200)
t.color("black")
t.write("Let us pass, please. TT", font=("Arial", 12, "italic"))
t.hideturtle()

turtle.done()