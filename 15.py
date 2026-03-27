import turtle
import random

turtle.speed(0)


# --- Screen Setup ---
def setup_screen():
    """Configures the turtle graphics window."""
    screen = turtle.Screen()
    screen.bgcolor("midnightblue")
    screen.setup(width=800, height=600)
    screen.title("Night City Skyline")
    turtle.tracer(0)
    return screen


# --- Star Drawing Function ---
def draw_stars(num_stars):
    """Draws random stars on the night sky."""
    star_turtle = turtle.Turtle()
    star_turtle.hideturtle()
    star_turtle.penup()
    star_turtle.color("white")
    for _ in range(num_stars):
        x = random.randint(-400, 400)
        y = random.randint(-200, 300)
        star_turtle.goto(x, y)
        star_turtle.dot(random.randint(2, 4))
    star_turtle.hideturtle()


# --- Moon Drawing Function ---
def draw_moon():
    """Draws a crescent moon in the sky."""
    moon_turtle = turtle.Turtle()
    moon_turtle.hideturtle()
    moon_turtle.penup()
    moon_turtle.goto(300, 250)
    moon_turtle.color("lightyellow")
    moon_turtle.begin_fill()
    moon_turtle.circle(40)
    moon_turtle.end_fill()
    
    moon_turtle.goto(290, 250)
    moon_turtle.color("midnightblue")
    moon_turtle.begin_fill()
    moon_turtle.circle(35)
    moon_turtle.end_fill()
    
    moon_turtle.hideturtle()


# --- Ground Drawing Function ---
def draw_ground():
    """Draws black ground for buildings to stand on."""
    ground_turtle = turtle.Turtle()
    ground_turtle.hideturtle()
    ground_turtle.penup()
    ground_turtle.goto(-400, -250)
    ground_turtle.pendown()
    ground_turtle.color("black")
    ground_turtle.begin_fill()
    ground_turtle.goto(400, -250)
    ground_turtle.goto(400, -300)
    ground_turtle.goto(-400, -300)
    ground_turtle.goto(-400, -250)
    ground_turtle.end_fill()


# --- Rectangular Window Function ---
def draw_rect_window(t, x, y, width, height):
    """Draws a rectangular window at given position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()


# --- Round Window Function ---
def draw_round_window(t, x, y, size):
    """Draws a round window at given position."""
    t.penup()
    t.goto(x, y)
    t.dot(size)
    t.color("yellow")


# --- Single Building Drawing Function ---
def draw_building(x, y_base, width, height, color):
    """Draws a single building with given position, dimensions and color."""
    building_turtle = turtle.Turtle()
    building_turtle.hideturtle()
    building_turtle.penup()
    building_turtle.goto(x, y_base)
    building_turtle.pendown()
    building_turtle.color(color)
    building_turtle.begin_fill()
    building_turtle.forward(width)
    building_turtle.left(90)
    building_turtle.forward(height)
    building_turtle.left(90)
    building_turtle.forward(width)
    building_turtle.left(90)
    building_turtle.forward(height)
    building_turtle.left(90)
    building_turtle.end_fill()
    draw_windows(x, y_base, width, height)


# --- Window Drawing Function ---
def draw_windows(x, y_base, width, height):
    """Draws structured grid windows on a building (mixed round and rectangular)."""
    window_turtle = turtle.Turtle()
    window_turtle.hideturtle()
    window_turtle.penup()
    
    rows = int(height // 25)
    cols = int(width // 25)
    
    for row in range(rows):
        for col in range(cols):
            if random.random() > 0.4:
                wx = x + col * 25 + 6
                wy = y_base + row * 25 + 6
                
                if random.random() > 0.5:
                    draw_round_window(window_turtle, wx, wy, 10)
                else:
                    draw_rect_window(window_turtle, wx, wy, 12, 16)


#City Generation Function
def draw_city():
    """Generates the entire city skyline with front and back building rows."""
    screen = setup_screen()
    draw_stars(100)
    draw_moon()
    draw_ground()
    
    x = -400
    while x < 400:
        width = random.randint(60, 110)
        height = random.randint(120, 280)
        draw_building(x, -250, width, height, "gray30")
        x += width + random.randint(5, 20)
    
    x = -400
    while x < 400:
        width = random.randint(50, 100)
        height = random.randint(100, 300)
        draw_building(x, -250, width, height, "black")
        x += width + random.randint(10, 30)
    
    turtle.update()
    turtle.done()


# --- Program Start ---
draw_city()
