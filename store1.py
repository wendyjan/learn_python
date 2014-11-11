"""
Sample code for Intro to Python, Class 2.

This shows how to define a class.

Nothing should happen if you run this file!
"""

class Store:

    def __init__(self, newName):

        self.name = newName

        self.items = []

    def addItem(self, item, cost):

        newPair = [item, cost]

        self.items.append(newPair)

    def getAllItems(self):

        return self.items
