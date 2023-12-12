from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.speed = MOVE_INCREMENT

    def create_car(self):
        rand_chance = random.randint(1, 6)
        if rand_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            rand_y = random.randint(-260, 260)
            new_car.goto(280, rand_y)
            self.all_cars.append(new_car)



    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.speed)

    def speed_up(self):
        self.speed += 5
        print(self.speed)
