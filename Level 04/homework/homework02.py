from turtle import *

# Set speed
speed = (30)
# Draw left koshkura
penup()
goto(-300, 0)
pendown()
left(90)
forward(250)
right(90)
forward(100)
right(90)
forward(250)
right(90)
forward(100)
# koshkura addon
penup()
goto(-300,100)
pendown()
# Draw center
penup()
goto(0, 0)
pendown()
begin_fill()  # Begin filling the shape
color("brown")  # Set color for the center
forward(196)
right(90)
forward(140)
right(90)
forward(30)
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(25)
right(90)
forward(140)
right(90)
forward(130)
end_fill()  # End filling the shape

# Draw right koshkura
penup()
goto(135, 0)
pendown()
begin_fill()  
color("brown") 
forward(4)
right(90)
forward(250)
right(90)
forward(100)
right(90)
forward(250)
right(90)
forward(100)
end_fill() 


#main koshkura
penup()
goto(0,-50)
right(90)
forward(150)
left(90)
forward(60)
right(90)
pendown()
forward(150)
right(90)
forward(80)
right(90)
forward(150)


#flag
width(3)
penup()
goto(0,249)
left(90)
pendown()
begin_fill()
color("peru")
forward(110)
right(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()
penup()
color("black")
width(5)
goto(-112,310)
pendown()
right(90)
forward(40)
right(90)
forward(20)
left(90)
right(180)
forward(8)
left(180)
forward(8)
left(90)
forward(20)
left(90)
forward(40)
left(90)
forward(20)
left(90)
forward(15)
left(90)
forward(5)
penup()
goto(-85,310)

#G
pendown()
right(90)
forward(40)
right(90)
forward(20)
right(90)
forward(40)
right(90)
forward(20)
penup()

#O
goto(-57,310)
pendown()
right(110)
forward(43)
right(140)
forward(45)

#A
penup()
goto(-35,320)
pendown()
right(110)
forward(15)
penup()
goto(1000,1000)
pendown()

color("yellow")
begin_fill()
circle(90)
end_fill()















exitonclick()
