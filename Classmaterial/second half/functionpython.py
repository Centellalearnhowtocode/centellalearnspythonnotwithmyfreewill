import turtle
screen = turtle.Screen()
screen.title("Square Loop")
screen.bgcolor("#6361df")

t = turtle.Turtle("turtle")
t.speed(0)
t.pensize(3)
t.color("pink")

def draw_square(side_length):
    for _ in range (4):
        t.forward(side_length)
        t.right(90)

def draw_pattern_square(side_length, numbner_of_square):
    for _ in range(numbner_of_square):
        draw_square(side_length)
        t.right(360 / numbner_of_square)


draw_pattern_square(150, 120)
t.hideturtle()
turtle.done()
