"""
filename: functions_continued.py
author: wendyjan

This file shows more about functions.
"""

def add_together(a, b):
    print "Adding together", a, "and", b
    return a + b


def add_together_unknown(a, *args):
    result = a
    for n in args:
      result += n
    return result




if __name__ == "__main__":
    # Print a value returned from a function.
    result = add_together(2, 3)
    print "The result of add_together(2, 3) is", result

    # See the scope of a variable.
    # Comment out the following three lines unless you want an error!
    # result = add_together(5, 6)
    # print "Done adding together", a, "and", b
    # print "The result of add_together(5, 6) is", result

    # Another scope example. What's different about this one? Why did it work, when the previous one did not?
    a = 7
    b = 11
    result = add_together(a, b)
    print "Done adding together", a, "and", b
    print "The result of add_together(a, b) is", result
