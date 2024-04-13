from turtle import *

speed (30)
#we want to paint a house

#step 1 draw a square
width(7)
color("brown")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of the square

#drawing a door
forward (70)
color ("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200,200)
pendown()


color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
# first window

penup()
goto(10,100)
pendown()
color("blue")
begin_fill()
right(240)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()
#second window
penup()
goto(190,100)
pendown()
color("blue")
begin_fill()
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()














exitonclick()
