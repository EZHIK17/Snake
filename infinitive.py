from turtle import *

bgcolor('black')
color('white')
speed(11)
right(45)
for i in range(150):
    circle(30)
    if 7 < i < 65:
        left(5)
    if 80 < i < 135:
        right(5)
    if i < 80:
        forward(10)
    else:
        forward(5)
