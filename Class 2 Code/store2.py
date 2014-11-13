"""
Sample code for Intro to Python, Class 2.

This shows how to define a class.

Nothing should happen if you run this file!

VERSION TWO, with better methods!
"""

class Store:

    def __init__(self, newName):

        self.name = newName

        self.items = []

    def addItem(self, item, cost):

        newPair = [item, cost]
        self.items.append(newPair)
        print ("Item added: " + str(item) + ", cost: " + str(cost))
        

    def getAllItems(self):

        stringToReturn = "Inventory of " + self.name + ": " + "\n"

        for item in self.items:
            thing = item[0]
            cost = item[1]
            stringToReturn += ("Item: " + str(thing) + ", cost: " + str(cost))
            stringToReturn += "\n"

        return stringToReturn
