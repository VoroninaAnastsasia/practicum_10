import turtle

turtle.speed(0)
turtle.bgcolor("white")

def circle(x, y):
    """Draws a circle"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor("pink")
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()

def square(x, y):
    """Draws a square"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor("deeppink")
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(60)
        turtle.right(90)
    turtle.end_fill()

def triangle(x, y):
    """Draws a triangle"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor("hotpink")
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(70)
        turtle.left(120)
    turtle.end_fill()

def create_ornament():
    """Creates an ornament on a square
    with three repeating elements"""
    
    # Draw a large square
    turtle.penup()
    turtle.goto(-200, 200)
    turtle.pendown()
    turtle.pensize(3)
    for _ in range(4):
        turtle.forward(400)
        turtle.right(90)
    
    circle(-105, 80)   # circle
    square(-20, 140)      # square
    triangle(105, 85)  # triangle
    
    # Second row
    square(-130, 40)     # square
    triangle(-25, -20)      # triangle
    circle(135, -25)      # circle
    
    # Third row
    triangle(-135, -130) # triangle
    circle(15, -135)      # circle
    square(110, -70)    # square
    
    turtle.hideturtle()
    turtle.done()

create_ornament()
