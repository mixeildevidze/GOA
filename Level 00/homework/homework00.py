from turtle import *
speed(30)
#squeare

width(8)
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
#end of square


#door
forward(70)
color("grey")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200, 200)
pendown()
#roof
right(150)
color("saddle brown")
begin_fill()
forward(200)
left(120)
forward(200)
end_fill()


#window 1
color("cyan")
begin_fill()
penup()
goto(20,130)
pendown()
right(150)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
end_fill()
#window 2
color("cyan")
begin_fill()
penup()
goto(180, 130)
pendown()
left(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
end_fill()






exitonclick()
