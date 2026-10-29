# Zealand Padilla
# 10/29/2026
# P4LAB1A
# Use turtle graphics, a while loop, and a for loop, to write a program that draws both a square and a triangle.

import turtle

# Create the turtle window and drawing object
win = turtle.Screen ()
pen = turtle.Turtle()


# Set turtle options
pen.pensize(5)
pen.pencolor("purple")
pen.shape("arrow")

# Draw the square
for i in range(4):
    pen.forward(200)
    pen.left(90)

# Move pen to the top of the square to draw the roof
pen.left(90)
pen.forward(200)
pen.right(30)

# Draw the triangle(roof)
pen.pencolor("blue")

sides = 3

while sides >0:
    pen.forward(200)
    pen.right(120)
    sides = sides - 1
    


# Wait for user to close window
win.mainloop()
