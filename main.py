import time
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.tracer(0)
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # TODO 3: Detect collision with food.
    if snake.segments[0].distance(food) < 15:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

    # TODO 4: Detect collision with walls.
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -300 or snake.segments[0].ycor() > 300 or snake.segments[0].ycor() < -280:
        scoreboard.reset()

    # TODO 5: Detect collision with tails.
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            scoreboard.reset()


screen.exitonclick()

