import turtle
screen = turtle.Screen()
screen.title("Hexagon")
screen.bgcolor("#606c38")

t = turtle.Turtle("turtle")
t.speed(0)
t.pensize(5)
t.color("#ffafcc")


def draw_square(side_length):
    for _ in range (side_length):
        t.forward(40)
        t.right(60)

def draw_pattern_square(side_length,number_of_square):
    for _ in range(number_of_square):
        draw_square(side_length)
        t.right(30)
    
draw_pattern_square(6,12)





t.penup()
t.goto(-75, -200)
t.write("TT. Please let me pass.TT", font=("Arial", 12, "italic"))
t.hideturtle()
turtle.done()
