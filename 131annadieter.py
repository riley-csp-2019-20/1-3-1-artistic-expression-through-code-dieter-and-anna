#creating snake
import turtle as trtl
import random

# Score

score = 0

pen = trtl.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  ", align="center", font=("Times New Roman", 24, "normal"))
score += 1

powerup = trtl.Turtle()
powerup.speed(0)
powerup.shape("circle")
powerup.color("red")
powerup.penup()
powerup.goto(0,100)

head = trtl.Turtle()
head.speed(0)
head.shape("triangle")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

head.xcor()
head.ycor()

def Up():
    head.setheading(90)
    head.forward(5)
    y = head.ycor()
    head.sety(y + 20)

def Down():
    head.setheading(270)
    head.forward(5)
    y = head.ycor()
    head.sety(y - 20)

def Left():
    head.setheading(180)
    head.forward(5)
    x = head.xcor()
    head.setx(x - 20)

def Right():
    head.setheading(0)
    head.forward(5)
    x = head.xcor()
    head.setx(x + 20)


wn = trtl.Screen()
wn.title("Snake Game by dieter and anna")
wn.bgcolor("purple")
wn.setup(width=600, height=600)
wn.tracer(0)
wn.onkeypress(Up, "Up")
wn.onkeypress(Down, "Down")
wn.onkeypress(Left, "Left")
wn.onkeypress(Right, "Right")
wn.listen()
wn.mainloop()