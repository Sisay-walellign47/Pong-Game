import turtle
import random


screen = turtle.Screen()
player1 = turtle.Turtle()
player2 = turtle.Turtle()
scorer = turtle.Turtle()
scorer2 = turtle.Turtle()
ball = turtle.Turtle()


screen.setup( 800 , 600)
screen.bgcolor("darkblue")
screen.title("Pong Game")

ball.shapesize(stretch_wid=1 , stretch_len=1 )
ball.color("yellow")
ball.shape('square')
ball.penup()
ball.goto(20,0)
ballxdxn = 6
ballydxn = -6

score1 = 0
score2 = 0

if ball.ycor() > 280:
       ball.sety(280)
       ballydxn *= -1   
if ball.ycor() < -280:
       ball.sety(-280)
       ballydxn *= -1   
if ball.xcor() > 400:
       ball.goto(0 , 0)
       ballxdxn *= -1 
       score1 += 1  
if ball.xcor() < -400:
      ball.goto( 0 , 0)
      ballxdxn *= -1
      score2 += 1

scorer.speed(0)
scorer.color("lime")
scorer.penup()
scorer.goto(-130,240)
scorer.pendown()
scorer.write("Player 1 Score:  {} ".format(score1), align="center", font= ["cursive", 22 , "bold"])
scorer.penup()
scorer.goto(-130,200)
scorer.pendown()
scorer.hideturtle()


scorer2.speed(0)
scorer2.color("red")
scorer2.penup()
scorer2.goto(130,240)
scorer2.pendown()
scorer2.write("Player 2 Score: {} ".format(score2), align="center", font= ["cursive", 22 , "bold"])
scorer2.penup()
scorer2.goto(130,200)
scorer2.pendown()
scorer2.hideturtle()

player1.shape('square')
player1.color("darkblue","lime")
player1.shapesize(stretch_wid= 5 , stretch_len=1.3 )
player1.penup()
player1.goto(-393,10)
player1.pendown()



player2.shape ('square')
player2.color("red")
player2.shapesize(stretch_wid=5 , stretch_len=1.3 )
player2.penup()
player2.goto(385,10)
player2.pendown


def player1_up():
    y = player1.ycor()
    y += 20
    player1.sety(y)

def player1_down():
    y = player1.ycor()
    y -= 20
    player1.sety(y)

def player2_up():
    y = player2.ycor()
    y += 20
    player2.sety(y)

def player2_down():
    y = player2.ycor()
    y -= 20
    player2.sety(y)


while True:
   screen.update()
   ball.setx(ball.xcor() + ballxdxn )
   ball.sety(ball.ycor() + ballydxn )

   screen.listen()
   screen.onkeypress(player2_up, "Up")

   screen.listen()
   screen.onkeypress(player2_down, "Down")

   screen.listen()
   screen.onkeypress(player1_up, "q")

   screen.listen()
   screen.onkeypress(player1_down, "a")

   if ball.ycor() > 280:
       ball.sety(280)
       ballydxn *= -1   
   if ball.ycor() < -280:
       ball.sety(-280)
       ballydxn *= -1   
   if ball.xcor() > 400:
       ball.goto(0 , 0)
       ballxdxn *= -1 
       score1 += 1 
       scorer.clear() 
       scorer.write("Player 1 Score: {} ".format(score1), align="center", font= ["cursive", 22 , "bold"])
   if ball.xcor() < -400:
      ball.goto( 0 , 0)
      ballxdxn *= -1
      score2 += 1
      scorer2.clear()
      scorer2.write("Player 2 Score: {} ".format(score2), align="center", font= ["cursive", 22 , "bold"])

   if (ball.xcor() < -340 and ball.xcor() > -350) and ( ball.ycor() < player1.ycor() + 40 and ball.ycor() > player1.ycor() - 40 ):
       ball.setx(-346)
       ballxdxn *= -1

   if (ball.xcor() > 340 and ball.xcor() < 350) and ( ball.ycor() < player2.ycor() + 40 and ball.ycor() > player2.ycor() - 40 ):
       ball.setx(346)
       ballxdxn *= -1