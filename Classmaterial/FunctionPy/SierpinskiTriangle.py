import turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.title("Car Assignment")
screen.bgcolor("#ffafcc")
t.pencolor("#606c38")
t.pensize(3)
def sierpiski_triangle(length,depth):
    if depth == 0:
        for _ in range(3):
            t.forward(length)
            t.left(120)
    else:
        sierpiski_triangle(length/2,depth-1)
        t.forward(length/2)
        sierpiski_triangle(length/2,depth-1)
        t.backward(length/2)
        t.left(60)
        t.forward(length/2)
        t.right(60)
        sierpiski_triangle(length/2,depth-1)
        t.left(60)
        t.backward(length/2)
        t.right(60)

t.speed('fastest')
t.penup()
t.goto(-200,-150)
t.pendown()

sierpiski_triangle(400,4)

t.hideturtle()
t.done()