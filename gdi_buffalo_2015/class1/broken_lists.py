"""
filename: broken_lists.py
author: wendyjan

This file has some syntax errors that will prevent it from running.
It also has a few mistakes in how it implements the tasks in its comments.

Take a look and fix it up!
"""

if __name__ == "__main__":
    
    grocery_list = ["apples", "cereal", "jerky", "milk", "cheetos", "ice cream"]
    
    # Print each grocery item on its own line.
    for item in grocery_list
        print item

    # Count the number of items.
    print "Total number of items to buy:", size(grocery_list)

    # Print the items on the grocery list that we forgot to purchase.
    purchased = ["apples", "jerky", "milk", "ice cream", "cereal"]
    still_needed = []
    for item in grocery_list:
	if item not in grocery_list:
		print "OOPS! We forgot", item 
		still_needed = still_needed + item

    # Now make a list of numbers (unrelated to the previous lists).
    numbers = range(20)
    print numbers
    
    # Print the smallest and largest numbers in the list.
    print "The smallest value in the list is:", numbers[1]
    print "and the largest value is:", numbers[len(numbers)] 
    
    # Print the list in reverse. 
    for i in range(len(numbers), 0, -1):
        print numbers[i]

    # Print every other number in the reversed list.
    for i in range(len(numbers)):
	if i / 2 == 0:
	    print numbers[i]

    # Shuffle the list, and find the index of the max number in it.
    random.shuffle(numbers)
    print numbers
    print "The largest number is", max(numbers), "at index", index(max(numbers))

