import random
from turtle import Turtle, colormode, Screen
tim = Turtle()
colormode(255)


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

tim.speed(0)

def draw_spirograph_large(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.color(random_colors())
        tim.circle(90)  
        tim.setheading(tim.heading() - size_of_gap)


def draw_spirograph_small(size_of_gap):
    for p in range(int(360 / size_of_gap)):
        tim.color(random_colors())
        tim.circle(96)  
        tim.setheading(tim.heading() + size_of_gap)

def draw_spirograph_medium(size_of_gap):
    for p in range(int(360 / size_of_gap)):
        tim.color(random_colors())  
        tim.circle(100)  
        tim.setheading(tim.heading() + size_of_gap)  

draw_spirograph_large(5)
tim.penup()
tim.goto(0, 0)
tim.pendown()  
draw_spirograph_medium(5)  
tim.penup()  
tim.goto(0, 0)  
tim.pendown()  
draw_spirograph_small(5)  

