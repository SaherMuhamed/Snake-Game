from turtle import Turtle

STARTING_POSITION = [(-20, 0), (-40, 0), (-60, 0)]
MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        for position in STARTING_POSITION:
            self.create_snake(position)

    def create_snake(self, position):
        # TODO 1: Create a snake.
        my_turtle = Turtle("square")
        my_turtle.penup()
        my_turtle.color("white")
        my_turtle.goto(position)
        self.segments.append(my_turtle)

    def extend(self):
        self.create_snake(self.segments[-1].position())

    def move(self):
        # TODO 2: Move a snake.
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def go_up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def go_down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def go_right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def go_left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
