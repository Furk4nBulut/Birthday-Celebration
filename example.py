import random
import turtle
tur = turtle.Turtle()
turtle.bgcolor("black")
def draw_base():
    tur.penup()
    tur.goto(-170,-180)
    tur.color("white")
    tur.pendown()
    tur.forward(330)
def draw_middle():
    tur.penup()
    tur.goto(-160,-150)
    tur.color("white")
    tur.pendown()
    tur.forward(305)
def draw_top():
    tur.penup()
    tur.goto(-150,-120)
    tur.color("white")
    tur.pendown()
    tur.forward(280)
def draw_candle(color):
    tur.color(color)
    tur.forward(20)
    tur.left(90)
    tur.forward(50)
    tur.back(50)
    tur.right(90)
    tur.back(20)
    tur.forward(20)
def write_happy_birthday(color, font_size):
    tur.penup()
    tur.goto(-150, 50)
    tur.color(color)
    tur.pendown()
    tur.write("Doğum Günün Kutlu Olsun İrem!", font=("Arial", font_size, "bold"))
draw_base()
draw_middle()
draw_top()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

tur.penup()
tur.goto(-120,-120)
tur.pendown()
for i in range(10):
    draw_candle(random.choice(colors))
write_happy_birthday("yellow", 24)
tur.hideturtle()
turtle.exitonclick()
