import turtle

# screen
screen=turtle.Screen()
screen.setup (width = 600 ,height =500 )
screen.title("Group 4 - Car Proportional Refinement")

# turtle
t=turtle.Turtle()
t.speed(3)
t.pensize(3)
t.pencolor("#002fa7")  # Classic blue outline

def draw_wheel(x, y):
    
    t.penup()
    t.goto(x, y - 28)
    t.setheading(0)
    t.pendown()
    
    t.fillcolor( "#888888")  # Grey fill
    t.begin_fill()
    t.circle( 28 )
    t.end_fill()
    
    #  rim 
    t.penup()
    t.goto(x,y - 18)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    t.circle(18 )
    t.end_fill( )

# Draw Main
t.penup()
t.goto(-145,  -20)  # front-bottom
t.pendown()

# Front bumper 
t.goto(-150, -10)
t.goto(-150,  15)
t.goto(-140,32)  #  nose

t.goto( -70, 44)   

# Windshield
t.goto( -20, 95)

# Roof line
t.goto(65, 95)

# Rear window slope
t.goto(115, 44)

# Trunk line 
t.goto(162, 41)

# Rounded rear bumper
t.goto(168, 25)
t.goto(168, -5)
t.goto(158, -20)

# Bottom chassis
t.goto(-145, -20)

# - 2. Draw windows & center Pillar
t.penup()
t.goto(-70, 44)
t.pendown()
t.goto(115, 44)

# Main center vertical pillar
t.penup()
t.goto(15, 95)
t.pendown()
t.goto(15, -20)

# --- 3. Draw Details (Handle & Lights) ---
# Minimalist door handle
t.penup()
t.goto(-5, 34)
t.pendown()
t.goto(5, 34)

# Centered Yellow Headlight Outline
t.penup()
t.goto(-150, 10)
t.pendown()
t.pencolor("#d4af37")
t.goto(-146, 25)
t.goto(-137, 23)
t.goto(-141, 10)
t.goto(-150, 10)

# Unfilled Red Taillight Outline
t.penup()
t.goto(168, 23)
t.pendown()
t.pencolor("red")
t.goto(156, 23)
t.goto(156, 5)
t.goto(168, 5)
t.goto(168, 23)

# Reset pen color for wheels
t.pencolor("#002fa7")

# --- 4. Draw Wheels ---
draw_wheel(-85, -20)
draw_wheel(95, -20)

# Hide turtle and lock screen
t.hideturtle()
screen.mainloop()