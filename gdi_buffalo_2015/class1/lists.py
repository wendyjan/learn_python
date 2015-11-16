"""
filename: lists.py
author: wendyjan

This file shows lists in Python using Turtle and printing.
"""
import turtle

if __name__ == "__main__":
    for number in [1, 1, 2, 3, 5, 8, 13, 21]:
        print(number)
    ted = turtle.Turtle()
    ted.speed(1)
    for temp_color in ["red", "blue", "green", "black"]:
        ted.color(temp_color) 
        ted.forward(100)
        ted.right(90)
    for index in range(4):
        ted.forward(50)
        ted.right(90)
    turtle.done()
