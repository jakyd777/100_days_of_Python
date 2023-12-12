import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)

# directions = [0, 90, 180, 270]
# timmy.pensize(10)
timmy.speed("fastest")


def random_color():
    """return random tuple with RGB"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_rgb = (r, g, b)
    return color_rgb


for _ in range(0, 360, 5):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.left(5)

# for _ in range(200):
#     timmy.color(random_color())
#     timmy.setheading(random.choice(directions))
#     timmy.forward(20)

screen = t.Screen()
screen.exitonclick()
