from turtle import *
from random import randint

speed(8)
penup()
goto(-140, 140)

for step in range(15):
	write(step, align='center')
	right(90)
	forward(10)
	pendown()
	forward(150)
	penup()
	backward(160)
	left(90)
	forward(20)

ada = Turtle()
ada.color('dark magenta')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()

bob = Turtle()
bob.color('dodger blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 75)
bob.pendown()

steve = Turtle()
steve.color('gold')
steve.shape('turtle')

steve.penup()
steve.goto(-160, 50)
steve.pendown()

nancy = Turtle()
nancy.color('lime green')
nancy.shape('turtle')

nancy.penup()
nancy.goto(-160, 25)
nancy.pendown()

for turn in range(100):
	ada.forward(randint(1,5))
	bob.forward(randint(1,5))
	steve.forward(randint(1,5))
	nancy.forward(randint(1,5))
