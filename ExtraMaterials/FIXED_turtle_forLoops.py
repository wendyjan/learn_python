"""
Filename: FIXED_turtle_forLoop.py

Author: Wendy Jansson



This file shows FIXED code.

Check the comments for the solutions. 

The broken code is posted to my github:
go to https://github.com/wendyjan/learnPython,
and look in the folder "ExtraMaterial".


"""

import turtle

if __name__ == "__main__":

    nancy = turtle.Turtle()
    
    nancy.down()
    print("Nancy begins at position: " + str(nancy.pos()))
    for i in range(4):
        nancy.forward(100)
        nancy.left(90)
    print("Nancy completed her first square. Now she wants to draw a blue square.")

    print("Nancy would rather begin the blue square in a new place.")
    nancy.up()
    nancy.pencolor("blue")
    nancy.goto(100, 100)
    nancy.down()
    for i in range(4):
        nancy.forward(100)
        nancy.left(90)
    print("Nancy completed her blue square. Now she wants to draw a big red pentagon.")

    print("Nancy wants to draw the red pentagon in a new place.")
    nancy.up()
    nancy.pencolor("red")
    nancy.goto(-100, -100)
    nancy.down()
    # Don't forget to add parentheses! "down()" is a method, so it needs parentheses.
    for i in range(5): 
        nancy.forward(100)
        nancy.left(72)
        # This angle needs to be 360 / (numberOfSides), so it should be 72.

    print("All done! Nancy drew 2 squares and a pentagon.")
    # "Unexpected EOF" means "unexpected end-of-file". Don't forget the last parentheses!
    

        

    
    

    
