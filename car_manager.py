from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.create_car()
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        # We will create a random choice to generate a car every 1 choice
        random_choice = random.randint(1, 6)
        if random_choice == 1 :
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            y_position = random.randint(-250, 250)
            new_car.goto(x=300, y=y_position)
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

