from turtle import *
width(4)

def kvadrati():
    for i in range(4):
        forward(250)
        left(90)
        forward(150)
        left(90)
        forward(250)
        left(90)
        forward(150)
        left(90)  #

def kvadrati1():
    for i in range(4):
        kvadrati()
        penup()
        forward(250)  
        pendown()

kvadrati1()
exitonclick()
