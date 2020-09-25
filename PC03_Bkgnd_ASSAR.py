'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME GOES HERE <----------
May 29, 2020

PROGRAM DESCRIPTION GOES HERE <---------
'''

from turtle import * #import the library of commands that you'd like to use
import math #get a bunch of math commands
colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 700 # width of panel
h = 700 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

#=======Add your code here======

panel.bgcolor(0,0,0) # set background color


Turtle(visible = False) # create a turtle, make it invisible 
# BONUS: what kind of variable is "visible"?

#===================
# YOUR CODE HERE!
speed(0)
up()
goto(-200,0)
down()
colors = ['steel blue', 'red', 'light slate gray', 'honeydew']
hexogonalSpirograph = range(360)
for i in hexogonalSpirograph:
    color(colors[i%4])
    width(i / 250 + 1)
    forward(i/2)
    left(59)


up()
goto(200,0)
down()
squareSpirograph = range(19)
for i in squareSpirograph:
    for colors in ['steel blue', 'red', 'light slate gray', 'honeydew']:
        color(colors)
        width(2)
        left(5)
        forward(125)
        left(90)
        forward(125)
        left(90)
        forward(125)
        left(90)
        forward(125)
        left(90)
hideturtle()

#===================


# done()