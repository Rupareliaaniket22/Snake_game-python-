import turtle
import time
import scoreboard
import snake
import food

screen = turtle.Screen()
screen.setup(height=600, width=600)
turtle.title("Snake Game")
turtle.bgcolor("black")
screen.tracer(0)
game_is_on = True
snake1 = snake.Snake()
food1 = food.Food()
screen.update()
screen.listen()
screen.onkey(snake1.move_up, "Up")
screen.onkey(snake1.move_down, "Down")
screen.onkey(snake1.move_right, "Right")
screen.onkey(snake1.move_left, "Left")
scoreboard = scoreboard.Scoreboard()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake1.move()
    if snake1.head.distance(food1) < 15:
        food1.refresh()
        snake1.extend()
        scoreboard.increase_score()
    if snake1.head.xcor() > 280 or snake1.head.xcor() < -280:
        scoreboard.game_over()
        game_is_on = False
    if snake1.head.ycor() > 280 or snake1.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False
    for turtles in snake1.turtles[1:]:
        if snake1.head.distance(turtles) < 5:
            game_is_on = False
            scoreboard.game_over()
            scoreboard.update_high_score()

screen.exitonclick()
