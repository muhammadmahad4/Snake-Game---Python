from turtle import Screen
from snake import Snake
import time
from snakefood import Food
# import playsoundsimple as pss
from snakescore import ScoreBoard

# s = pss.Sound("E:\sound1.wav")

score = ScoreBoard()

my_screen = Screen()
my_screen.bgcolor('black')
my_screen.title('MF this is a snake game')
my_screen.setup(width=600, height=600)
my_screen.tracer(0)

snake = Snake()
food = Food()

my_screen.listen()
my_screen.onkey(snake.up, 'Up')
my_screen.onkey(snake.down, 'Down')
my_screen.onkey(snake.left, 'Left')
my_screen.onkey(snake.right, 'Right')

game = True
while game:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score_up()
        # s.play(1)

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()

    for segments in snake.segments[1::]:
        if snake.head.distance(segments) < 8:
            score.reset()


my_screen.exitonclick()
