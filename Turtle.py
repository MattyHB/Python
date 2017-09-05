import turtle               # allows us to use the turtles library
wn = turtle.Screen()        # creates a graphics window
alex = turtle.Turtle()      # create a turtle named alex

for i in range(440):
    alex.forward(1)           # tell alex to move forward by 150 units
    alex.left(1)               # turn by 90 degrees
    alex.forward(1)            # complete the second side of a rectangle

alex.left(90)
alex.forward(230)

for i in range (360):
    alex.left(1)
    alex.forward(.25)
wn.exitonclick()