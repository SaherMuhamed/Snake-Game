from turtle import Turtle, Screen
import random

screen = Screen()
screen.addshape("apple.gif")


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("apple.gif")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(x=random_x, y=random_y)
