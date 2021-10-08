from turtle import Screen
from pedal import pedal
from Ball import ball
from scoreboard import scoreboard
import time

Pedal1_POSITION = (350,0)
Pedal2_POSITION = (-350,0)


screen= Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)
right_pedal = pedal(Pedal1_POSITION)
left_pedal = pedal(Pedal2_POSITION)
ball = ball()
score = scoreboard()

screen.listen()

screen.onkey(left_pedal.move_down ,"d")
screen.onkey(left_pedal.move_up,"w")
screen.onkey(right_pedal.move_down ,"Down")
screen.onkey(right_pedal.move_up,"Up")


is_game_on =True
while is_game_on:
   ball.move()
   time.sleep(ball.move_speed)
   screen.update()

   #Detect ball collision with y axis wall
   if ball.ycor()>280 or ball.ycor()<-280:
      ball.bounce_y()
      

   #Detect ball collision with pedal
   if ball.distance(right_pedal)<50 and ball.xcor()>320 or ball.distance(left_pedal)<50 and ball.xcor()<-320:
      ball.bounce_x()
   

   #detect when right pedal misses
   if ball.xcor()>380 :
      ball.reset_position()
      score.l_point()

   #detect when right pedal misses 
   if ball.xcor()<-380:
      ball.reset_position()
      score.r_point()

   if score.l_score==10:
            score.goto(0,0)
            score.clear()
            score.write(f"GAME OVER\nLeft Player wins\nScore: {score.l_score}/{score.r_score}", align="center",font=("Courier",25,"normal"))
            is_game_on =False    
   elif score.r_score==10:
            score.goto(0,0)
            score.clear()
            score.write(f"GAME OVER\nRight Player wins\nScore: {score.r_score}/{score.l_score}", align="center",font=("Courier",25,"normal"))
            is_game_on = False
         





screen.exitonclick()