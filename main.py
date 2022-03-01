import turtle
from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter a color")
y = [-60, -30, 0, 30, 60, 90]
color = ["green", "red", "orange", "purple", "yellow", "blue"]
is_race_on = False
all_turtles = []
for i in range(0, 6):
    turt1 = Turtle()
    turt1.penup()
    turt1.shape("turtle")
    turt1.color(color[i])
    turt1.goto(x=-230, y=y[i])
    all_turtles.append(turt1)

if user_bet:
    is_race_on = True

while is_race_on:
    if turtle.xcor() > 230 :
        is_race_on = False
        if turtle.pencolor() == user_bet :
            print(f"You've won! The {turtle.pencolor()} turtle is the winner")
        else:
            print(f"You've lost! The {turtle.pencolor()} turtle is the winner")


    for turtle in all_turtles:
        distance = random.randint(0, 10)
        turtle.fd(distance)



screen.exitonclick()