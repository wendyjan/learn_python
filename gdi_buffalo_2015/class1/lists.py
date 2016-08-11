"""
filename: lists.py
author: wendyjan

This file shows lists in Python using Turtle and printing.
"""
import turtle

if __name__ == "__main__":
    print "List basics!"
    my_list = [1, 1, 2, 3, 5, 8, 13, 21]
    print my_list
    for number in my_list: 
        print number
    
    print '\n'
    print "List indexing!"
    my_list[0]
    my_list[-1]
    my_list[1:5]
    # TODO Print the second-to-last element in the array.

    print '\n'
    print "Lists and types!"
    my_mixed_list = [1, 1, 2, 3, "shell", "petal", 13, 21.0]
    for thing in my_mixed_list:
	print thing, "is of type:", type(thing)

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

    print '\n'
    print "List slicing!"
    students = ["Wendy", "Anne", "Ryan", "Lena", "Jess"]
    print "The first two students to arrive are:",students[0:2]
    print "And the last three are:", students[-3:]
    # Print the last student to arrive in class.
    # Can you do it two different ways?

    print '\n'
    print "List shortcuts!"
    print range(5)
    for i in range(5):
        print i
    range(1, 6, 1)
    range(1, 6, 2)
    range(5, 0, -1)

    print "Copying a list!"
    list_a = range(10)
    print "list_a:", list_a
    list_b = list_a
    print "list_b = list_a"
    print "Now let's change the first element in list_b"
    print "We'll change it from", list_b[0], "to 200"
    list_b[0] = 200
    print "list_b is now:", list_b
    print "and list_a is:", list_a
    
    list_c = list_a[:]
    list_c[0] = 33
    print list_c, list_a

    fruit_list = ['apple','orange','pear']
    fruit_list.append('cherry')	
    print fruit_list
    fruit_list[4] = 'peach'	#error, cannot append with assignment in lists (can in dictionaries)
    fruit_list[2] = 'peach'	# okay, replaces item
    print fruit_list
    fruit_list.insert(1,'mango')
    print fruit_list
    fruit_list.remove('apple')
    del fruit_list[3]
    print fruit_list
    print fruit_list.pop()
    print fruit_list
