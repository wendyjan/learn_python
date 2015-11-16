"""
Filename: BROKEN_turtle_forLoop.py

Author: Wendy Jansson



This file shows BROKEN code.

Can you fix it? Check the comments for hints.

--> There are 3 mistakes.


Solution code is posted to my github:
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
    nancy.down
    for i in range(5): # We changed the number of sides to 5.
        nancy.forward(100) 
        nancy.left(90)

    # The first mistake is on this next line.
    print("All done! Nancy drew 2 squares and a pentagon."
    

        

    
    

    
