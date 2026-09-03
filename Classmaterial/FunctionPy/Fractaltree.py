import turtle
def draw_fractal_tree(branch_length):
    if branch_length > 5:
        turtle.forward(branch_length)
        turtle.right(20)
        draw_fractal_tree(branch_length -15)
        turtle.left(40)
        draw_fractal_tree(branch_length -15)
        turtle.right(20)
        turtle.backward(branch_length)


turtle.speed('fastest')
turtle.left(90)
turtle.goto(0,-200)
turtle.pendown()

draw_fractal_tree(100)

turtle.hideturtle()
turtle.done()