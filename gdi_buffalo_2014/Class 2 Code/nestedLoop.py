"""
Class 2 Example: Nested loops with turtle.

"""


import turtle

if __name__ == "__main__":

    # Draw two squares of different colors.
    # They will be on top of one another.
    alex = turtle.Turtle()
    for tempColor in ["red", "blue"]:
        alex.color(tempColor)
        for side in [1, 2, 3, 4]:
            alex.forward(50)
            alex.right(90)

#### Comment out everything above this line,
## Then uncomment the lines below to see squares of 2 different sizes.

##import turtle
##
##if __name__ == "__main__":
##
##    # Draw 2 squares of different colors and different sizes.
##    # They will be on top of one another but visible as two squares.
##    alex = turtle.Turtle()
##    for tempColor in ["red", "blue"]:
##        alex.color(tempColor)
##        for side in [1, 2, 3, 4]:
##            # Hint: len("red") is 3 and len("blue") is 4!
##            alex.forward(50 * len(tempColor)) 
##            alex.right(90)
