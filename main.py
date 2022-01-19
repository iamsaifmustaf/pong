from turtle import Turtle, Screen, tracer, width, window_height
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

def pong_game():
    screen = Screen()
    screen.setup(width=800,height=600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)

    r_paddle = Paddle((350,0))
    l_paddle = Paddle((-350,0))
    ball = Ball()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(r_paddle.move_up, "Up")
    screen.onkey(r_paddle.move_down, "Down")
    screen.onkey(l_paddle.move_up, "w")
    screen.onkey(l_paddle.move_down, "s")
    screen.onkey(scoreboard.game_over,"q")
    screen.onkeypress(r_paddle.move_up, "Up")
    screen.onkeypress(r_paddle.move_down, "Down")
    screen.onkeypress(l_paddle.move_up, "w")
    screen.onkeypress(l_paddle.move_down, "s")

    game_is_on = True

    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        #Detect Collision with Wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            #needs to bounce
            ball.bounce_y()

        #Detect collision with r_paddle and l_paddle
        if ball.distance(r_paddle) < 55 and ball.xcor() > 320 or ball.distance(l_paddle) < 55 and ball.xcor() < -320:
            ball.bounce_x()
            ball.move_speed *= 0.95

        
        #Detect miss with r_paddle and l_paddle
        if ball.xcor() > 380:
            scoreboard.increase_score_left()
            ball.reset_position()
            time.sleep(2)
        if ball.xcor() < -380:
            scoreboard.increase_score_right()
            ball.reset_position()
            time.sleep(2)
        
    print("Game Over")
    time.sleep(3)

    screen.exitonclick()


pong_game()