from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(0.75, 0.75)
        self.speed(0)
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

    def move(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
