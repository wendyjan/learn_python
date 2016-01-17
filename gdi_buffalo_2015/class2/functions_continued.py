"""
filename: functions_continued.py
author: wendyjan

This file shows more about functions.
"""

def say_hi():
    print "Hello World!"


def say_hi_personally(person):
    print "Hello " + person + "!"


def add_together(a, b):
    return a + b


def calculate_y(m, x, b):
    return m * x + b


def add_together_many(a, *args):
    result = a
    for n in args:
      result += n
    return result


def scale_list(my_list):
    # TODO please implement this!
    pass


if __name__ == "__main__":
    # Call a function.
    say_hi()

    # Call a function with a parameter (also called an argument).
    say_hi_personally("Elena")

    # Print a value returned from a function.
    result = add_together(2, 3)
    print "The first result is:", result

    # See the scope of a variable.
    # Comment out the following three lines unless you want an error!
    # result = add_together(5, 6)
    # print "Done adding together", a, "and", b
    # print "The result of add_together(5, 6) is", result

    # Another scope example. What's different about this one? 
    # Why did it work, when the previous one in comments did not?
    a = 7
    b = 11
    result = add_together(a, b)
    print "Done adding together", a, "and", b
    print "The result of add_together(a, b) is", result

    # Now what if we want to give three parameters?
    print "Given the formula y = 3x + 5, what is y when x is 8?"
    print "Don't forget that old formula, y = mx + b."
    print "y =", calculate_y(3, 8, 5)

    # What about an arbitrary number of parameters?
    result = add_together_many(1, 2, 3, 4, 5, 6)
    print "All of those together equal:", result

    # Now what if we have a list, and want to multiply each element?
    my_list = range(5)
    print my_list, "scaled by 3 is", my_list * 5
    print "Oops!!! No!!! I meant to say it's", scale_list(my_list)
    # Hmm... looks like this needs work! 

