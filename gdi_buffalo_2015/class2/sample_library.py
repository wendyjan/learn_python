"""
filename: sample_library.py
author: wendyjan

Small start to our own library to write letters in Turtle.
"""

import turtle


def print_w(t, start_x, start_y):
    """Draws an uppercase 'W' in Turtle. 

    Args:
       t (turtle.Turtle): used to draw letter.
       start_x (int): starting x coordinate at lower left of letter.
       start_y (int): starting y coordinate at lower left of letter.
    """
    t.penup()
    t.goto(start_x, start_y + 30) # Assume total letter size is 20x30
    t.pendown()
    t.goto(start_x + 7, start_y)
    t.goto(start_x + 15, start_y + 10)
    t.goto(start_x + 23, start_y)
    t.goto(start_x + 30, start_y + 30)
    t.penup()


def print_j(t, start_x, start_y):
    """Draws an uppercase 'W' in Turtle. 

    Args:
       t (turtle.Turtle): used to draw letter.
       start_x (int): starting x coordinate at lower left of letter.
       start_y (int): starting y coordinate at lower left of letter.
    """
    t.penup()
    t.goto(start_x, start_y + 30)
    t.pendown()
    t.goto(start_x + 20, start_y + 30)
    t.penup()    
    t.goto(start_x, start_y + 30)
    t.pendown()
    t.goto(start_x, start_y)
    t.goto(start_x + 20, start_y)
    t.penup()
    t.goto(start_x, start_y + 15)
    t.pendown()
    t.goto(start_x + 15, start_y + 15)
    t.penup()


if __name__ == "__main__":
    my_turtle = turtle.Turtle()
    wn = turtle.Screen()
    print_w(my_turtle, 0, 0)
    print_j(my_turtle, 35, 0)
    wn.exitonclick()
